"""Execution session models for the Aegis OS runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import uuid4

from .context import ExecutionContext
from .models import ExecutionMode


def utc_now() -> datetime:
    """Return the current timezone-aware UTC datetime."""

    return datetime.now(timezone.utc)


class ExecutionSessionState(StrEnum):
    """Supported execution session lifecycle states."""

    CREATED = "created"
    CONTEXT_READY = "context-ready"
    PLANNED = "planned"
    DRY_RUN_READY = "dry-run-ready"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass(slots=True)
class ExecutionSession:
    """One identifiable Aegis OS execution session."""

    target_asset_id: str
    mode: ExecutionMode
    session_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    state: ExecutionSessionState = (
        ExecutionSessionState.CREATED
    )
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)
    started_at: datetime | None = None
    completed_at: datetime | None = None
    context: ExecutionContext | None = None
    workspace_id: str = ""
    audit_metadata: dict[str, Any] = field(
        default_factory=dict
    )
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    @property
    def is_terminal(self) -> bool:
        """Return whether the session reached a terminal state."""

        return self.state in {
            ExecutionSessionState.COMPLETED,
            ExecutionSessionState.FAILED,
            ExecutionSessionState.CANCELLED,
        }

    def attach_context(
        self,
        context: ExecutionContext,
    ) -> None:
        """Attach a validated context to the session."""

        if context.target_asset_id != self.target_asset_id:
            raise ValueError(
                "Execution context target does not match "
                "the session target asset."
            )

        if context.mode != self.mode:
            raise ValueError(
                "Execution context mode does not match "
                "the session execution mode."
            )

        self.context = context
        self.transition_to(
            ExecutionSessionState.CONTEXT_READY
        )

    def transition_to(
        self,
        state: ExecutionSessionState,
    ) -> None:
        """Update the session state and timestamps."""

        if self.is_terminal:
            raise ValueError(
                "A terminal execution session cannot transition "
                "to another state."
            )

        now = utc_now()

        if self.started_at is None and state not in {
            ExecutionSessionState.CREATED,
            ExecutionSessionState.CONTEXT_READY,
        }:
            self.started_at = now

        if state in {
            ExecutionSessionState.COMPLETED,
            ExecutionSessionState.FAILED,
            ExecutionSessionState.CANCELLED,
        }:
            self.completed_at = now

        self.state = state
        self.updated_at = now

    def to_dict(self) -> dict[str, Any]:
        """Serialize the execution session."""

        return {
            "session_id": self.session_id,
            "target_asset_id": self.target_asset_id,
            "mode": self.mode.value,
            "state": self.state.value,
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
            "context": (
                self.context.to_dict()
                if self.context
                else None
            ),
            "workspace_id": self.workspace_id,
            "audit_metadata": dict(
                self.audit_metadata
            ),
            "metadata": dict(self.metadata),
        }