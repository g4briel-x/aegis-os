"""Persistent execution audit history inspection for Aegis OS."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

from .audit import (
    ExecutionAuditEvent,
    ExecutionAuditEventType,
)
from .models import ExecutionMode
from .session import ExecutionSessionState
from .workspace_store import StoredExecutionSession


@dataclass(slots=True, frozen=True)
class ExecutionAuditHistory:
    """Validated audit history for one execution session."""

    session_id: str
    workspace_id: str
    target_asset_id: str
    mode: ExecutionMode
    state: ExecutionSessionState
    audit_manifest: Path
    created_at: datetime
    updated_at: datetime
    started_at: datetime | None = None
    completed_at: datetime | None = None
    audit_metadata: dict[str, Any] = field(
        default_factory=dict
    )
    events: tuple[ExecutionAuditEvent, ...] = field(
        default_factory=tuple
    )

    @property
    def event_count(self) -> int:
        """Return the number of validated audit events."""

        return len(self.events)

    @property
    def first_event_at(self) -> str | None:
        """Return the first event timestamp."""

        if not self.events:
            return None

        return self.events[0].timestamp

    @property
    def last_event_at(self) -> str | None:
        """Return the last event timestamp."""

        if not self.events:
            return None

        return self.events[-1].timestamp

    def select(
        self,
        *,
        event_type: ExecutionAuditEventType | None = None,
        actor: str = "",
        limit: int | None = None,
        reverse: bool = False,
    ) -> tuple[ExecutionAuditEvent, ...]:
        """Select audit events without mutating the history."""

        if limit is not None and limit <= 0:
            raise ValueError(
                "Audit history limit must be greater than zero."
            )

        normalized_actor = actor.strip()

        selected: Iterable[ExecutionAuditEvent] = (
            reversed(self.events)
            if reverse
            else self.events
        )

        filtered: list[ExecutionAuditEvent] = []

        for event in selected:
            if (
                event_type is not None
                and event.event_type != event_type
            ):
                continue

            if (
                normalized_actor
                and event.actor != normalized_actor
            ):
                continue

            filtered.append(event)

            if (
                limit is not None
                and len(filtered) >= limit
            ):
                break

        return tuple(filtered)

    def to_dict(self) -> dict[str, Any]:
        """Serialize the validated audit history."""

        return {
            "session_id": self.session_id,
            "workspace_id": self.workspace_id,
            "target_asset_id": self.target_asset_id,
            "mode": self.mode.value,
            "state": self.state.value,
            "audit_manifest": str(self.audit_manifest),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "started_at": (
                self.started_at.isoformat()
                if self.started_at
                else None
            ),
            "completed_at": (
                self.completed_at.isoformat()
                if self.completed_at
                else None
            ),
            "audit_metadata": dict(
                self.audit_metadata
            ),
            "event_count": self.event_count,
            "first_event_at": self.first_event_at,
            "last_event_at": self.last_event_at,
            "events": [
                event.to_dict()
                for event in self.events
            ],
        }


class ExecutionAuditHistoryReader:
    """Load and validate persistent execution audit history."""

    def load(
        self,
        record: StoredExecutionSession,
    ) -> ExecutionAuditHistory:
        """Load one audit history from a stored session."""

        workspace_path = record.workspace_path.resolve()

        if not workspace_path.is_dir():
            raise FileNotFoundError(
                "Execution workspace does not exist: "
                f"{workspace_path}"
            )

        audit_manifest = self._audit_manifest_path(
            record
        )

        if not audit_manifest.is_file():
            raise FileNotFoundError(
                "Execution audit manifest does not exist: "
                f"{audit_manifest}"
            )

        payload = self._read_json_object(
            audit_manifest
        )

        session_id = self._required_string(
            payload,
            "session_id",
            "execution audit manifest",
        )
        workspace_id = self._required_string(
            payload,
            "workspace_id",
            "execution audit manifest",
        )
        target_asset_id = self._required_string(
            payload,
            "target_asset_id",
            "execution audit manifest",
        )

        if session_id != record.session_id:
            raise ValueError(
                "Audit session ID does not match "
                "the stored execution session."
            )

        if workspace_id != record.workspace_id:
            raise ValueError(
                "Audit workspace ID does not match "
                "the stored execution workspace."
            )

        session_payload = record.payload.get(
            "session"
        )

        if not isinstance(session_payload, dict):
            raise ValueError(
                "Stored execution session must be "
                "a JSON object."
            )

        stored_target = self._required_string(
            session_payload,
            "target_asset_id",
            "stored execution session",
        )
        stored_mode = self._required_string(
            session_payload,
            "mode",
            "stored execution session",
        )
        stored_state = self._required_string(
            session_payload,
            "state",
            "stored execution session",
        )

        if target_asset_id != stored_target:
            raise ValueError(
                "Audit target asset does not match "
                "the stored execution session."
            )

        mode = self._parse_mode(
            payload
        )
        state = self._parse_state(
            payload
        )

        if mode.value != stored_mode:
            raise ValueError(
                "Audit execution mode does not match "
                "the stored execution session."
            )

        if state.value != stored_state:
            raise ValueError(
                "Audit execution state does not match "
                "the stored execution session."
            )

        created_at = self._parse_datetime_field(
            payload,
            "created_at",
            required=True,
        )
        updated_at = self._parse_datetime_field(
            payload,
            "updated_at",
            required=True,
        )
        started_at = self._parse_datetime_field(
            payload,
            "started_at",
            required=False,
        )
        completed_at = self._parse_datetime_field(
            payload,
            "completed_at",
            required=False,
        )

        assert created_at is not None
        assert updated_at is not None

        self._validate_session_timestamps(
            created_at=created_at,
            updated_at=updated_at,
            started_at=started_at,
            completed_at=completed_at,
        )

        audit_metadata = payload.get(
            "audit_metadata",
            {},
        )

        if not isinstance(audit_metadata, dict):
            raise ValueError(
                "Execution audit metadata must "
                "be a JSON object."
            )

        events = self._parse_events(
            payload=payload,
            session_id=session_id,
            workspace_id=workspace_id,
            created_at=created_at,
        )

        self._validate_event_summary(
            payload=payload,
            events=events,
        )

        return ExecutionAuditHistory(
            session_id=session_id,
            workspace_id=workspace_id,
            target_asset_id=target_asset_id,
            mode=mode,
            state=state,
            audit_manifest=audit_manifest,
            created_at=created_at,
            updated_at=updated_at,
            started_at=started_at,
            completed_at=completed_at,
            audit_metadata=dict(
                audit_metadata
            ),
            events=events,
        )

    def _parse_events(
        self,
        payload: dict[str, Any],
        session_id: str,
        workspace_id: str,
        created_at: datetime,
    ) -> tuple[ExecutionAuditEvent, ...]:
        """Parse and validate stored audit events."""

        raw_events = payload.get(
            "events",
            [],
        )

        if not isinstance(raw_events, list):
            raise ValueError(
                "Stored execution audit events "
                "must be a JSON array."
            )

        events: list[ExecutionAuditEvent] = []
        event_ids: set[str] = set()
        previous_timestamp: datetime | None = None

        for index, raw_event in enumerate(
            raw_events
        ):
            if not isinstance(raw_event, dict):
                raise ValueError(
                    "Stored execution audit event "
                    f"at index {index} must be a JSON object."
                )

            event = self._parse_event(
                payload=raw_event,
                index=index,
            )

            if event.session_id != session_id:
                raise ValueError(
                    "Audit event session ID does not match "
                    f"the audit history at index {index}."
                )

            if event.workspace_id != workspace_id:
                raise ValueError(
                    "Audit event workspace ID does not match "
                    f"the audit history at index {index}."
                )

            if event.event_id in event_ids:
                raise ValueError(
                    "Execution audit event IDs "
                    "must be unique."
                )

            event_ids.add(
                event.event_id
            )

            event_timestamp = self._parse_datetime_value(
                event.timestamp,
                (
                    "execution audit event timestamp "
                    f"at index {index}"
                ),
            )

            if event_timestamp < created_at:
                raise ValueError(
                    "Execution audit event cannot occur "
                    "before session creation."
                )

            if (
                previous_timestamp is not None
                and event_timestamp < previous_timestamp
            ):
                raise ValueError(
                    "Execution audit events must be "
                    "stored in chronological order."
                )

            previous_timestamp = event_timestamp
            events.append(event)

        return tuple(events)

    def _parse_event(
        self,
        payload: dict[str, Any],
        index: int,
    ) -> ExecutionAuditEvent:
        """Reconstruct one immutable audit event."""

        event_type_value = self._required_string(
            payload,
            "event_type",
            f"execution audit event at index {index}",
        )

        try:
            event_type = ExecutionAuditEventType(
                event_type_value
            )
        except ValueError as exc:
            raise ValueError(
                "Unsupported execution audit event type "
                f"at index {index}: {event_type_value}"
            ) from exc

        metadata = payload.get(
            "metadata",
            {},
        )

        if not isinstance(metadata, dict):
            raise ValueError(
                "Execution audit event metadata "
                f"at index {index} must be a JSON object."
            )

        return ExecutionAuditEvent(
            event_id=self._required_string(
                payload,
                "event_id",
                f"execution audit event at index {index}",
            ),
            event_type=event_type,
            session_id=self._required_string(
                payload,
                "session_id",
                f"execution audit event at index {index}",
            ),
            workspace_id=self._required_string(
                payload,
                "workspace_id",
                f"execution audit event at index {index}",
            ),
            timestamp=self._required_string(
                payload,
                "timestamp",
                f"execution audit event at index {index}",
            ),
            actor=self._required_string(
                payload,
                "actor",
                f"execution audit event at index {index}",
            ),
            message=self._required_string(
                payload,
                "message",
                f"execution audit event at index {index}",
            ),
            previous_state=self._optional_string(
                payload,
                "previous_state",
                f"execution audit event at index {index}",
            ),
            next_state=self._optional_string(
                payload,
                "next_state",
                f"execution audit event at index {index}",
            ),
            metadata=dict(metadata),
        )

    def _validate_event_summary(
        self,
        payload: dict[str, Any],
        events: tuple[ExecutionAuditEvent, ...],
    ) -> None:
        """Validate stored event summary fields."""

        stored_count = payload.get(
            "event_count"
        )

        if stored_count is not None:
            if (
                isinstance(stored_count, bool)
                or not isinstance(stored_count, int)
            ):
                raise ValueError(
                    "Stored audit event count must "
                    "be an integer."
                )

            if stored_count != len(events):
                raise ValueError(
                    "Stored audit event count does not "
                    "match the event collection."
                )

        stored_last_event_at = payload.get(
            "last_event_at"
        )

        if events:
            if (
                not isinstance(stored_last_event_at, str)
                or not stored_last_event_at.strip()
            ):
                raise ValueError(
                    "Stored audit history with events "
                    "requires last_event_at."
                )

            last_timestamp = self._parse_datetime_value(
                events[-1].timestamp,
                "last execution audit event timestamp",
            )
            summary_timestamp = self._parse_datetime_value(
                stored_last_event_at,
                "stored audit last_event_at",
            )

            if summary_timestamp != last_timestamp:
                raise ValueError(
                    "Stored audit last_event_at does not "
                    "match the final event timestamp."
                )

        elif stored_last_event_at not in {
            None,
            "",
        }:
            raise ValueError(
                "Stored audit history without events "
                "cannot declare last_event_at."
            )

    def _parse_mode(
        self,
        payload: dict[str, Any],
    ) -> ExecutionMode:
        """Parse the stored execution mode."""

        value = self._required_string(
            payload,
            "mode",
            "execution audit manifest",
        )

        try:
            return ExecutionMode(value)
        except ValueError as exc:
            raise ValueError(
                f"Unsupported audit execution mode: {value}"
            ) from exc

    def _parse_state(
        self,
        payload: dict[str, Any],
    ) -> ExecutionSessionState:
        """Parse the stored execution state."""

        value = self._required_string(
            payload,
            "state",
            "execution audit manifest",
        )

        try:
            return ExecutionSessionState(value)
        except ValueError as exc:
            raise ValueError(
                f"Unsupported audit execution state: {value}"
            ) from exc

    def _validate_session_timestamps(
        self,
        *,
        created_at: datetime,
        updated_at: datetime,
        started_at: datetime | None,
        completed_at: datetime | None,
    ) -> None:
        """Validate chronological session timestamps."""

        if updated_at < created_at:
            raise ValueError(
                "Execution audit updated_at cannot "
                "precede created_at."
            )

        if (
            started_at is not None
            and started_at < created_at
        ):
            raise ValueError(
                "Execution audit started_at cannot "
                "precede created_at."
            )

        if (
            completed_at is not None
            and completed_at < created_at
        ):
            raise ValueError(
                "Execution audit completed_at cannot "
                "precede created_at."
            )

        if (
            started_at is not None
            and completed_at is not None
            and completed_at < started_at
        ):
            raise ValueError(
                "Execution audit completed_at cannot "
                "precede started_at."
            )

    def _parse_datetime_field(
        self,
        payload: dict[str, Any],
        field_name: str,
        *,
        required: bool,
    ) -> datetime | None:
        """Parse one datetime field from a manifest."""

        value = payload.get(
            field_name
        )

        if value is None:
            if required:
                raise ValueError(
                    "Execution audit manifest requires "
                    f"'{field_name}'."
                )

            return None

        if (
            not isinstance(value, str)
            or not value.strip()
        ):
            raise ValueError(
                "Execution audit datetime field "
                f"'{field_name}' must be a non-empty string."
            )

        return self._parse_datetime_value(
            value,
            f"execution audit field '{field_name}'",
        )

    def _parse_datetime_value(
        self,
        value: str,
        description: str,
    ) -> datetime:
        """Parse one timezone-aware ISO datetime."""

        try:
            parsed = datetime.fromisoformat(
                value
            )
        except ValueError as exc:
            raise ValueError(
                f"Invalid ISO datetime for {description}: "
                f"{value}"
            ) from exc

        if parsed.utcoffset() is None:
            raise ValueError(
                f"{description} must be timezone-aware."
            )

        return parsed

    def _audit_manifest_path(
        self,
        record: StoredExecutionSession,
    ) -> Path:
        """Resolve the declared session audit manifest."""

        workspace_payload = record.payload.get(
            "workspace"
        )

        if not isinstance(workspace_payload, dict):
            raise ValueError(
                "Stored workspace must be a JSON object."
            )

        locations = workspace_payload.get(
            "locations"
        )

        if not isinstance(locations, list):
            raise ValueError(
                "Stored workspace locations must "
                "be a JSON array."
            )

        relative_path = ""

        for location in locations:
            if not isinstance(location, dict):
                raise ValueError(
                    "Stored workspace location must "
                    "be a JSON object."
                )

            if location.get("name") != "session-audit":
                continue

            value = location.get(
                "relative_path"
            )

            if (
                not isinstance(value, str)
                or not value.strip()
            ):
                raise ValueError(
                    "Stored session-audit location "
                    "has no valid relative path."
                )

            relative_path = value.strip()
            break

        if not relative_path:
            raise ValueError(
                "Stored workspace does not declare "
                "a session-audit location."
            )

        relative = Path(
            relative_path
        )

        if (
            relative.is_absolute()
            or ".." in relative.parts
        ):
            raise ValueError(
                "Stored session-audit location "
                "is not workspace-relative."
            )

        workspace_path = record.workspace_path.resolve()
        audit_manifest = (
            workspace_path / relative
        ).resolve()

        if (
            audit_manifest != workspace_path
            and workspace_path
            not in audit_manifest.parents
        ):
            raise ValueError(
                "Execution audit manifest resolves "
                "outside the workspace."
            )

        return audit_manifest

    def _read_json_object(
        self,
        path: Path,
    ) -> dict[str, Any]:
        """Read and validate one JSON object."""

        try:
            payload = json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                "Execution audit manifest contains "
                f"invalid JSON: {path}"
            ) from exc

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit manifest must "
                "contain a JSON object."
            )

        return dict(payload)

    def _required_string(
        self,
        payload: dict[str, Any],
        field_name: str,
        description: str,
    ) -> str:
        """Read one required non-empty string."""

        value = payload.get(
            field_name
        )

        if (
            not isinstance(value, str)
            or not value.strip()
        ):
            raise ValueError(
                f"{description} requires a valid "
                f"'{field_name}' string."
            )

        return value.strip()

    def _optional_string(
        self,
        payload: dict[str, Any],
        field_name: str,
        description: str,
    ) -> str:
        """Read one optional string."""

        value = payload.get(
            field_name
        )

        if value is None:
            return ""

        if not isinstance(value, str):
            raise ValueError(
                f"{description} field "
                f"'{field_name}' must be a string or null."
            )

        return value.strip()