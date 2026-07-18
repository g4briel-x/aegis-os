"""Execution audit verification reporting for Aegis OS."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .audit_history import ExecutionAuditHistoryReader
from .audit_integrity import (
    ExecutionAuditIntegrityVerification,
)
from .models import ExecutionMode
from .session import ExecutionSessionState
from .workspace_store import StoredExecutionSession


@dataclass(slots=True, frozen=True)
class ExecutionAuditVerificationReport:
    """Successful verification report for one audit journal."""

    session_id: str
    workspace_id: str
    target_asset_id: str
    mode: ExecutionMode
    state: ExecutionSessionState
    audit_manifest: Path
    integrity: ExecutionAuditIntegrityVerification

    @property
    def ok(self) -> bool:
        """Return whether the audit journal is valid."""

        return self.integrity.ok

    @property
    def event_count(self) -> int:
        """Return the verified audit event count."""

        return self.integrity.event_count

    def to_dict(self) -> dict[str, Any]:
        """Serialize the complete verification report."""

        return {
            "ok": self.ok,
            "session_id": self.session_id,
            "workspace_id": self.workspace_id,
            "target_asset_id": self.target_asset_id,
            "mode": self.mode.value,
            "state": self.state.value,
            "audit_manifest": str(self.audit_manifest),
            "event_count": self.event_count,
            "integrity": self.integrity.to_dict(),
        }


class ExecutionAuditVerifier:
    """Verify one persistent execution audit journal."""

    def __init__(self) -> None:
        """Initialize the strict persistent history reader."""

        self._history_reader = ExecutionAuditHistoryReader()

    def verify(
        self,
        record: StoredExecutionSession,
    ) -> ExecutionAuditVerificationReport:
        """Verify and describe one stored audit journal."""

        history = self._history_reader.load(
            record
        )

        return ExecutionAuditVerificationReport(
            session_id=history.session_id,
            workspace_id=history.workspace_id,
            target_asset_id=history.target_asset_id,
            mode=history.mode,
            state=history.state,
            audit_manifest=history.audit_manifest,
            integrity=history.integrity,
        )