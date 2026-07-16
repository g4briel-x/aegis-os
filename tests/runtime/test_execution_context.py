"""Tests for execution context and input resolution."""

from aegis_runtime.execution import (
    ExecutionContextBuilder,
    ExecutionContract,
    ExecutionContractType,
    ExecutionInput,
    ExecutionInputResolver,
    ExecutionMode,
    ExecutionOutput,
    ExecutionSafetyLevel,
)


def build_contract() -> ExecutionContract:
    """Create a representative execution contract for tests."""

    return ExecutionContract(
        asset_id="security.review-api-security",
        contract_type=ExecutionContractType.SKILL,
        safety_level=ExecutionSafetyLevel.SAFE_DRY_RUN,
        allowed_modes=["plan", "dry-run"],
        inputs=[
            ExecutionInput(
                name="target_asset_id",
                description="Target asset identifier.",
                required=True,
            ),
            ExecutionInput(
                name="report_format",
                description="Requested report format.",
                required=False,
                default="markdown",
            ),
            ExecutionInput(
                name="scope",
                description="Security review scope.",
                required=True,
            ),
        ],
        outputs=[
            ExecutionOutput(
                name="execution_plan",
                description="Generated execution plan.",
            ),
            ExecutionOutput(
                name="dry_run_report",
                description="Generated dry-run report.",
            ),
        ],
        required_assets=["security.api-security-checklist"],
    )


def test_resolver_resolves_runtime_parameter_and_default() -> None:
    """Inputs must resolve from runtime, parameters and defaults."""

    contract = build_contract()

    result = ExecutionInputResolver().resolve(
        contract=contract,
        parameters={"scope": "public-api"},
    )

    assert result.ok
    assert result.values["target_asset_id"] == contract.asset_id
    assert result.values["scope"] == "public-api"
    assert result.values["report_format"] == "markdown"

    sources = {
        item.name: item.source
        for item in result.resolved_inputs
    }

    assert sources["target_asset_id"] == "runtime"
    assert sources["scope"] == "parameter"
    assert sources["report_format"] == "contract-default"


def test_resolver_reports_missing_required_input() -> None:
    """A missing required input must fail resolution."""

    contract = build_contract()

    result = ExecutionInputResolver().resolve(
        contract=contract,
        parameters={},
    )

    error_codes = {
        issue.code
        for issue in result.errors
    }

    assert not result.ok
    assert "missing_required_input" in error_codes
    assert "scope" not in result.values


def test_resolver_warns_about_unknown_parameter() -> None:
    """Undeclared runtime parameters must produce a warning."""

    contract = build_contract()

    result = ExecutionInputResolver().resolve(
        contract=contract,
        parameters={
            "scope": "internal-api",
            "unexpected": "value",
        },
    )

    warning_codes = {
        issue.code
        for issue in result.warnings
    }

    assert result.ok
    assert "unknown_input_parameter" in warning_codes


def test_context_builder_creates_resolved_context() -> None:
    """The context builder must create environment and artifacts."""

    contract = build_contract()

    result = ExecutionContextBuilder().build(
        contract=contract,
        mode=ExecutionMode.DRY_RUN,
        parameters={"scope": "public-api"},
    )

    context = result.context

    assert result.ok
    assert context.target_asset_id == contract.asset_id
    assert context.mode == ExecutionMode.DRY_RUN
    assert context.get_input("scope") == "public-api"
    assert context.get_input("report_format") == "markdown"
    assert context.environment.name == "local"
    assert context.environment.python_version
    assert context.environment.platform
    assert context.metadata["contract_type"] == "skill"
    assert context.metadata["safety_level"] == "safe-dry-run"

    artifact_names = {
        artifact.name
        for artifact in context.artifacts
    }

    assert artifact_names == {
        "execution_plan",
        "dry_run_report",
    }


def test_context_builder_rejects_disallowed_mode() -> None:
    """A mode excluded by the contract must fail context building."""

    contract = build_contract()
    contract.allowed_modes = ["plan"]

    result = ExecutionContextBuilder().build(
        contract=contract,
        mode=ExecutionMode.DRY_RUN,
        parameters={"scope": "public-api"},
    )

    error_codes = {
        issue.code
        for issue in result.errors
    }

    assert not result.ok
    assert "execution_mode_not_allowed" in error_codes


def test_context_serialization() -> None:
    """Execution context data must serialize to a dictionary."""

    contract = build_contract()

    result = ExecutionContextBuilder().build(
        contract=contract,
        mode=ExecutionMode.PLAN,
        parameters={"scope": "partner-api"},
    )

    payload = result.to_dict()

    assert payload["ok"] is True
    assert payload["context"]["target_asset_id"] == contract.asset_id
    assert payload["context"]["mode"] == "plan"
    assert payload["input_resolution"]["ok"] is True
    assert len(payload["context"]["artifacts"]) == 2