"""Persisted execution session rehydration for Aegis OS."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .context import (
    ExecutionArtifact,
    ExecutionContext,
    ExecutionEnvironment,
    ResolvedExecutionInput,
)
from .models import ExecutionMode
from .session import (
    ExecutionSession,
    ExecutionSessionState,
)
from .workspace_store import StoredExecutionSession


class ExecutionSessionLoader:
    """Rebuild executable session objects from persistent storage."""

    def load(
        self,
        record: StoredExecutionSession,
    ) -> ExecutionSession:
        """Rehydrate one stored execution session."""

        session_payload = self._mapping(
            record.payload.get("session"),
            "session",
        )

        session_id = self._required_text(
            session_payload,
            "session_id",
        )

        workspace_id = self._required_text(
            session_payload,
            "workspace_id",
        )

        if session_id != record.session_id:
            raise ValueError(
                "Stored session ID does not match its record."
            )

        if workspace_id != record.workspace_id:
            raise ValueError(
                "Stored workspace ID does not match its record."
            )

        mode = self._execution_mode(
            session_payload.get("mode")
        )

        state = self._session_state(
            session_payload.get("state")
        )

        context_payload = self._mapping(
            session_payload.get("context"),
            "session context",
        )

        context = self._build_context(
            context_payload
        )

        target_asset_id = self._required_text(
            session_payload,
            "target_asset_id",
        )

        if context.target_asset_id != target_asset_id:
            raise ValueError(
                "Stored execution context target does not "
                "match the session target."
            )

        if context.mode != mode:
            raise ValueError(
                "Stored execution context mode does not "
                "match the session mode."
            )

        return ExecutionSession(
            target_asset_id=target_asset_id,
            mode=mode,
            session_id=session_id,
            state=state,
            created_at=self._datetime(
                session_payload.get("created_at"),
                "created_at",
            ),
            updated_at=self._datetime(
                session_payload.get("updated_at"),
                "updated_at",
            ),
            started_at=self._optional_datetime(
                session_payload.get("started_at"),
                "started_at",
            ),
            completed_at=self._optional_datetime(
                session_payload.get("completed_at"),
                "completed_at",
            ),
            context=context,
            workspace_id=workspace_id,
            audit_metadata=self._optional_mapping(
                session_payload.get("audit_metadata"),
                "audit_metadata",
            ),
            metadata=self._optional_mapping(
                session_payload.get("metadata"),
                "metadata",
            ),
        )

    def _build_context(
        self,
        payload: dict[str, Any],
    ) -> ExecutionContext:
        """Rebuild one execution context."""

        resolved_inputs_payload = self._list(
            payload.get("resolved_inputs"),
            "resolved_inputs",
        )

        resolved_inputs = []

        for item in resolved_inputs_payload:
            input_payload = self._mapping(
                item,
                "resolved input",
            )

            resolved_inputs.append(
                ResolvedExecutionInput(
                    name=self._required_text(
                        input_payload,
                        "name",
                    ),
                    value=input_payload.get("value"),
                    source=self._required_text(
                        input_payload,
                        "source",
                    ),
                    required=bool(
                        input_payload.get(
                            "required",
                            False,
                        )
                    ),
                )
            )

        environment_payload = self._mapping(
            payload.get("environment"),
            "environment",
        )

        variables_payload = self._optional_mapping(
            environment_payload.get("variables"),
            "environment variables",
        )

        environment = ExecutionEnvironment(
            name=str(
                environment_payload.get(
                    "name",
                    "local",
                )
            ),
            working_directory=str(
                environment_payload.get(
                    "working_directory",
                    "",
                )
            ),
            python_version=str(
                environment_payload.get(
                    "python_version",
                    "",
                )
            ),
            platform=str(
                environment_payload.get(
                    "platform",
                    "",
                )
            ),
            variables={
                str(key): str(value)
                for key, value in variables_payload.items()
            },
        )

        artifacts_payload = self._list(
            payload.get("artifacts"),
            "artifacts",
        )

        artifacts = []

        for item in artifacts_payload:
            artifact_payload = self._mapping(
                item,
                "execution artifact",
            )

            artifacts.append(
                ExecutionArtifact(
                    name=self._required_text(
                        artifact_payload,
                        "name",
                    ),
                    artifact_type=self._required_text(
                        artifact_payload,
                        "artifact_type",
                    ),
                    location=str(
                        artifact_payload.get(
                            "location",
                            "",
                        )
                    ),
                    metadata=self._optional_mapping(
                        artifact_payload.get(
                            "metadata"
                        ),
                        "artifact metadata",
                    ),
                )
            )

        return ExecutionContext(
            target_asset_id=self._required_text(
                payload,
                "target_asset_id",
            ),
            mode=self._execution_mode(
                payload.get("mode")
            ),
            parameters=self._optional_mapping(
                payload.get("parameters"),
                "context parameters",
            ),
            resolved_inputs=resolved_inputs,
            environment=environment,
            artifacts=artifacts,
            metadata=self._optional_mapping(
                payload.get("metadata"),
                "context metadata",
            ),
        )

    def _mapping(
        self,
        value: Any,
        field_name: str,
    ) -> dict[str, Any]:
        """Require one JSON object."""

        if not isinstance(value, dict):
            raise ValueError(
                f"Stored {field_name} must be a JSON object."
            )

        return dict(value)

    def _optional_mapping(
        self,
        value: Any,
        field_name: str,
    ) -> dict[str, Any]:
        """Read an optional JSON object."""

        if value is None:
            return {}

        return self._mapping(
            value,
            field_name,
        )

    def _list(
        self,
        value: Any,
        field_name: str,
    ) -> list[Any]:
        """Require one JSON array."""

        if not isinstance(value, list):
            raise ValueError(
                f"Stored {field_name} must be a JSON array."
            )

        return list(value)

    def _required_text(
        self,
        payload: dict[str, Any],
        field_name: str,
    ) -> str:
        """Read one required non-empty text value."""

        value = payload.get(field_name)

        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"Stored field '{field_name}' "
                "must be non-empty text."
            )

        return value.strip()

    def _execution_mode(
        self,
        value: Any,
    ) -> ExecutionMode:
        """Parse one stored execution mode."""

        try:
            return ExecutionMode(str(value))
        except ValueError as exc:
            raise ValueError(
                f"Unsupported stored execution mode: {value}"
            ) from exc

    def _session_state(
        self,
        value: Any,
    ) -> ExecutionSessionState:
        """Parse one stored session state."""

        try:
            return ExecutionSessionState(str(value))
        except ValueError as exc:
            raise ValueError(
                f"Unsupported stored session state: {value}"
            ) from exc

    def _datetime(
        self,
        value: Any,
        field_name: str,
    ) -> datetime:
        """Parse one required timezone-aware datetime."""

        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"Stored datetime '{field_name}' is required."
            )

        try:
            parsed = datetime.fromisoformat(
                value.replace("Z", "+00:00")
            )
        except ValueError as exc:
            raise ValueError(
                f"Stored datetime '{field_name}' is invalid."
            ) from exc

        if parsed.tzinfo is None:
            raise ValueError(
                f"Stored datetime '{field_name}' "
                "must include a timezone."
            )

        return parsed

    def _optional_datetime(
        self,
        value: Any,
        field_name: str,
    ) -> datetime | None:
        """Parse one optional timezone-aware datetime."""

        if value is None:
            return None

        return self._datetime(
            value,
            field_name,
        )