"""Terminal execution lifecycle management for Aegis OS."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
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


class ExecutionLifecycleAction(StrEnum):
    """Supported terminal lifecycle actions."""

    COMPLETE = "complete"
    FAIL = "fail"
    CANCEL = "cancel"


@dataclass(slots=True)
class ExecutionLifecycleResult:
    """Result of one controlled terminal lifecycle transition."""

    action: ExecutionLifecycleAction
    terminal_state: ExecutionSessionState
    session: ExecutionSession
    reason: str
    actor: str
    events: list[ExecutionAuditEvent] = field(
        default_factory=list
    )

    @property
    def ok(self) -> bool:
        """Return whether the expected terminal state was reached."""

        return (
            self.session.state == self.terminal_state
            and self.session.is_terminal
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize the lifecycle result."""

        return {
            "ok": self.ok,
            "action": self.action.value,
            "terminal_state": self.terminal_state.value,
            "reason": self.reason,
            "actor": self.actor,
            "session": self.session.to_dict(),
            "events": [
                event.to_dict()
                for event in self.events
            ],
        }


class ExecutionLifecycleManager:
    """Apply controlled terminal transitions to sessions."""

    def complete(
        self,
        session: ExecutionSession,
        reason: str = "",
        actor: str = "aegis-runtime",
    ) -> ExecutionLifecycleResult:
        """Complete one successfully prepared execution session."""

        return self.transition(
            session=session,
            action=ExecutionLifecycleAction.COMPLETE,
            reason=reason,
            actor=actor,
        )

    def fail(
        self,
        session: ExecutionSession,
        reason: str,
        actor: str = "aegis-runtime",
    ) -> ExecutionLifecycleResult:
        """Mark one active execution session as failed."""

        return self.transition(
            session=session,
            action=ExecutionLifecycleAction.FAIL,
            reason=reason,
            actor=actor,
        )

    def cancel(
        self,
        session: ExecutionSession,
        reason: str,
        actor: str = "aegis-runtime",
    ) -> ExecutionLifecycleResult:
        """Cancel one active execution session."""

        return self.transition(
            session=session,
            action=ExecutionLifecycleAction.CANCEL,
            reason=reason,
            actor=actor,
        )

    def transition(
        self,
        session: ExecutionSession,
        action: ExecutionLifecycleAction,
        reason: str = "",
        actor: str = "aegis-runtime",
    ) -> ExecutionLifecycleResult:
        """Apply one validated terminal lifecycle transition."""

        normalized_actor = actor.strip()

        if not normalized_actor:
            raise ValueError(
                "Execution lifecycle actor cannot be empty."
            )

        normalized_reason = self._normalize_reason(
            action=action,
            reason=reason,
        )

        self._validate_session(
            session=session,
            action=action,
        )

        terminal_state = self._terminal_state(action)
        terminal_event_type = self._terminal_event_type(
            action
        )
        previous_state = session.state

        session.transition_to(terminal_state)

        session.audit_metadata["lifecycle"] = {
            "action": action.value,
            "previous_state": previous_state.value,
            "terminal_state": terminal_state.value,
            "reason": normalized_reason,
            "actor": normalized_actor,
            "completed_at": (
                session.completed_at.isoformat()
                if session.completed_at
                else None
            ),
        }

        result = ExecutionLifecycleResult(
            action=action,
            terminal_state=terminal_state,
            session=session,
            reason=normalized_reason,
            actor=normalized_actor,
        )

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
                    f"'{terminal_state.value}'."
                ),
                actor=normalized_actor,
                previous_state=previous_state.value,
                next_state=terminal_state.value,
                metadata={
                    "trigger_event": (
                        terminal_event_type.value
                    ),
                    "reason": normalized_reason,
                },
            )
        )

        result.events.append(
            self._event(
                session=session,
                event_type=terminal_event_type,
                message=self._terminal_message(action),
                actor=normalized_actor,
                previous_state=previous_state.value,
                next_state=terminal_state.value,
                metadata={
                    "action": action.value,
                    "reason": normalized_reason,
                },
            )
        )

        return result

    def _validate_session(
        self,
        session: ExecutionSession,
        action: ExecutionLifecycleAction,
    ) -> None:
        """Validate that a session may become terminal."""

        if session.context is None:
            raise ValueError(
                "Execution lifecycle requires "
                "a resolved session context."
            )

        if not session.workspace_id.strip():
            raise ValueError(
                "Execution lifecycle requires a workspace ID."
            )

        if session.is_terminal:
            raise ValueError(
                "A terminal execution session cannot "
                "transition again."
            )

        if action == ExecutionLifecycleAction.COMPLETE:
            expected_state = self._completion_source_state(
                session
            )

            if session.state != expected_state:
                raise ValueError(
                    "Execution session must be in "
                    f"'{expected_state.value}' state "
                    "before completion."
                )

            return

        allowed_states = {
            ExecutionSessionState.CONTEXT_READY,
            ExecutionSessionState.PLANNED,
            ExecutionSessionState.DRY_RUN_READY,
        }

        if session.state not in allowed_states:
            raise ValueError(
                "Execution session state does not allow "
                f"the '{action.value}' lifecycle action."
            )

    def _completion_source_state(
        self,
        session: ExecutionSession,
    ) -> ExecutionSessionState:
        """Return the required source state for completion."""

        if session.mode == ExecutionMode.PLAN:
            return ExecutionSessionState.PLANNED

        if session.mode == ExecutionMode.DRY_RUN:
            return ExecutionSessionState.DRY_RUN_READY

        raise ValueError(
            "Unsupported execution mode for completion: "
            f"{session.mode.value}"
        )

    def _normalize_reason(
        self,
        action: ExecutionLifecycleAction,
        reason: str,
    ) -> str:
        """Validate and normalize the lifecycle reason."""

        normalized = reason.strip()

        if action == ExecutionLifecycleAction.COMPLETE:
            return (
                normalized
                or "Execution lifecycle completed successfully."
            )

        if not normalized:
            raise ValueError(
                f"Lifecycle action '{action.value}' "
                "requires a reason."
            )

        return normalized

    def _terminal_state(
        self,
        action: ExecutionLifecycleAction,
    ) -> ExecutionSessionState:
        """Map one lifecycle action to its terminal state."""

        mapping = {
            ExecutionLifecycleAction.COMPLETE: (
                ExecutionSessionState.COMPLETED
            ),
            ExecutionLifecycleAction.FAIL: (
                ExecutionSessionState.FAILED
            ),
            ExecutionLifecycleAction.CANCEL: (
                ExecutionSessionState.CANCELLED
            ),
        }

        return mapping[action]

    def _terminal_event_type(
        self,
        action: ExecutionLifecycleAction,
    ) -> ExecutionAuditEventType:
        """Map one lifecycle action to its audit event."""

        mapping = {
            ExecutionLifecycleAction.COMPLETE: (
                ExecutionAuditEventType.SESSION_COMPLETED
            ),
            ExecutionLifecycleAction.FAIL: (
                ExecutionAuditEventType.SESSION_FAILED
            ),
            ExecutionLifecycleAction.CANCEL: (
                ExecutionAuditEventType.SESSION_CANCELLED
            ),
        }

        return mapping[action]

    def _terminal_message(
        self,
        action: ExecutionLifecycleAction,
    ) -> str:
        """Return the terminal event message."""

        mapping = {
            ExecutionLifecycleAction.COMPLETE: (
                "Execution session completed."
            ),
            ExecutionLifecycleAction.FAIL: (
                "Execution session failed."
            ),
            ExecutionLifecycleAction.CANCEL: (
                "Execution session cancelled."
            ),
        }

        return mapping[action]

    def _event(
        self,
        session: ExecutionSession,
        event_type: ExecutionAuditEventType,
        message: str,
        actor: str,
        previous_state: str,
        next_state: str,
        metadata: dict[str, Any] | None = None,
    ) -> ExecutionAuditEvent:
        """Build one immutable lifecycle audit event."""

        return ExecutionAuditEvent(
            event_type=event_type,
            session_id=session.session_id,
            workspace_id=session.workspace_id,
            message=message,
            actor=actor,
            previous_state=previous_state,
            next_state=next_state,
            metadata=dict(metadata or {}),
        )