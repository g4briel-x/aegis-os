"""Tests for Aegis execution contracts."""

from pathlib import Path

from aegis_runtime.execution import (
    ExecutionContract,
    ExecutionContractBuilder,
    ExecutionContractType,
    ExecutionContractValidator,
    ExecutionSafetyLevel,
)
from aegis_runtime.models import Asset


def test_builder_creates_skill_contract() -> None:
    """A skill asset must produce a skill execution contract."""

    asset = Asset(
        id="security.review-api-security",
        name="Review API Security",
        type="skill",
        domain="security",
        path="skills/security/review-api-security",
        tags=["security", "api"],
        related_assets=["engineering.api-contract-template"],
        source_file=Path("registry/skills/skills.registry.yaml"),
    )

    contract = ExecutionContractBuilder().build_from_asset(asset)

    assert contract.asset_id == asset.id
    assert contract.contract_type == ExecutionContractType.SKILL
    assert contract.safety_level == ExecutionSafetyLevel.SAFE_DRY_RUN
    assert contract.allowed_modes == ["plan", "dry-run"]
    assert contract.required_assets == asset.related_assets
    assert contract.inputs[0].name == "target_asset_id"
    assert contract.outputs[0].name == "execution_plan"


def test_builder_creates_playbook_contract() -> None:
    """A playbook asset must produce a playbook execution contract."""

    asset = Asset(
        id="security.respond-to-security-incident",
        name="Respond to Security Incident",
        type="playbook",
        domain="security",
        path="playbooks/security/respond-to-security-incident",
    )

    contract = ExecutionContractBuilder().build_from_asset(asset)

    assert contract.contract_type == ExecutionContractType.PLAYBOOK
    assert contract.is_safe_for_dry_run()
    assert "delete_file" in contract.forbidden_actions
    assert "call_external_api" in contract.forbidden_actions


def test_validator_accepts_generated_contract() -> None:
    """A generated conservative contract must pass validation."""

    asset = Asset(
        id="engineering.create-api-contract",
        name="Create API Contract",
        type="playbook",
        domain="engineering",
        path="playbooks/engineering/create-api-contract",
    )

    contract = ExecutionContractBuilder().build_from_asset(asset)
    result = ExecutionContractValidator().validate(contract)

    assert result.ok
    assert result.errors == []


def test_validator_rejects_blocked_contract() -> None:
    """A blocked execution contract must fail validation."""

    contract = ExecutionContract(
        asset_id="security.blocked-operation",
        contract_type=ExecutionContractType.PLAYBOOK,
        safety_level=ExecutionSafetyLevel.BLOCKED,
        allowed_modes=["plan", "dry-run"],
        forbidden_actions=["delete_file"],
    )

    result = ExecutionContractValidator().validate(contract)
    error_codes = {issue.code for issue in result.errors}

    assert not result.ok
    assert "blocked_contract" in error_codes


def test_validator_reports_missing_dry_run_and_forbidden_actions() -> None:
    """Incomplete safety declarations must produce warnings."""

    contract = ExecutionContract(
        asset_id="skills.incomplete-contract",
        contract_type=ExecutionContractType.SKILL,
        safety_level=ExecutionSafetyLevel.REQUIRES_APPROVAL,
        allowed_modes=["plan"],
        forbidden_actions=[],
    )

    result = ExecutionContractValidator().validate(contract)
    warning_codes = {issue.code for issue in result.warnings}

    assert result.ok
    assert "dry_run_not_declared" in warning_codes
    assert "no_forbidden_actions" in warning_codes