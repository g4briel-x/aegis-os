"""Tests for unified execution audit cryptographic protection."""

from __future__ import annotations

import copy
from typing import Any

import pytest

from aegis_runtime.execution.audit_authentication import (
    ExecutionAuditAuthenticator,
)
from aegis_runtime.execution.audit_integrity import (
    ExecutionAuditIntegrity,
)
from aegis_runtime.execution.audit_protection import (
    ExecutionAuditProtection,
)

_SECRET = (
    "0123456789abcdef"
    "0123456789abcdef"
)

_KEY_ID = "test-protection-key-v1"


def _audit_payload() -> dict[str, Any]:
    """Build one representative execution audit journal."""

    return {
        "session_id": "session-protection-test",
        "workspace_id": "workspace-protection-test",
        "target_asset_id": "security.review-api-security",
        "mode": "dry-run",
        "state": "completed",
        "created_at": "2026-07-23T02:00:00+00:00",
        "updated_at": "2026-07-23T02:02:00+00:00",
        "event_count": 2,
        "last_event_at": "2026-07-23T02:02:00+00:00",
        "events": [
            {
                "event_id": "event-protection-0001",
                "event_type": "session-loaded",
                "session_id": "session-protection-test",
                "workspace_id": "workspace-protection-test",
                "timestamp": "2026-07-23T02:00:30+00:00",
                "actor": "test:protection",
                "message": "Execution session loaded.",
                "previous_state": None,
                "next_state": "context-ready",
                "metadata": {
                    "sequence": 1,
                },
            },
            {
                "event_id": "event-protection-0002",
                "event_type": "session-completed",
                "session_id": "session-protection-test",
                "workspace_id": "workspace-protection-test",
                "timestamp": "2026-07-23T02:02:00+00:00",
                "actor": "test:protection",
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


def _authenticated_protection() -> ExecutionAuditProtection:
    """Build protection configured with one HMAC key."""

    authenticator = ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )

    return ExecutionAuditProtection(
        authenticator=authenticator,
    )


def test_seals_and_verifies_integrity_only_journal() -> None:
    """Protection without a key applies SHA-256 only."""

    protection = ExecutionAuditProtection()

    protected = protection.seal(
        _audit_payload()
    )

    verification = protection.verify(
        protected
    )

    assert "integrity" in protected
    assert "authentication" not in protected

    assert verification.ok
    assert not verification.authenticated
    assert verification.authentication is None
    assert verification.integrity.ok


def test_seals_and_verifies_authenticated_journal() -> None:
    """Configured protection applies SHA-256 and HMAC."""

    protection = _authenticated_protection()

    protected = protection.seal(
        _audit_payload()
    )

    verification = protection.verify(
        protected
    )

    assert "integrity" in protected
    assert "authentication" in protected

    assert verification.ok
    assert verification.authenticated
    assert verification.integrity.ok
    assert verification.authentication is not None
    assert verification.authentication.ok
    assert verification.authentication.key_id == _KEY_ID

    serialized = verification.to_dict()

    assert serialized["ok"] is True
    assert serialized["authenticated"] is True
    assert serialized["integrity"]["ok"] is True
    assert serialized["authentication"]["ok"] is True


def test_authenticated_seal_is_deterministic() -> None:
    """Identical input and key produce identical protection."""

    protection = _authenticated_protection()
    payload = _audit_payload()

    first = protection.seal(
        payload
    )

    second = protection.seal(
        payload
    )

    repeated = protection.seal(
        first
    )

    assert first == second
    assert repeated == first


def test_configured_key_requires_authentication_by_default() -> None:
    """Configured HMAC mode rejects an unsigned journal by default."""

    integrity_only = ExecutionAuditIntegrity().seal(
        _audit_payload()
    )

    protection = _authenticated_protection()

    with pytest.raises(
        ValueError,
        match="authentication is required",
    ):
        protection.verify(
            integrity_only
        )


def test_explicit_legacy_mode_allows_unsigned_journal() -> None:
    """A valid legacy journal may be verified explicitly."""

    integrity_only = ExecutionAuditIntegrity().seal(
        _audit_payload()
    )

    protection = _authenticated_protection()

    verification = protection.verify(
        integrity_only,
        require_authentication=False,
    )

    assert verification.ok
    assert not verification.authenticated
    assert verification.authentication is None


def test_signed_journal_cannot_be_verified_without_key() -> None:
    """A signed journal requires its HMAC key for verification."""

    signed = _authenticated_protection().seal(
        _audit_payload()
    )

    protection_without_key = ExecutionAuditProtection()

    with pytest.raises(
        ValueError,
        match="no HMAC key is configured",
    ):
        protection_without_key.verify(
            signed
        )


def test_signed_journal_cannot_be_resealed_without_key() -> None:
    """Existing authentication cannot be silently removed."""

    signed = _authenticated_protection().seal(
        _audit_payload()
    )

    protection_without_key = ExecutionAuditProtection()

    with pytest.raises(
        ValueError,
        match="cannot be replaced or removed",
    ):
        protection_without_key.seal(
            signed
        )


def test_rejects_resealed_forged_authenticated_journal() -> None:
    """Recalculated SHA-256 seals cannot recreate a valid HMAC."""

    protection = _authenticated_protection()

    authenticated = protection.seal(
        _audit_payload()
    )

    forged = copy.deepcopy(
        authenticated
    )

    original_authentication = forged.pop(
        "authentication"
    )

    forged["events"][0]["message"] = (
        "Forged execution event."
    )

    forged = ExecutionAuditIntegrity().seal(
        forged
    )

    forged["authentication"] = (
        original_authentication
    )

    with pytest.raises(
        ValueError,
        match="journal hash does not match",
    ):
        protection.verify(
            forged
        )