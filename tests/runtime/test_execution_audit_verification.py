"""Tests for persistent execution audit verification reporting."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

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
from aegis_runtime.execution.audit_verification import (
    ExecutionAuditVerifier,
)
from aegis_runtime.execution.lifecycle import (
    ExecutionLifecycleManager,
)
from aegis_runtime.execution.lifecycle_store import (
    ExecutionLifecycleStore,
)


def build_contract() -> ExecutionContract:
    """Create a representative verification contract."""

    return ExecutionContract(
        asset_id="security.review-api-security",
        contract_type=ExecutionContractType.SKILL,
        safety_level=ExecutionSafetyLevel.SAFE_DRY_RUN,
        allowed_modes=[
            "plan",
            "dry-run",
        ],
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
):
    """Build and persist one context-ready session."""

    build_result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=ExecutionMode.PLAN,
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


def persist_completed_session(
    tmp_path: Path,
):
    """Persist, orchestrate, and complete one plan session."""

    (
        workspace_store,
        persisted_workspace,
        record,
    ) = persist_context_ready_session(
        tmp_path
    )

    session = ExecutionSessionLoader().load(
        record
    )

    orchestration_result = (
        ExecutionOrchestrator().orchestrate(
            session
        )
    )

    assert orchestration_result.ok

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

    lifecycle_result = (
        ExecutionLifecycleManager().complete(
            prepared_session,
            reason="Verification test completed.",
            actor="operator:test",
        )
    )

    assert lifecycle_result.ok

    persisted_lifecycle = (
        ExecutionLifecycleStore().persist(
            record=prepared_record,
            result=lifecycle_result,
        )
    )

    completed_record = workspace_store.load(
        prepared_record.workspace_id
    )

    return (
        completed_record,
        persisted_workspace,
        persisted_lifecycle,
    )


def read_json(
    path: Path,
) -> dict[str, Any]:
    """Read one JSON object."""

    payload = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    assert isinstance(payload, dict)

    return payload


def write_json(
    path: Path,
    payload: dict[str, Any],
) -> None:
    """Write one JSON object."""

    path.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def test_verifier_reports_valid_completed_audit(
    tmp_path: Path,
) -> None:
    """A valid completed journal produces a full report."""

    (
        record,
        _,
        persisted_lifecycle,
    ) = persist_completed_session(
        tmp_path
    )

    report = ExecutionAuditVerifier().verify(
        record
    )

    assert report.ok
    assert report.session_id == record.session_id
    assert report.workspace_id == record.workspace_id
    assert (
        report.target_asset_id
        == "security.review-api-security"
    )
    assert report.mode == ExecutionMode.PLAN
    assert (
        report.state
        == ExecutionSessionState.COMPLETED
    )
    assert (
        report.audit_manifest
        == persisted_lifecycle.audit_manifest
    )
    assert report.event_count == 5
    assert report.integrity.algorithm == "sha256"
    assert len(report.integrity.root_hash) == 64
    assert len(report.integrity.manifest_hash) == 64
    assert len(report.integrity.journal_hash) == 64

    serialized = report.to_dict()

    assert serialized["ok"] is True
    assert serialized["event_count"] == 5
    assert serialized["state"] == "completed"
    assert serialized["mode"] == "plan"
    assert (
        serialized["integrity"]["algorithm"]
        == "sha256"
    )
    assert (
        serialized["audit_manifest"]
        == str(persisted_lifecycle.audit_manifest)
    )


def test_verifier_reports_valid_empty_audit(
    tmp_path: Path,
) -> None:
    """A newly created journal with no events remains valid."""

    (
        _,
        persisted_workspace,
        record,
    ) = persist_context_ready_session(
        tmp_path
    )

    report = ExecutionAuditVerifier().verify(
        record
    )

    assert report.ok
    assert (
        report.state
        == ExecutionSessionState.CONTEXT_READY
    )
    assert report.event_count == 0
    assert report.integrity.event_count == 0
    assert report.integrity.root_hash == "0" * 64
    assert (
        report.audit_manifest
        == persisted_workspace.audit_manifest
    )


def test_verifier_rejects_tampered_audit_event(
    tmp_path: Path,
) -> None:
    """A modified event invalidates verification."""

    (
        record,
        _,
        persisted_lifecycle,
    ) = persist_completed_session(
        tmp_path
    )

    payload = read_json(
        persisted_lifecycle.audit_manifest
    )

    events = payload["events"]

    assert isinstance(events, list)
    assert events

    events[0]["message"] = (
        "This audit event was altered."
    )

    write_json(
        persisted_lifecycle.audit_manifest,
        payload,
    )

    with pytest.raises(
        ValueError,
        match="event hash",
    ):
        ExecutionAuditVerifier().verify(
            record
        )