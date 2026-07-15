"""Execution data models for the Aegis runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class ExecutionMode(StrEnum):
    """Supported execution modes."""

    PLAN = "plan"
    DRY_RUN = "dry-run"


class ExecutionStatus(StrEnum):
    """Execution status values."""

    PLANNED = "planned"
    READY = "ready"
    SKIPPED = "skipped"
    FAILED = "failed"


@dataclass(slots=True)
class ExecutionStep:
    """One step in an Aegis execution plan."""

    index: int
    title: str
    action: str
    asset_id: str | None = None
    asset_type: str | None = None
    status: ExecutionStatus = ExecutionStatus.PLANNED
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "title": self.title,
            "action": self.action,
            "asset_id": self.asset_id,
            "asset_type": self.asset_type,
            "status": self.status.value,
            "metadata": dict(self.metadata),
        }


@dataclass(slots=True)
class ExecutionPlan:
    """A planned execution for one Aegis asset."""

    target_asset_id: str
    mode: ExecutionMode
    steps: list[ExecutionStep] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_asset_id": self.target_asset_id,
            "mode": self.mode.value,
            "steps": [step.to_dict() for step in self.steps],
            "metadata": dict(self.metadata),
        }


@dataclass(slots=True)
class ExecutionReport:
    """Result of planning or dry-running an execution."""

    plan: ExecutionPlan
    status: ExecutionStatus
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.value,
            "message": self.message,
            "plan": self.plan.to_dict(),
        }