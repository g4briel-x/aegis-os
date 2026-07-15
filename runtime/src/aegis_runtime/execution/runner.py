"""Execution runner services for the Aegis runtime."""

from __future__ import annotations

from .models import (
    ExecutionMode,
    ExecutionReport,
    ExecutionStatus,
)
from .planner import ExecutionPlanner


class ExecutionRunner:
    """Runs safe execution modes for Aegis assets."""

    def __init__(self, planner: ExecutionPlanner) -> None:
        self.planner = planner

    def dry_run(self, target_asset_id: str) -> ExecutionReport:
        """Create a dry-run execution report without executing actions."""

        plan = self.planner.create_plan(
            target_asset_id,
            mode=ExecutionMode.DRY_RUN,
        )

        return ExecutionReport(
            plan=plan,
            status=ExecutionStatus.READY,
            message=(
                "Dry-run completed. No actions were executed. "
                "The target asset is ready for planned execution."
            ),
        )