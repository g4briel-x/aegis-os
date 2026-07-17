"""Tests for controlled execution orchestration."""

from __future__ import annotations

import pytest

from aegis_runtime.execution import (
    ExecutionContract,
    ExecutionContractType,
    ExecutionInput,
    ExecutionMode,
    ExecutionOutput,
    ExecutionSafetyLevel,
    ExecutionSession,
    ExecutionSessionBuilder,
    ExecutionSessionState,
)
from aegis_runtime.execution.audit import (
    ExecutionAuditEventType,
)
from aegis_runtime.execution.orchestrator import (
    ExecutionOrchestrator,
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


def build_session(
    mode: ExecutionMode,
) -> ExecutionSession:
    """Build one valid context-ready execution session."""

    result = ExecutionSessionBuilder().build(
        contract=build_contract(),
        mode=mode,
        parameters={
            "scope": "public-api",
        },
    )

    assert result.ok

    return result.session


def test_orchestrator_prepares_plan_session() -> None:
    """Plan mode must reach the planned state."""

    session = build_session(
        ExecutionMode.PLAN
    )

    result = ExecutionOrchestrator().orchestrate(
        session
    )

    assert result.ok
    assert (
        session.state
        == ExecutionSessionState.PLANNED
    )
    assert session.started_at is not None
    assert session.completed_at is None

    event_types = [
        event.event_type
        for event in result.events
    ]

    assert event_types == [
        ExecutionAuditEventType.ORCHESTRATION_STARTED,
        ExecutionAuditEventType.STATE_TRANSITION,
        ExecutionAuditEventType.PLAN_CREATED,
    ]

    transition = result.events[1]

    assert transition.previous_state == "context-ready"
    assert transition.next_state == "planned"
    assert transition.session_id == session.session_id
    assert transition.workspace_id == session.workspace_id


def test_orchestrator_prepares_dry_run_session() -> None:
    """Dry-run mode must reach the dry-run-ready state."""

    session = build_session(
        ExecutionMode.DRY_RUN
    )

    result = ExecutionOrchestrator().orchestrate(
        session
    )

    assert result.ok
    assert (
        session.state
        == ExecutionSessionState.DRY_RUN_READY
    )

    event_types = [
        event.event_type
        for event in result.events
    ]

    assert event_types == [
        ExecutionAuditEventType.ORCHESTRATION_STARTED,
        ExecutionAuditEventType.STATE_TRANSITION,
        ExecutionAuditEventType.PLAN_CREATED,
        ExecutionAuditEventType.STATE_TRANSITION,
        ExecutionAuditEventType.DRY_RUN_PREPARED,
    ]

    final_transition = result.events[3]

    assert final_transition.previous_state == "planned"
    assert final_transition.next_state == "dry-run-ready"


def test_orchestrator_rejects_session_without_context() -> None:
    """A session without resolved context cannot be orchestrated."""

    session = ExecutionSession(
        target_asset_id="security.review-api-security",
        mode=ExecutionMode.PLAN,
        workspace_id="workspace-test",
    )

    with pytest.raises(
        ValueError,
        match="resolved context",
    ):
        ExecutionOrchestrator().orchestrate(
            session
        )


def test_orchestrator_rejects_session_without_workspace() -> None:
    """A session without workspace identity cannot be orchestrated."""

    session = build_session(
        ExecutionMode.PLAN
    )

    session.workspace_id = ""

    with pytest.raises(
        ValueError,
        match="workspace ID",
    ):
        ExecutionOrchestrator().orchestrate(
            session
        )


def test_orchestrator_rejects_invalid_starting_state() -> None:
    """Only context-ready sessions may enter orchestration."""

    session = build_session(
        ExecutionMode.PLAN
    )

    session.transition_to(
        ExecutionSessionState.PLANNED
    )

    with pytest.raises(
        ValueError,
        match="context-ready",
    ):
        ExecutionOrchestrator().orchestrate(
            session
        )