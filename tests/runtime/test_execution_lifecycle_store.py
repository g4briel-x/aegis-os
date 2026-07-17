"""Tests for persistent execution lifecycle storage."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from aegis_runtime.execution import (
    ExecutionContract,
    ExecutionContractType,
    ExecutionInput,
    ExecutionMode,
    ExecutionOrchestrationStore,
    ExecutionOrchestrator,
    ExecutionOutput,
    ExecutionSafetyLevel,
    ExecutionSessionBuilder,
    ExecutionSessionLoader,
    ExecutionSessionState,
    ExecutionWorkspaceStore,
)
from aegis_runtime.execution.lifecycle import (
    ExecutionLifecycleManager,
)
from aegis_runtime.execution.lifecycle_store import (
    ExecutionLifecycleStore,
)


def build_contract() -> ExecutionContract:
    """Create a representative lifecycle contract."""

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


def persist_context_ready_session(
    tmp_path: Path,
    mode: ExecutionMode,
):
    """Build and persist one context-ready session."""

    build_result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=mode,
        parameters={
            "scope": "public-api",
        },
    )

    assert build_result.ok

    workspace_store = ExecutionWorkspaceStore(
        repo_root=tmp_path,
    )

    persisted_workspace = workspace_store.persist(
        build_result
    )

    record = workspace_store.load(
        build_result.workspace.workspace_id
    )

    return (
        workspace_store,
        persisted_workspace,
        record,
    )


def persist_prepared_session(
    tmp_path: Path,
    mode: ExecutionMode,
):
    """Persist and orchestrate one execution session."""

    (
        workspace_store,
        persisted_workspace,
        record,
    ) = persist_context_ready_session(
        tmp_path,
        mode,
    )

    session = ExecutionSessionLoader().load(
        record
    )

    orchestration_result = (
        ExecutionOrchestrator().orchestrate(
            session
        )
    )

    ExecutionOrchestrationStore().persist(
        record=record,
        result=orchestration_result,
    )

    prepared_record = workspace_store.load(
        record.workspace_id
    )

    prepared_session = ExecutionSessionLoader().load(
        prepared_record
    )

    return (
        workspace_store,
        persisted_workspace,
        prepared_record,
        prepared_session,
    )


def test_store_persists_completed_plan_session(
    tmp_path: Path,
) -> None:
    """A completed plan session must be persisted and reloadable."""

    (
        workspace_store,
        _,
        record,
        session,
    ) = persist_prepared_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    lifecycle_result = (
        ExecutionLifecycleManager().complete(
            session,
            reason="Execution plan review completed.",
        )
    )

    persisted = ExecutionLifecycleStore().persist(
        record=record,
        result=lifecycle_result,
    )

    assert persisted.event_count == 2
    assert persisted.terminal_state == "completed"

    session_payload = json.loads(
        persisted.session_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert (
        session_payload["session"]["state"]
        == "completed"
    )
    assert (
        session_payload["session"]["completed_at"]
        is not None
    )
    assert (
        session_payload["lifecycle"]["action"]
        == "complete"
    )
    assert (
        session_payload["lifecycle"]["reason"]
        == "Execution plan review completed."
    )
    assert (
        session_payload["lifecycle"]["event_count"]
        == 2
    )

    audit_payload = json.loads(
        persisted.audit_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert audit_payload["state"] == "completed"
    assert audit_payload["event_count"] == 5
    assert [
        event["event_type"]
        for event in audit_payload["events"][-2:]
    ] == [
        "state-transition",
        "session-completed",
    ]

    reloaded_record = workspace_store.load(
        record.workspace_id
    )

    reloaded_session = ExecutionSessionLoader().load(
        reloaded_record
    )

    assert (
        reloaded_session.state
        == ExecutionSessionState.COMPLETED
    )
    assert reloaded_session.is_terminal


def test_store_persists_cancelled_dry_run_session(
    tmp_path: Path,
) -> None:
    """A dry-run-ready session may be cancelled and persisted."""

    (
        _,
        _,
        record,
        session,
    ) = persist_prepared_session(
        tmp_path,
        ExecutionMode.DRY_RUN,
    )

    lifecycle_result = (
        ExecutionLifecycleManager().cancel(
            session,
            reason="Operator cancelled the dry-run review.",
            actor="operator:test",
        )
    )

    persisted = ExecutionLifecycleStore().persist(
        record=record,
        result=lifecycle_result,
    )

    session_payload = json.loads(
        persisted.session_manifest.read_text(
            encoding="utf-8"
        )
    )

    audit_payload = json.loads(
        persisted.audit_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert persisted.terminal_state == "cancelled"
    assert (
        session_payload["session"]["state"]
        == "cancelled"
    )
    assert (
        session_payload["lifecycle"]["actor"]
        == "operator:test"
    )
    assert audit_payload["state"] == "cancelled"
    assert audit_payload["event_count"] == 7
    assert (
        audit_payload["events"][-1]["event_type"]
        == "session-cancelled"
    )


def test_store_persists_failed_context_ready_session(
    tmp_path: Path,
) -> None:
    """A context-ready session may fail before orchestration."""

    (
        _,
        _,
        record,
    ) = persist_context_ready_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    session = ExecutionSessionLoader().load(
        record
    )

    lifecycle_result = (
        ExecutionLifecycleManager().fail(
            session,
            reason="Execution input validation failed.",
        )
    )

    persisted = ExecutionLifecycleStore().persist(
        record=record,
        result=lifecycle_result,
    )

    audit_payload = json.loads(
        persisted.audit_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert persisted.terminal_state == "failed"
    assert audit_payload["state"] == "failed"
    assert audit_payload["event_count"] == 2
    assert [
        event["event_type"]
        for event in audit_payload["events"]
    ] == [
        "state-transition",
        "session-failed",
    ]


def test_store_rejects_workspace_identity_mismatch(
    tmp_path: Path,
) -> None:
    """Lifecycle and stored workspace identities must match."""

    (
        _,
        _,
        record,
    ) = persist_context_ready_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    session = ExecutionSessionLoader().load(
        record
    )

    lifecycle_result = (
        ExecutionLifecycleManager().fail(
            session,
            reason="Execution failed.",
        )
    )

    lifecycle_result.session.workspace_id = (
        "different-workspace"
    )

    with pytest.raises(
        ValueError,
        match="workspace ID does not match",
    ):
        ExecutionLifecycleStore().persist(
            record=record,
            result=lifecycle_result,
        )


def test_store_rejects_missing_audit_manifest(
    tmp_path: Path,
) -> None:
    """Lifecycle persistence requires its audit manifest."""

    (
        _,
        persisted_workspace,
        record,
        session,
    ) = persist_prepared_session(
        tmp_path,
        ExecutionMode.PLAN,
    )

    lifecycle_result = (
        ExecutionLifecycleManager().complete(
            session
        )
    )

    persisted_workspace.audit_manifest.unlink()

    with pytest.raises(
        FileNotFoundError,
        match="audit manifest does not exist",
    ):
        ExecutionLifecycleStore().persist(
            record=record,
            result=lifecycle_result,
        )