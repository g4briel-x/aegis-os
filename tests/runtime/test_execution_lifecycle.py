"""Tests for terminal execution lifecycle management."""

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
from aegis_runtime.execution.lifecycle import (
    ExecutionLifecycleAction,
    ExecutionLifecycleManager,
)
from aegis_runtime.execution.orchestrator import (
    ExecutionOrchestrator,
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


def build_prepared_session(
    mode: ExecutionMode,
) -> ExecutionSession:
    """Build and orchestrate one session."""

    session = build_session(mode)

    result = ExecutionOrchestrator().orchestrate(
        session
    )

    assert result.ok

    return session


def test_lifecycle_completes_plan_session() -> None:
    """A planned session may become completed."""

    session = build_prepared_session(
        ExecutionMode.PLAN
    )

    result = ExecutionLifecycleManager().complete(
        session
    )

    assert result.ok
    assert result.action == ExecutionLifecycleAction.COMPLETE
    assert result.reason == (
        "Execution lifecycle completed successfully."
    )
    assert session.state == ExecutionSessionState.COMPLETED
    assert session.is_terminal
    assert session.completed_at is not None

    assert [
        event.event_type
        for event in result.events
    ] == [
        ExecutionAuditEventType.STATE_TRANSITION,
        ExecutionAuditEventType.SESSION_COMPLETED,
    ]

    transition = result.events[0]

    assert transition.previous_state == "planned"
    assert transition.next_state == "completed"

    lifecycle_metadata = session.audit_metadata[
        "lifecycle"
    ]

    assert lifecycle_metadata["action"] == "complete"
    assert lifecycle_metadata["previous_state"] == "planned"
    assert (
        lifecycle_metadata["terminal_state"]
        == "completed"
    )


def test_lifecycle_completes_dry_run_session() -> None:
    """A dry-run-ready session may become completed."""

    session = build_prepared_session(
        ExecutionMode.DRY_RUN
    )

    result = ExecutionLifecycleManager().complete(
        session,
        reason="Dry-run review completed.",
    )

    assert result.ok
    assert session.state == ExecutionSessionState.COMPLETED
    assert result.reason == "Dry-run review completed."
    assert (
        result.events[0].previous_state
        == "dry-run-ready"
    )
    assert result.events[0].next_state == "completed"


def test_lifecycle_fails_context_ready_session() -> None:
    """An active session may be marked as failed."""

    session = build_session(
        ExecutionMode.PLAN
    )

    result = ExecutionLifecycleManager().fail(
        session,
        reason="Required execution input was rejected.",
        actor="operator:test",
    )

    assert result.ok
    assert result.action == ExecutionLifecycleAction.FAIL
    assert session.state == ExecutionSessionState.FAILED
    assert session.completed_at is not None
    assert result.actor == "operator:test"

    assert [
        event.event_type
        for event in result.events
    ] == [
        ExecutionAuditEventType.STATE_TRANSITION,
        ExecutionAuditEventType.SESSION_FAILED,
    ]

    assert all(
        event.actor == "operator:test"
        for event in result.events
    )

    assert (
        result.events[-1].metadata["reason"]
        == "Required execution input was rejected."
    )


def test_lifecycle_cancels_planned_session() -> None:
    """A planned session may be cancelled."""

    session = build_prepared_session(
        ExecutionMode.PLAN
    )

    result = ExecutionLifecycleManager().cancel(
        session,
        reason="Execution was cancelled by the operator.",
    )

    assert result.ok
    assert (
        result.action
        == ExecutionLifecycleAction.CANCEL
    )
    assert (
        session.state
        == ExecutionSessionState.CANCELLED
    )
    assert (
        result.events[-1].event_type
        == ExecutionAuditEventType.SESSION_CANCELLED
    )
    assert (
        result.events[-1].previous_state
        == "planned"
    )
    assert (
        result.events[-1].next_state
        == "cancelled"
    )


def test_lifecycle_rejects_early_completion() -> None:
    """Completion requires a prepared session state."""

    session = build_session(
        ExecutionMode.PLAN
    )

    with pytest.raises(
        ValueError,
        match="planned",
    ):
        ExecutionLifecycleManager().complete(
            session
        )


@pytest.mark.parametrize(
    "action",
    [
        ExecutionLifecycleAction.FAIL,
        ExecutionLifecycleAction.CANCEL,
    ],
)
def test_lifecycle_requires_reason(
    action: ExecutionLifecycleAction,
) -> None:
    """Failure and cancellation require an explicit reason."""

    session = build_session(
        ExecutionMode.PLAN
    )

    with pytest.raises(
        ValueError,
        match="requires a reason",
    ):
        ExecutionLifecycleManager().transition(
            session=session,
            action=action,
            reason="   ",
        )


def test_lifecycle_rejects_empty_actor() -> None:
    """Lifecycle audit actors cannot be empty."""

    session = build_session(
        ExecutionMode.PLAN
    )

    with pytest.raises(
        ValueError,
        match="actor cannot be empty",
    ):
        ExecutionLifecycleManager().fail(
            session,
            reason="Execution failed.",
            actor="   ",
        )


def test_lifecycle_rejects_second_terminal_transition() -> None:
    """A terminal session cannot transition again."""

    session = build_prepared_session(
        ExecutionMode.PLAN
    )

    ExecutionLifecycleManager().complete(
        session
    )

    with pytest.raises(
        ValueError,
        match="terminal execution session",
    ):
        ExecutionLifecycleManager().cancel(
            session,
            reason="Second transition is forbidden.",
        )