"""Execution contract builder services."""

from __future__ import annotations

from aegis_runtime.models import Asset

from .contracts import (
    ExecutionContract,
    ExecutionContractType,
    ExecutionInput,
    ExecutionOutput,
    ExecutionSafetyLevel,
)


class ExecutionContractBuilder:
    """Builds execution contracts from registered Aegis assets."""

    def build_from_asset(self, asset: Asset) -> ExecutionContract:
        """Build a conservative execution contract for an asset."""

        contract_type = self._resolve_contract_type(asset)

        contract = ExecutionContract(
            asset_id=asset.id,
            contract_type=contract_type,
            safety_level=ExecutionSafetyLevel.SAFE_DRY_RUN,
            description=(
                f"Safe dry-run execution contract generated for {asset.id}."
            ),
            allowed_modes=["plan", "dry-run"],
            required_assets=list(asset.related_assets),
            forbidden_actions=[
                "delete_file",
                "delete_directory",
                "write_file",
                "modify_file",
                "send_email",
                "call_external_api",
                "execute_shell_command",
                "run_untrusted_code",
            ],
            metadata={
                "name": asset.name,
                "type": asset.type,
                "domain": asset.domain,
                "path": asset.path,
                "tags": list(asset.tags),
                "source_file": str(asset.source_file) if asset.source_file else None,
            },
        )

        contract.inputs.append(
            ExecutionInput(
                name="target_asset_id",
                description="Identifier of the asset to plan or dry-run.",
                required=True,
                default=asset.id,
            )
        )

        contract.outputs.append(
            ExecutionOutput(
                name="execution_plan",
                description="Structured execution plan generated for the asset.",
            )
        )

        contract.outputs.append(
            ExecutionOutput(
                name="dry_run_report",
                description="Safe dry-run report showing what would be executed.",
            )
        )

        return contract

    def _resolve_contract_type(self, asset: Asset) -> ExecutionContractType:
        asset_type = asset.type.strip().lower()

        if asset_type == "skill":
            return ExecutionContractType.SKILL

        return ExecutionContractType.PLAYBOOK