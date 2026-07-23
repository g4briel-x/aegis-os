"""Tests for execution sessions and logical workspaces."""

from uuid import UUID
from pathlib import Path
import json
import pytest

_AUDIT_HMAC_SECRET = (
    "0123456789abcdef"
    "0123456789abcdef"
)

_AUDIT_HMAC_KEY_ID = "test-workspace-store-key-v1"

from aegis_runtime.execution.workspace_store import (
    ExecutionWorkspaceStore,
)

from aegis_runtime.execution import (
    ExecutionAuditAuthenticator,
    ExecutionAuditProtection,
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



def test_workspace_store_persists_session_manifests(
    tmp_path: Path,
) -> None:
    """A successful session must be persisted inside its workspace."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.DRY_RUN,
        parameters={
            "scope": "public-api",
        },
    )

    persisted = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    ).persist(result)

    assert persisted.workspace_path.is_dir()
    assert persisted.session_manifest.is_file()
    assert persisted.context_manifest.is_file()
    assert persisted.inputs_manifest.is_file()
    assert persisted.audit_manifest.is_file()

    assert (
        persisted.workspace_path
        == (
            tmp_path
            / result.workspace.logical_path
        ).resolve()
    )

    session_payload = json.loads(
        persisted.session_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert session_payload["build"]["ok"] is True
    assert (
        session_payload["session"]["session_id"]
        == result.session.session_id
    )
    assert (
        session_payload["workspace"]["workspace_id"]
        == result.workspace.workspace_id
    )

    context_payload = json.loads(
        persisted.context_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert (
        context_payload["target_asset_id"]
        == "security.review-api-security"
    )
    assert context_payload["mode"] == "dry-run"

    inputs_payload = json.loads(
        persisted.inputs_manifest.read_text(
            encoding="utf-8"
        )
    )

    resolved_values = {
        item["name"]: item["value"]
        for item in inputs_payload["resolved_inputs"]
    }

    assert resolved_values["scope"] == "public-api"
    assert (
        resolved_values["target_asset_id"]
        == "security.review-api-security"
    )

    audit_payload = json.loads(
        persisted.audit_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert (
        audit_payload["session_id"]
        == result.session.session_id
    )
    assert audit_payload["state"] == "context-ready"

def test_workspace_store_authenticates_initial_audit_manifest(
    tmp_path: Path,
) -> None:
    """A configured HMAC key must authenticate the initial journal."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.DRY_RUN,
        parameters={
            "scope": "authenticated-api",
        },
    )

    authenticator = ExecutionAuditAuthenticator(
        _AUDIT_HMAC_SECRET,
        key_id=_AUDIT_HMAC_KEY_ID,
    )

    protection = ExecutionAuditProtection(
        authenticator=authenticator,
    )

    persisted = ExecutionWorkspaceStore(
        repo_root=tmp_path,
        audit_protection=protection,
    ).persist(
        result
    )

    serialized_audit = (
        persisted.audit_manifest.read_text(
            encoding="utf-8"
        )
    )

    audit_payload = json.loads(
        serialized_audit
    )

    verification = protection.verify(
        audit_payload
    )

    assert verification.ok
    assert verification.authenticated
    assert verification.authentication is not None
    assert (
        verification.authentication.key_id
        == _AUDIT_HMAC_KEY_ID
    )

    assert "integrity" in audit_payload
    assert "authentication" in audit_payload

    assert (
        audit_payload["authentication"]["key_id"]
        == _AUDIT_HMAC_KEY_ID
    )

    assert (
        audit_payload["authentication"]["journal_hash"]
        == audit_payload["integrity"]["journal_hash"]
    )

    assert _AUDIT_HMAC_SECRET not in serialized_audit

def test_workspace_store_rejects_duplicate_persistence(
    tmp_path: Path,
) -> None:
    """An existing session workspace must never be overwritten."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.PLAN,
        parameters={
            "scope": "partner-api",
        },
    )

    store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    store.persist(result)

    with pytest.raises(
        FileExistsError,
        match="already exists",
    ):
        store.persist(result)


def test_workspace_store_rejects_failed_session(
    tmp_path: Path,
) -> None:
    """A failed session must not create a physical workspace."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.DRY_RUN,
        parameters={},
    )

    store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    with pytest.raises(
        ValueError,
        match="successful execution session",
    ):
        store.persist(result)

    assert not (
        tmp_path
        / result.workspace.logical_path
    ).exists()

def test_workspace_store_loads_session_by_workspace_id(
    tmp_path: Path,
) -> None:
    """A persisted session can be loaded by workspace ID."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.DRY_RUN,
        parameters={
            "scope": "public-api",
        },
    )

    store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    persisted = store.persist(result)

    record = store.load(
        result.workspace.workspace_id
    )

    assert record.workspace_path == persisted.workspace_path
    assert record.session_manifest == persisted.session_manifest
    assert record.workspace_id == result.workspace.workspace_id
    assert record.session_id == result.session.session_id
    assert (
        record.payload["session"]["target_asset_id"]
        == "security.review-api-security"
    )

def test_workspace_store_loads_session_by_session_id(
    tmp_path: Path,
) -> None:
    """A persisted session can be located by session ID."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.PLAN,
        parameters={
            "scope": "partner-api",
        },
    )

    store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    store.persist(result)

    record = store.load(
        result.session.session_id
    )

    assert record.session_id == result.session.session_id
    assert record.workspace_id == result.workspace.workspace_id
    assert record.payload["session"]["mode"] == "plan"

def test_workspace_store_rejects_unsafe_identifier(
    tmp_path: Path,
) -> None:
    """Session lookup must reject path traversal identifiers."""

    store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    with pytest.raises(
        ValueError,
        match="path separators",
    ):
        store.load("../outside")

def test_workspace_store_reports_missing_session(
    tmp_path: Path,
) -> None:
    """An unknown session identifier must return a clear error."""

    store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    with pytest.raises(
        FileNotFoundError,
        match="was not found",
    ):
        store.load("missing-session-id")