"""Tests for execution sessions and logical workspaces."""

from uuid import UUID

import pytest

from aegis_runtime.execution import (
    ExecutionContext,
    ExecutionContract,
    ExecutionContractType,
    ExecutionInput,
    ExecutionMode,
    ExecutionOutput,
    ExecutionSafetyLevel,
    ExecutionSession,
    ExecutionSessionBuilder,
    ExecutionSessionState,
    ExecutionWorkspace,
    ExecutionWorkspaceState,
    WorkspaceLocation,
)


def build_contract() -> ExecutionContract:
    """Create a representative contract for session tests."""

    return ExecutionContract(
        asset_id="security.review-api-security",
        contract_type=ExecutionContractType.SKILL,
        safety_level=ExecutionSafetyLevel.SAFE_DRY_RUN,
        allowed_modes=["plan", "dry-run"],
        inputs=[
            ExecutionInput(
                name="target_asset_id",
                required=True,
            ),
            ExecutionInput(
                name="scope",
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
        required_assets=[
            "security.api-security-checklist",
        ],
    )


def test_session_has_identifier_and_timestamps() -> None:
    """A session must have a valid identifier and UTC timestamps."""

    session = ExecutionSession(
        target_asset_id="security.review-api-security",
        mode=ExecutionMode.DRY_RUN,
    )

    assert UUID(session.session_id)
    assert session.state == ExecutionSessionState.CREATED
    assert session.created_at.tzinfo is not None
    assert session.updated_at.tzinfo is not None
    assert session.started_at is None
    assert session.completed_at is None
    assert not session.is_terminal


def test_session_attaches_matching_context() -> None:
    """A matching context must move the session to context-ready."""

    session = ExecutionSession(
        target_asset_id="security.review-api-security",
        mode=ExecutionMode.DRY_RUN,
    )

    context = ExecutionContext(
        target_asset_id="security.review-api-security",
        mode=ExecutionMode.DRY_RUN,
    )

    session.attach_context(context)

    assert session.context is context
    assert session.state == ExecutionSessionState.CONTEXT_READY


def test_session_rejects_mismatched_context() -> None:
    """A session must reject a context for another asset."""

    session = ExecutionSession(
        target_asset_id="security.review-api-security",
        mode=ExecutionMode.DRY_RUN,
    )

    context = ExecutionContext(
        target_asset_id="engineering.create-api-contract",
        mode=ExecutionMode.DRY_RUN,
    )

    with pytest.raises(
        ValueError,
        match="target does not match",
    ):
        session.attach_context(context)


def test_terminal_session_cannot_transition() -> None:
    """A completed session must reject later transitions."""

    session = ExecutionSession(
        target_asset_id="security.review-api-security",
        mode=ExecutionMode.PLAN,
    )

    session.transition_to(ExecutionSessionState.COMPLETED)

    assert session.is_terminal
    assert session.started_at is not None
    assert session.completed_at is not None

    with pytest.raises(
        ValueError,
        match="terminal execution session",
    ):
        session.transition_to(
            ExecutionSessionState.FAILED
        )


def test_workspace_rejects_unsafe_paths() -> None:
    """Workspace locations must remain relative and isolated."""

    workspace = ExecutionWorkspace(
        session_id="session-001",
    )

    with pytest.raises(
        ValueError,
        match="relative path",
    ):
        workspace.add_location(
            WorkspaceLocation(
                name="absolute",
                relative_path="/tmp/output",
            )
        )

    with pytest.raises(
        ValueError,
        match="traverse parent directories",
    ):
        workspace.add_location(
            WorkspaceLocation(
                name="traversal",
                relative_path="../outside",
            )
        )

    with pytest.raises(
        ValueError,
        match="drive-qualified",
    ):
        workspace.add_location(
            WorkspaceLocation(
                name="windows-drive",
                relative_path="C:/outside",
            )
        )


def test_workspace_rejects_duplicate_locations() -> None:
    """Workspace location names and paths must be unique."""

    workspace = ExecutionWorkspace(
        session_id="session-002",
    )

    workspace.add_location(
        WorkspaceLocation(
            name="artifacts",
            relative_path="artifacts",
        )
    )

    with pytest.raises(
        ValueError,
        match="already declared",
    ):
        workspace.add_location(
            WorkspaceLocation(
                name="artifacts",
                relative_path="other-artifacts",
            )
        )

    with pytest.raises(
        ValueError,
        match="already reserved",
    ):
        workspace.add_location(
            WorkspaceLocation(
                name="duplicate-path",
                relative_path="artifacts",
            )
        )


def test_session_builder_creates_ready_session() -> None:
    """The builder must create a resolved session and workspace."""

    contract = build_contract()

    result = ExecutionSessionBuilder().build(
        contract=contract,
        mode=ExecutionMode.DRY_RUN,
        parameters={
            "scope": "public-api",
        },
    )

    assert result.ok
    assert result.session.context is not None
    assert (
        result.session.state
        == ExecutionSessionState.CONTEXT_READY
    )
    assert (
        result.workspace.state
        == ExecutionWorkspaceState.READY
    )
    assert (
        result.session.workspace_id
        == result.workspace.workspace_id
    )

    location_names = {
        location.name
        for location in result.workspace.locations
    }

    assert {
        "resolved-inputs",
        "execution-context",
        "artifacts",
        "session-audit",
        "artifact:execution_plan",
        "artifact:dry_run_report",
    }.issubset(location_names)

    assert result.session.audit_metadata[
        "safety_level"
    ] == "safe-dry-run"


def test_session_builder_fails_on_missing_input() -> None:
    """A missing required input must fail the session build."""

    contract = build_contract()

    result = ExecutionSessionBuilder().build(
        contract=contract,
        mode=ExecutionMode.DRY_RUN,
        parameters={},
    )

    error_codes = {
        issue.code
        for issue in result.errors
    }

    assert not result.ok
    assert "missing_required_input" in error_codes
    assert (
        result.session.state
        == ExecutionSessionState.FAILED
    )
    assert result.session.context is None
    assert (
        result.workspace.state
        == ExecutionWorkspaceState.DECLARED
    )


def test_session_build_serialization() -> None:
    """Session build results must serialize completely."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.PLAN,
        parameters={
            "scope": "partner-api",
        },
    )

    payload = result.to_dict()

    assert payload["ok"] is True
    assert payload["session"]["mode"] == "plan"
    assert payload["session"]["state"] == "context-ready"
    assert payload["workspace"]["state"] == "ready"
    assert payload["workspace"]["logical_path"].startswith(
        ".aegis/workspaces/"
    )
    assert payload["context_build"]["ok"] is True