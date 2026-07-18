"""Tests for execution audit journal integrity protection."""

from __future__ import annotations

import copy
from typing import Any

import pytest

from aegis_runtime.execution.audit_integrity import (
    AUDIT_GENESIS_HASH,
    AUDIT_INTEGRITY_ALGORITHM,
    AUDIT_INTEGRITY_VERSION,
    ExecutionAuditIntegrity,
)


def _audit_payload() -> dict[str, Any]:
    """Build one representative execution audit manifest."""

    return {
        "session_id": "session-test-integrity",
        "workspace_id": "workspace-test-integrity",
        "target_asset_id": "security.review-api-security",
        "mode": "dry-run",
        "state": "completed",
        "created_at": "2026-07-17T20:00:00+00:00",
        "updated_at": "2026-07-17T20:02:00+00:00",
        "started_at": "2026-07-17T20:00:30+00:00",
        "completed_at": "2026-07-17T20:02:00+00:00",
        "event_count": 2,
        "last_event_at": "2026-07-17T20:02:00+00:00",
        "audit_metadata": {
            "source": "test-suite",
            "schema": "execution-audit",
        },
        "events": [
            {
                "event_id": "event-0001",
                "event_type": "session-loaded",
                "session_id": "session-test-integrity",
                "workspace_id": "workspace-test-integrity",
                "timestamp": "2026-07-17T20:00:30+00:00",
                "actor": "test:integrity",
                "message": "Execution session loaded.",
                "previous_state": None,
                "next_state": "context-ready",
                "metadata": {
                    "sequence": 1,
                },
            },
            {
                "event_id": "event-0002",
                "event_type": "session-completed",
                "session_id": "session-test-integrity",
                "workspace_id": "workspace-test-integrity",
                "timestamp": "2026-07-17T20:02:00+00:00",
                "actor": "test:integrity",
                "message": "Execution session completed.",
                "previous_state": "plan-ready",
                "next_state": "completed",
                "metadata": {
                    "sequence": 2,
                    "result": "success",
                },
            },
        ],
    }


def test_seals_and_verifies_audit_journal() -> None:
    """A valid audit journal receives a verifiable seal."""

    engine = ExecutionAuditIntegrity()
    payload = _audit_payload()
    original_payload = copy.deepcopy(payload)

    sealed = engine.seal(payload)
    verification = engine.verify(sealed)

    assert payload == original_payload
    assert "integrity" not in payload
    assert engine.is_sealed(sealed)
    assert verification.ok
    assert verification.version == AUDIT_INTEGRITY_VERSION
    assert verification.algorithm == AUDIT_INTEGRITY_ALGORITHM
    assert verification.event_count == 2
    assert verification.root_hash != AUDIT_GENESIS_HASH
    assert len(verification.root_hash) == 64
    assert len(verification.manifest_hash) == 64
    assert len(verification.journal_hash) == 64

    verification_payload = verification.to_dict()

    assert verification_payload["ok"] is True
    assert verification_payload["event_count"] == 2


def test_seal_is_deterministic_and_idempotent() -> None:
    """Identical journals always produce the same seal."""

    engine = ExecutionAuditIntegrity()
    payload = _audit_payload()

    first_seal = engine.seal(payload)
    second_seal = engine.seal(
        copy.deepcopy(payload)
    )
    resealed = engine.seal(first_seal)

    assert first_seal == second_seal
    assert resealed == first_seal


def test_canonical_json_ignores_object_key_order() -> None:
    """JSON object insertion order does not change the seal."""

    engine = ExecutionAuditIntegrity()
    first_payload = _audit_payload()
    second_payload = copy.deepcopy(first_payload)

    second_payload["audit_metadata"] = {
        "schema": "execution-audit",
        "source": "test-suite",
    }
    second_payload["events"][1]["metadata"] = {
        "result": "success",
        "sequence": 2,
    }

    first_seal = engine.seal(first_payload)
    second_seal = engine.seal(second_payload)

    assert (
        first_seal["integrity"]
        == second_seal["integrity"]
    )


def test_verify_rejects_tampered_event_content() -> None:
    """Changing one event invalidates its chained hash."""

    engine = ExecutionAuditIntegrity()
    sealed = engine.seal(
        _audit_payload()
    )

    sealed["events"][0]["message"] = (
        "Execution event was modified."
    )

    with pytest.raises(
        ValueError,
        match="event hash",
    ):
        engine.verify(sealed)


def test_verify_rejects_reordered_events() -> None:
    """Changing event order invalidates the audit chain."""

    engine = ExecutionAuditIntegrity()
    sealed = engine.seal(
        _audit_payload()
    )

    sealed["events"].reverse()

    with pytest.raises(
        ValueError,
        match="event ID mismatch",
    ):
        engine.verify(sealed)


def test_verify_rejects_tampered_manifest_metadata() -> None:
    """Changing protected manifest metadata invalidates the seal."""

    engine = ExecutionAuditIntegrity()
    sealed = engine.seal(
        _audit_payload()
    )

    sealed["audit_metadata"]["source"] = (
        "untrusted-source"
    )

    with pytest.raises(
        ValueError,
        match="manifest hash",
    ):
        engine.verify(sealed)


def test_verify_rejects_tampered_chain_entry() -> None:
    """Changing a stored chain hash is detected."""

    engine = ExecutionAuditIntegrity()
    sealed = engine.seal(
        _audit_payload()
    )

    sealed["integrity"]["entries"][0][
        "event_hash"
    ] = "f" * 64

    with pytest.raises(
        ValueError,
        match="event hash",
    ):
        engine.verify(sealed)


def test_verify_rejects_missing_integrity_seal() -> None:
    """An unsealed audit journal cannot pass verification."""

    engine = ExecutionAuditIntegrity()
    payload = _audit_payload()

    assert not engine.is_sealed(payload)

    with pytest.raises(
        ValueError,
        match="no valid integrity seal",
    ):
        engine.verify(payload)