"""Controlled execution orchestration for Aegis OS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .audit import (
    ExecutionAuditEvent,
    ExecutionAuditEventType,
)
from .models import ExecutionMode
from .session import (
    ExecutionSession,
    ExecutionSessionState,
)


@dataclass(slots=True)
class ExecutionOrchestrationResult:
    """Result of one controlled execution orchestration."""

    session: ExecutionSession
    events: list[ExecutionAuditEvent] = field(
        default_factory=list
    )

    @property
    def ok(self) -> bool:
        """Return whether orchestration reached the expected state."""

        if self.session.mode == ExecutionMode.PLAN:
            return (
                self.session.state
                == ExecutionSessionState.PLANNED
            )

        if self.session.mode == ExecutionMode.DRY_RUN:
            return (
                self.session.state
                == ExecutionSessionState.DRY_RUN_READY
            )

        return False

    def to_dict(self) -> dict[str, Any]:
        """Serialize the orchestration result."""

        return {
            "ok": self.ok,
            "session": self.session.to_dict(),
            "events": [
                event.to_dict()
                for event in self.events
            ],
        }


class ExecutionOrchestrator:
    """Advance execution sessions through safe runtime states."""

    def orchestrate(
        self,
        session: ExecutionSession,
    ) -> ExecutionOrchestrationResult:
        """Orchestrate one validated in-memory execution session."""

        self._validate_session(session)

        result = ExecutionOrchestrationResult(
            session=session
        )

        result.events.append(
            self._event(
                session=session,
                event_type=(
                    ExecutionAuditEventType
                    .ORCHESTRATION_STARTED
                ),
                message="Controlled orchestration started.",
                metadata={
                    "mode": session.mode.value,
                    "target_asset_id": (
                        session.target_asset_id
                    ),
                },
            )
        )

        self._transition(
            result=result,
            next_state=ExecutionSessionState.PLANNED,
            event_type=ExecutionAuditEventType.PLAN_CREATED,
            message="Execution plan state prepared.",
        )

        if session.mode == ExecutionMode.DRY_RUN:
            self._transition(
                result=result,
                next_state=(
                    ExecutionSessionState.DRY_RUN_READY
                ),
                event_type=(
                    ExecutionAuditEventType
                    .DRY_RUN_PREPARED
                ),
                message="Dry-run execution state prepared.",
            )

        return result

    def _validate_session(
        self,
        session: ExecutionSession,
    ) -> None:
        """Validate that a session may enter orchestration."""

        if session.context is None:
            raise ValueError(
                "Execution session requires a resolved context."
            )

        if not session.workspace_id.strip():
            raise ValueError(
                "Execution session requires a workspace ID."
            )

        if session.is_terminal:
            raise ValueError(
                "Terminal execution sessions cannot be orchestrated."
            )

        if (
            session.state
            != ExecutionSessionState.CONTEXT_READY
        ):
            raise ValueError(
                "Execution session must be in "
                "'context-ready' state before orchestration."
            )

        if session.mode not in {
            ExecutionMode.PLAN,
            ExecutionMode.DRY_RUN,
        }:
            raise ValueError(
                f"Unsupported execution mode: "
                f"{session.mode.value}"
            )

    def _transition(
        self,
        result: ExecutionOrchestrationResult,
        next_state: ExecutionSessionState,
        event_type: ExecutionAuditEventType,
        message: str,
    ) -> None:
        """Apply one controlled state transition and audit it."""

        session = result.session
        previous_state = session.state

        session.transition_to(next_state)

        result.events.append(
            self._event(
                session=session,
                event_type=(
                    ExecutionAuditEventType
                    .STATE_TRANSITION
                ),
                message=(
                    f"Session transitioned from "
                    f"'{previous_state.value}' to "
                    f"'{next_state.value}'."
                ),
                previous_state=previous_state.value,
                next_state=next_state.value,
                metadata={
                    "trigger_event": event_type.value,
                },
            )
        )

        result.events.append(
            self._event(
                session=session,
                event_type=event_type,
                message=message,
                previous_state=previous_state.value,
                next_state=next_state.value,
            )
        )

    def _event(
        self,
        session: ExecutionSession,
        event_type: ExecutionAuditEventType,
        message: str,
        previous_state: str = "",
        next_state: str = "",
        metadata: dict[str, Any] | None = None,
    ) -> ExecutionAuditEvent:
        """Build one audit event for a session."""

        return ExecutionAuditEvent(
            event_type=event_type,
            session_id=session.session_id,
            workspace_id=session.workspace_id,
            message=message,
            previous_state=previous_state,
            next_state=next_state,
            metadata=dict(metadata or {}),
        )