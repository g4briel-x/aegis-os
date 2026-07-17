"""Persistent execution lifecycle storage for Aegis OS."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from uuid import uuid4

from .lifecycle import ExecutionLifecycleResult
from .workspace_store import StoredExecutionSession


@dataclass(slots=True, frozen=True)
class PersistedExecutionLifecycle:
    """Paths updated while persisting a lifecycle transition."""

    workspace_path: Path
    session_manifest: Path
    audit_manifest: Path
    event_count: int
    terminal_state: str

    def to_dict(self) -> dict[str, Any]:
        """Serialize persisted lifecycle information."""

        return {
            "workspace_path": str(self.workspace_path),
            "session_manifest": str(self.session_manifest),
            "audit_manifest": str(self.audit_manifest),
            "event_count": self.event_count,
            "terminal_state": self.terminal_state,
        }


class ExecutionLifecycleStore:
    """Persist terminal lifecycle states and audit events."""

    def persist(
        self,
        record: StoredExecutionSession,
        result: ExecutionLifecycleResult,
    ) -> PersistedExecutionLifecycle:
        """Persist one successful terminal lifecycle transition."""

        self._validate_result(
            record=record,
            result=result,
        )

        workspace_path = record.workspace_path.resolve()

        if not workspace_path.is_dir():
            raise FileNotFoundError(
                "Execution workspace does not exist: "
                f"{workspace_path}"
            )

        session_manifest = (
            record.session_manifest.resolve()
        )

        self._require_inside_workspace(
            workspace_path=workspace_path,
            target=session_manifest,
        )

        if not session_manifest.is_file():
            raise FileNotFoundError(
                "Execution session manifest does not exist: "
                f"{session_manifest}"
            )

        audit_manifest = self._audit_manifest_path(
            record=record,
        )

        if not audit_manifest.is_file():
            raise FileNotFoundError(
                "Execution audit manifest does not exist: "
                f"{audit_manifest}"
            )

        session_payload = dict(record.payload)

        audit_payload = self._read_json_object(
            audit_manifest,
            "execution audit manifest",
        )

        serialized_events = [
            event.to_dict()
            for event in result.events
        ]

        existing_events = audit_payload.get(
            "events",
            [],
        )

        if not isinstance(existing_events, list):
            raise ValueError(
                "Stored execution audit events "
                "must be a JSON array."
            )

        all_events = [
            *existing_events,
            *serialized_events,
        ]

        last_event_at = (
            result.events[-1].timestamp
            if result.events
            else None
        )

        lifecycle_summary = {
            "ok": result.ok,
            "action": result.action.value,
            "terminal_state": (
                result.terminal_state.value
            ),
            "reason": result.reason,
            "actor": result.actor,
            "event_count": len(serialized_events),
            "event_ids": [
                event.event_id
                for event in result.events
            ],
            "last_event_at": last_event_at,
        }

        session_payload["session"] = (
            result.session.to_dict()
        )

        session_payload["lifecycle"] = (
            lifecycle_summary
        )

        audit_payload.update(
            {
                "session_id": result.session.session_id,
                "workspace_id": (
                    result.session.workspace_id
                ),
                "target_asset_id": (
                    result.session.target_asset_id
                ),
                "mode": result.session.mode.value,
                "state": result.session.state.value,
                "created_at": (
                    result.session.created_at.isoformat()
                ),
                "updated_at": (
                    result.session.updated_at.isoformat()
                ),
                "started_at": (
                    result.session.started_at.isoformat()
                    if result.session.started_at
                    else None
                ),
                "completed_at": (
                    result.session.completed_at.isoformat()
                    if result.session.completed_at
                    else None
                ),
                "audit_metadata": dict(
                    result.session.audit_metadata
                ),
                "lifecycle": lifecycle_summary,
                "event_count": len(all_events),
                "last_event_at": last_event_at,
                "events": all_events,
            }
        )

        # Audit is replaced first. The session manifest is
        # written last and acts as the committed session state.
        self._write_json_atomic(
            path=audit_manifest,
            payload=audit_payload,
        )

        self._write_json_atomic(
            path=session_manifest,
            payload=session_payload,
        )

        return PersistedExecutionLifecycle(
            workspace_path=workspace_path,
            session_manifest=session_manifest,
            audit_manifest=audit_manifest,
            event_count=len(serialized_events),
            terminal_state=(
                result.terminal_state.value
            ),
        )

    def _validate_result(
        self,
        record: StoredExecutionSession,
        result: ExecutionLifecycleResult,
    ) -> None:
        """Validate lifecycle result and storage identities."""

        if not result.ok:
            raise ValueError(
                "Only a successful execution lifecycle "
                "result can be persisted."
            )

        if not result.session.is_terminal:
            raise ValueError(
                "Lifecycle persistence requires "
                "a terminal execution session."
            )

        if (
            result.session.session_id
            != record.session_id
        ):
            raise ValueError(
                "Lifecycle session ID does not "
                "match the stored session."
            )

        if (
            result.session.workspace_id
            != record.workspace_id
        ):
            raise ValueError(
                "Lifecycle workspace ID does not "
                "match the stored workspace."
            )

        if not result.events:
            raise ValueError(
                "Lifecycle result contains "
                "no audit events."
            )

        for event in result.events:
            if (
                event.session_id
                != result.session.session_id
            ):
                raise ValueError(
                    "Audit event session ID does not "
                    "match the lifecycle session."
                )

            if (
                event.workspace_id
                != result.session.workspace_id
            ):
                raise ValueError(
                    "Audit event workspace ID does not "
                    "match the lifecycle workspace."
                )

    def _audit_manifest_path(
        self,
        record: StoredExecutionSession,
    ) -> Path:
        """Resolve the declared session-audit location."""

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

            if location.get("name") == "session-audit":
                value = location.get("relative_path")

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

        relative = Path(relative_path)

        if (
            relative.is_absolute()
            or ".." in relative.parts
        ):
            raise ValueError(
                "Stored session-audit location "
                "is not workspace-relative."
            )

        target = (
            record.workspace_path
            / relative
        ).resolve()

        self._require_inside_workspace(
            workspace_path=(
                record.workspace_path.resolve()
            ),
            target=target,
        )

        return target

    def _require_inside_workspace(
        self,
        workspace_path: Path,
        target: Path,
    ) -> None:
        """Require a path to remain inside its workspace."""

        resolved_workspace = workspace_path.resolve()
        resolved_target = target.resolve()

        if (
            resolved_target != resolved_workspace
            and resolved_workspace
            not in resolved_target.parents
        ):
            raise ValueError(
                "Persistent lifecycle path "
                "resolves outside the workspace."
            )

    def _read_json_object(
        self,
        path: Path,
        description: str,
    ) -> dict[str, Any]:
        """Read and validate one stored JSON object."""

        try:
            payload = json.loads(
                path.read_text(
                    encoding="utf-8"
                )
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Stored {description} contains invalid JSON: "
                f"{path}"
            ) from exc

        if not isinstance(payload, dict):
            raise ValueError(
                f"Stored {description} must "
                "contain a JSON object."
            )

        return dict(payload)

    def _write_json_atomic(
        self,
        path: Path,
        payload: dict[str, Any],
    ) -> None:
        """Replace one JSON manifest atomically."""

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        temporary_path = path.with_name(
            f".{path.name}.{uuid4().hex}.tmp"
        )

        try:
            temporary_path.write_text(
                json.dumps(
                    payload,
                    indent=2,
                    ensure_ascii=False,
                    sort_keys=True,
                )
                + "\n",
                encoding="utf-8",
            )

            temporary_path.replace(path)
        finally:
            if temporary_path.exists():
                temporary_path.unlink()