"""Tests for persisted execution session rehydration."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import pytest

from aegis_runtime.execution import (
    ExecutionContract,
    ExecutionContractType,
    ExecutionInput,
    ExecutionMode,
    ExecutionOutput,
    ExecutionSafetyLevel,
    ExecutionSessionBuilder,
    ExecutionSessionState,
    ExecutionWorkspaceStore,
)
from aegis_runtime.execution.orchestrator import (
    ExecutionOrchestrator,
)
from aegis_runtime.execution.session_loader import (
    ExecutionSessionLoader,
)
from aegis_runtime.execution.workspace_store import (
    StoredExecutionSession,
)


def build_contract() -> ExecutionContract:
    """Create a representative persisted-session contract."""

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


def persist_session(
    tmp_path: Path,
    mode: ExecutionMode,
) -> tuple[ExecutionWorkspaceStore, StoredExecutionSession]:
    """Build, persist and reload one execution session record."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=mode,
        parameters={
            "scope": "public-api",
        },
    )

    assert result.ok

    store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    store.persist(result)

    record = store.load(
        result.workspace.workspace_id
    )

    return store, record


def test_session_loader_rehydrates_persisted_session(
    tmp_path: Path,
) -> None:
    """A persisted session must retain its identity and context."""

    _, record = persist_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    session = ExecutionSessionLoader().load(
        record
    )

    assert session.session_id == record.session_id
    assert session.workspace_id == record.workspace_id
    assert (
        session.target_asset_id
        == "security.review-api-security"
    )
    assert session.mode == ExecutionMode.PLAN
    assert (
        session.state
        == ExecutionSessionState.CONTEXT_READY
    )
    assert session.context is not None
    assert (
        session.context.get_input("scope")
        == "public-api"
    )
    assert session.created_at.tzinfo is not None
    assert session.updated_at.tzinfo is not None


def test_rehydrated_plan_session_can_be_orchestrated(
    tmp_path: Path,
) -> None:
    """A rehydrated plan session must reach the planned state."""

    _, record = persist_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    session = ExecutionSessionLoader().load(
        record
    )

    result = ExecutionOrchestrator().orchestrate(
        session
    )

    assert result.ok
    assert (
        session.state
        == ExecutionSessionState.PLANNED
    )
    assert len(result.events) == 3


def test_rehydrated_dry_run_session_can_be_orchestrated(
    tmp_path: Path,
) -> None:
    """A rehydrated dry-run session must reach dry-run-ready."""

    _, record = persist_session(
        tmp_path,
        ExecutionMode.DRY_RUN,
    )

    session = ExecutionSessionLoader().load(
        record
    )

    result = ExecutionOrchestrator().orchestrate(
        session
    )

    assert result.ok
    assert (
        session.state
        == ExecutionSessionState.DRY_RUN_READY
    )
    assert len(result.events) == 5


def test_session_loader_rejects_workspace_mismatch(
    tmp_path: Path,
) -> None:
    """Stored workspace identities must remain consistent."""

    _, record = persist_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    payload = deepcopy(record.payload)
    payload["session"]["workspace_id"] = (
        "different-workspace"
    )

    invalid_record = StoredExecutionSession(
        workspace_path=record.workspace_path,
        session_manifest=record.session_manifest,
        payload=payload,
    )

    with pytest.raises(
        ValueError,
        match="workspace ID does not match",
    ):
        ExecutionSessionLoader().load(
            invalid_record
        )


def test_session_loader_rejects_naive_datetime(
    tmp_path: Path,
) -> None:
    """Stored timestamps must retain timezone information."""

    _, record = persist_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    payload = deepcopy(record.payload)
    payload["session"]["created_at"] = (
        "2026-07-16T21:00:00"
    )

    invalid_record = StoredExecutionSession(
        workspace_path=record.workspace_path,
        session_manifest=record.session_manifest,
        payload=payload,
    )

    with pytest.raises(
        ValueError,
        match="must include a timezone",
    ):
        ExecutionSessionLoader().load(
            invalid_record
        )