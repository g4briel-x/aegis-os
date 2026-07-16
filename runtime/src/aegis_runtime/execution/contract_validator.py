"""Execution contract validation services."""

from __future__ import annotations

from .contracts import (
    ContractValidationResult,
    ExecutionContract,
    ExecutionContractType,
    ExecutionSafetyLevel,
)


class ExecutionContractValidator:
    """Validates Aegis execution contracts before execution."""

    VALID_MODES = {"plan", "dry-run"}

    FORBIDDEN_ACTIONS = {
        "delete_file",
        "delete_directory",
        "write_file",
        "modify_file",
        "send_email",
        "call_external_api",
        "execute_shell_command",
        "run_untrusted_code",
    }

    def validate(self, contract: ExecutionContract) -> ContractValidationResult:
        """Validate one execution contract."""

        result = ContractValidationResult(contract=contract)

        if not contract.asset_id.strip():
            result.add_issue(
                "error",
                "missing_asset_id",
                "Execution contract must declare an asset_id.",
            )

        if contract.contract_type not in {
            ExecutionContractType.PLAYBOOK,
            ExecutionContractType.SKILL,
        }:
            result.add_issue(
                "error",
                "invalid_contract_type",
                "Execution contract type must be playbook or skill.",
            )

        if contract.safety_level == ExecutionSafetyLevel.BLOCKED:
            result.add_issue(
                "error",
                "blocked_contract",
                "Execution contract is explicitly blocked.",
            )

        for mode in contract.allowed_modes:
            if mode not in self.VALID_MODES:
                result.add_issue(
                    "error",
                    "invalid_execution_mode",
                    f"Unsupported execution mode: {mode}",
                )

        if "dry-run" not in contract.allowed_modes:
            result.add_issue(
                "warning",
                "dry_run_not_declared",
                "Execution contract does not explicitly allow dry-run mode.",
            )

        for action in contract.forbidden_actions:
            if action not in self.FORBIDDEN_ACTIONS:
                result.add_issue(
                    "warning",
                    "unknown_forbidden_action",
                    f"Forbidden action is not part of the known action catalog: {action}",
                )

        if not contract.forbidden_actions:
            result.add_issue(
                "warning",
                "no_forbidden_actions",
                "Execution contract does not declare forbidden actions.",
            )

        return result