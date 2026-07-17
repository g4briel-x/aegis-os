"""Execution audit events for the Aegis OS runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any
from uuid import uuid4

from .session import utc_now


class ExecutionAuditEventType(StrEnum):
    """Supported execution orchestration audit events."""

    SESSION_LOADED = "session-loaded"
    ORCHESTRATION_STARTED = "orchestration-started"
    STATE_TRANSITION = "state-transition"
    PLAN_CREATED = "plan-created"
    DRY_RUN_PREPARED = "dry-run-prepared"
    SESSION_COMPLETED = "session-completed"
    SESSION_FAILED = "session-failed"
    SESSION_CANCELLED = "session-cancelled"


@dataclass(slots=True, frozen=True)
class ExecutionAuditEvent:
    """One immutable execution orchestration audit event."""

    event_type: ExecutionAuditEventType
    session_id: str
    workspace_id: str
    message: str
    previous_state: str = ""
    next_state: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    timestamp: str = field(
        default_factory=lambda: utc_now().isoformat()
    )
    actor: str = "aegis-runtime"

    def __post_init__(self) -> None:
        """Validate required audit event fields."""

        if not self.session_id.strip():
            raise ValueError(
                "Execution audit event requires a session ID."
            )

        if not self.workspace_id.strip():
            raise ValueError(
                "Execution audit event requires a workspace ID."
            )

        if not self.message.strip():
            raise ValueError(
                "Execution audit event requires a message."
            )

    def to_dict(self) -> dict[str, Any]:
        """Serialize the execution audit event."""

        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "session_id": self.session_id,
            "workspace_id": self.workspace_id,
            "timestamp": self.timestamp,
            "actor": self.actor,
            "message": self.message,
            "previous_state": self.previous_state or None,
            "next_state": self.next_state or None,
            "metadata": dict(self.metadata),
        }