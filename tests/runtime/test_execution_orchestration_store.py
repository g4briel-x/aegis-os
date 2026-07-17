"""Tests for persistent execution orchestration storage."""

from __future__ import annotations

import json
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
from aegis_runtime.execution.orchestration_store import (
    ExecutionOrchestrationStore,
)
from aegis_runtime.execution.orchestrator import (
    ExecutionOrchestrator,
)
from aegis_runtime.execution.session_loader import (
    ExecutionSessionLoader,
)


def build_contract() -> ExecutionContract:
    """Create a representative orchestration contract."""

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


def build_orchestration(
    tmp_path: Path,
    mode: ExecutionMode,
):
    """Build, persist, load and orchestrate one session."""

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

    session = ExecutionSessionLoader().load(
        record
    )

    orchestration_result = (
        ExecutionOrchestrator().orchestrate(
            session
        )
    )

    return (
        record,
        persisted_workspace,
        orchestration_result,
    )


def test_store_persists_plan_orchestration(
    tmp_path: Path,
) -> None:
    """Plan orchestration must update session and audit manifests."""

    (
        record,
        persisted_workspace,
        orchestration_result,
    ) = build_orchestration(
        tmp_path,
        ExecutionMode.PLAN,
    )

    persisted = ExecutionOrchestrationStore().persist(
        record=record,
        result=orchestration_result,
    )

    assert persisted.event_count == 3
    assert (
        orchestration_result.session.state
        == ExecutionSessionState.PLANNED
    )

    session_payload = json.loads(
        persisted.session_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert (
        session_payload["session"]["state"]
        == "planned"
    )
    assert (
        session_payload["orchestration"]["ok"]
        is True
    )
    assert (
        session_payload["orchestration"]["event_count"]
        == 3
    )
    assert (
        len(
            session_payload[
                "orchestration"
            ]["event_ids"]
        )
        == 3
    )

    audit_payload = json.loads(
        persisted.audit_manifest.read_text(
            encoding="utf-8"
        )
    )

    assert audit_payload["state"] == "planned"
    assert audit_payload["event_count"] == 3
    assert len(audit_payload["events"]) == 3
    assert [
        event["event_type"]
        for event in audit_payload["events"]
    ] == [
        "orchestration-started",
        "state-transition",
        "plan-created",
    ]

    assert (
        persisted.audit_manifest
        == persisted_workspace.audit_manifest
    )


def test_store_persists_dry_run_orchestration(
    tmp_path: Path,
) -> None:
    """Dry-run orchestration must persist all state transitions."""

    (
        record,
        _,
        orchestration_result,
    ) = build_orchestration(
        tmp_path,
        ExecutionMode.DRY_RUN,
    )

    persisted = ExecutionOrchestrationStore().persist(
        record=record,
        result=orchestration_result,
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

    assert persisted.event_count == 5
    assert (
        session_payload["session"]["state"]
        == "dry-run-ready"
    )
    assert (
        session_payload["orchestration"]["event_count"]
        == 5
    )
    assert audit_payload["state"] == "dry-run-ready"
    assert audit_payload["event_count"] == 5
    assert len(audit_payload["events"]) == 5
    assert (
        audit_payload["events"][-1]["event_type"]
        == "dry-run-prepared"
    )


def test_store_rejects_workspace_identity_mismatch(
    tmp_path: Path,
) -> None:
    """Orchestration and stored workspace identities must match."""

    (
        record,
        _,
        orchestration_result,
    ) = build_orchestration(
        tmp_path,
        ExecutionMode.PLAN,
    )

    orchestration_result.session.workspace_id = (
        "different-workspace"
    )

    with pytest.raises(
        ValueError,
        match="workspace ID does not match",
    ):
        ExecutionOrchestrationStore().persist(
            record=record,
            result=orchestration_result,
        )


def test_store_rejects_missing_audit_manifest(
    tmp_path: Path,
) -> None:
    """The declared audit manifest must exist before update."""

    (
        record,
        persisted_workspace,
        orchestration_result,
    ) = build_orchestration(
        tmp_path,
        ExecutionMode.PLAN,
    )

    persisted_workspace.audit_manifest.unlink()

    with pytest.raises(
        FileNotFoundError,
        match="audit manifest does not exist",
    ):
        ExecutionOrchestrationStore().persist(
            record=record,
            result=orchestration_result,
        )


def test_store_rejects_invalid_existing_event_collection(
    tmp_path: Path,
) -> None:
    """Stored audit events must remain a JSON array."""

    (
        record,
        persisted_workspace,
        orchestration_result,
    ) = build_orchestration(
        tmp_path,
        ExecutionMode.PLAN,
    )

    audit_payload = json.loads(
        persisted_workspace.audit_manifest.read_text(
            encoding="utf-8"
        )
    )

    audit_payload["events"] = {
        "invalid": True,
    }

    persisted_workspace.audit_manifest.write_text(
        json.dumps(
            audit_payload,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="events must be a JSON array",
    ):
        ExecutionOrchestrationStore().persist(
            record=record,
            result=orchestration_result,
        )