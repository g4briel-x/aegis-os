"""Execution planning services for the Aegis runtime."""

from __future__ import annotations

from aegis_runtime.asset_resolver import AssetResolver

from .models import (
    ExecutionMode,
    ExecutionPlan,
    ExecutionStatus,
    ExecutionStep,
)


class ExecutionPlanner:
    """Builds execution plans for Aegis assets."""

    def __init__(self, resolver: AssetResolver) -> None:
        self.resolver = resolver

    def create_plan(
        self,
        target_asset_id: str,
        *,
        mode: ExecutionMode = ExecutionMode.PLAN,
    ) -> ExecutionPlan:
        """Create an execution plan for one registered asset."""

        asset = self.resolver.require(target_asset_id)

        plan = ExecutionPlan(
            target_asset_id=asset.id,
            mode=mode,
            metadata={
                "target_name": asset.name,
                "target_type": asset.type,
                "target_domain": asset.domain,
                "target_path": asset.path,
            },
        )

        plan.steps.append(
            ExecutionStep(
                index=1,
                title="Resolve target asset",
                action="resolve_asset",
                asset_id=asset.id,
                asset_type=asset.type,
                status=ExecutionStatus.READY,
                metadata={
                    "path": asset.path,
                    "domain": asset.domain,
                },
            )
        )

        plan.steps.append(
            ExecutionStep(
                index=2,
                title="Load related assets",
                action="load_related_assets",
                asset_id=asset.id,
                asset_type=asset.type,
                status=ExecutionStatus.READY,
                metadata={
                    "related_assets": list(asset.related_assets),
                    "related_asset_count": len(asset.related_assets),
                },
            )
        )

        plan.steps.append(
            ExecutionStep(
                index=3,
                title="Validate execution readiness",
                action="validate_execution_readiness",
                asset_id=asset.id,
                asset_type=asset.type,
                status=ExecutionStatus.READY,
                metadata={
                    "mode": mode.value,
                    "dry_run_only": mode is ExecutionMode.DRY_RUN,
                },
            )
        )

        plan.steps.append(
            ExecutionStep(
                index=4,
                title="Prepare execution report",
                action="prepare_execution_report",
                asset_id=asset.id,
                asset_type=asset.type,
                status=ExecutionStatus.READY,
                metadata={
                    "report_type": "execution_plan",
                },
            )
        )

        return plan