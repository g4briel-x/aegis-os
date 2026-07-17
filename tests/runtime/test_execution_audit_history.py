"""Tests for persistent execution audit history inspection."""

from __future__ import annotations

import json
from datetime import datetime, timedelta
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
from aegis_runtime.execution.audit import (
    ExecutionAuditEventType,
)
from aegis_runtime.execution.audit_history import (
    ExecutionAuditHistoryReader,
)
from aegis_runtime.execution.lifecycle import (
    ExecutionLifecycleManager,
)
from aegis_runtime.execution.lifecycle_store import (
    ExecutionLifecycleStore,
)


def build_contract() -> ExecutionContract:
    """Create a representative execution contract."""

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
    mode: ExecutionMode = ExecutionMode.PLAN,
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


def persist_completed_plan_session(
    tmp_path: Path,
):
    """Persist, orchestrate, and complete one plan session."""

    (
        workspace_store,
        persisted_workspace,
        record,
    ) = persist_context_ready_session(
        tmp_path,
        ExecutionMode.PLAN,
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
            reason="Execution review completed.",
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


def test_reader_loads_completed_execution_history(
    tmp_path: Path,
) -> None:
    """A completed session history must be reconstructed."""

    (
        record,
        _,
        persisted_lifecycle,
    ) = persist_completed_plan_session(
        tmp_path
    )

    history = ExecutionAuditHistoryReader().load(
        record
    )

    assert history.session_id == record.session_id
    assert history.workspace_id == record.workspace_id
    assert (
        history.target_asset_id
        == "security.review-api-security"
    )
    assert history.mode == ExecutionMode.PLAN
    assert (
        history.state
        == ExecutionSessionState.COMPLETED
    )
    assert (
        history.audit_manifest
        == persisted_lifecycle.audit_manifest
    )
    assert history.event_count == 5
    assert history.first_event_at is not None
    assert history.last_event_at is not None
    assert history.completed_at is not None

    assert [
        event.event_type
        for event in history.events[-2:]
    ] == [
        ExecutionAuditEventType.STATE_TRANSITION,
        ExecutionAuditEventType.SESSION_COMPLETED,
    ]

    serialized = history.to_dict()

    assert serialized["event_count"] == 5
    assert serialized["state"] == "completed"
    assert len(serialized["events"]) == 5
    assert (
        serialized["last_event_at"]
        == history.events[-1].timestamp
    )


def test_history_selects_events_without_mutation(
    tmp_path: Path,
) -> None:
    """History events may be filtered in read-only mode."""

    (
        record,
        _,
        _,
    ) = persist_completed_plan_session(
        tmp_path
    )

    history = ExecutionAuditHistoryReader().load(
        record
    )

    completed_events = history.select(
        event_type=(
            ExecutionAuditEventType.SESSION_COMPLETED
        )
    )

    assert len(completed_events) == 1
    assert (
        completed_events[0].event_type
        == ExecutionAuditEventType.SESSION_COMPLETED
    )

    operator_events = history.select(
        actor="operator:test"
    )

    assert len(operator_events) == 2
    assert all(
        event.actor == "operator:test"
        for event in operator_events
    )

    recent_events = history.select(
        reverse=True,
        limit=2,
    )

    assert [
        event.event_type
        for event in recent_events
    ] == [
        ExecutionAuditEventType.SESSION_COMPLETED,
        ExecutionAuditEventType.STATE_TRANSITION,
    ]

    assert history.event_count == 5

    with pytest.raises(
        ValueError,
        match="limit must be greater than zero",
    ):
        history.select(
            limit=0
        )


def test_reader_loads_history_without_events(
    tmp_path: Path,
) -> None:
    """A new context-ready session may have no events."""

    (
        _,
        persisted_workspace,
        record,
    ) = persist_context_ready_session(
        tmp_path
    )

    history = ExecutionAuditHistoryReader().load(
        record
    )

    assert (
        history.state
        == ExecutionSessionState.CONTEXT_READY
    )
    assert history.event_count == 0
    assert history.events == ()
    assert history.first_event_at is None
    assert history.last_event_at is None
    assert (
        history.audit_manifest
        == persisted_workspace.audit_manifest
    )


def test_reader_rejects_session_identity_mismatch(
    tmp_path: Path,
) -> None:
    """Audit and session identities must remain consistent."""

    (
        record,
        _,
        persisted_lifecycle,
    ) = persist_completed_plan_session(
        tmp_path
    )

    payload = read_json(
        persisted_lifecycle.audit_manifest
    )
    payload["session_id"] = "different-session"

    write_json(
        persisted_lifecycle.audit_manifest,
        payload,
    )

    with pytest.raises(
        ValueError,
        match="Audit session ID does not match",
    ):
        ExecutionAuditHistoryReader().load(
            record
        )


def test_reader_rejects_duplicate_event_ids(
    tmp_path: Path,
) -> None:
    """Every immutable audit event must have a unique ID."""

    (
        record,
        _,
        persisted_lifecycle,
    ) = persist_completed_plan_session(
        tmp_path
    )

    payload = read_json(
        persisted_lifecycle.audit_manifest
    )

    events = payload["events"]

    assert isinstance(events, list)
    assert len(events) >= 2

    events[-1]["event_id"] = events[0]["event_id"]

    write_json(
        persisted_lifecycle.audit_manifest,
        payload,
    )

    with pytest.raises(
        ValueError,
        match="event IDs must be unique",
    ):
        ExecutionAuditHistoryReader().load(
            record
        )


def test_reader_rejects_non_chronological_events(
    tmp_path: Path,
) -> None:
    """Audit events must remain chronologically ordered."""

    (
        record,
        _,
        persisted_lifecycle,
    ) = persist_completed_plan_session(
        tmp_path
    )

    payload = read_json(
        persisted_lifecycle.audit_manifest
    )

    events = payload["events"]

    assert isinstance(events, list)
    assert len(events) >= 2

    created_at = datetime.fromisoformat(
        payload["created_at"]
    )

    events[0]["timestamp"] = (
        created_at
        + timedelta(seconds=2)
    ).isoformat()

    events[1]["timestamp"] = (
        created_at
        + timedelta(seconds=1)
    ).isoformat()

    write_json(
        persisted_lifecycle.audit_manifest,
        payload,
    )

    with pytest.raises(
        ValueError,
        match="chronological order",
    ):
        ExecutionAuditHistoryReader().load(
            record
        )


def test_reader_rejects_incorrect_event_count(
    tmp_path: Path,
) -> None:
    """The stored event summary must match its collection."""

    (
        record,
        _,
        persisted_lifecycle,
    ) = persist_completed_plan_session(
        tmp_path
    )

    payload = read_json(
        persisted_lifecycle.audit_manifest
    )

    payload["event_count"] = 999

    write_json(
        persisted_lifecycle.audit_manifest,
        payload,
    )

    with pytest.raises(
        ValueError,
        match="event count does not match",
    ):
        ExecutionAuditHistoryReader().load(
            record
        )


def test_reader_rejects_audit_path_traversal(
    tmp_path: Path,
) -> None:
    """The audit manifest must remain inside its workspace."""

    (
        _,
        _,
        record,
    ) = persist_context_ready_session(
        tmp_path
    )

    workspace_payload = record.payload["workspace"]
    locations = workspace_payload["locations"]

    for location in locations:
        if location["name"] == "session-audit":
            location["relative_path"] = (
                "../outside-audit.json"
            )
            break

    with pytest.raises(
        ValueError,
        match="not workspace-relative",
    ):
        ExecutionAuditHistoryReader().load(
            record
        )