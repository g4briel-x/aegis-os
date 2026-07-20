"""Tests for unified execution audit cryptographic protection."""

from __future__ import annotations

from typing import Any

import pytest

from aegis_runtime.execution.audit_authentication import (
    ExecutionAuditAuthenticator,
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
        "session_id": "session-test-protection",
        "workspace_id": "workspace-test-protection",
        "target_asset_id": "security.review-api-security",
        "mode": "dry-run",
        "state": "completed",
        "created_at": "2026-07-18T01:00:00+00:00",
        "updated_at": "2026-07-18T01:02:00+00:00",
        "event_count": 2,
        "events": [
            {
                "event_id": "event-protection-0001",
                "event_type": "session-loaded",
                "session_id": "session-test-protection",
                "workspace_id": "workspace-test-protection",
                "timestamp": "2026-07-18T01:00:30+00:00",
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
                "session_id": "session-test-protection",
                "workspace_id": "workspace-test-protection",
                "timestamp": "2026-07-18T01:02:00+00:00",
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
        authenticator=authenticator
    )


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

    payload = verification.to_dict()

    assert payload["ok"] is True
    assert payload["authenticated"] is True
    assert payload["integrity"]["ok"] is True
    assert payload["authentication"]["ok"] is True


def test_seals_and_verifies_integrity_only_journal() -> None:
    """Protection without a key preserves SHA-256 compatibility."""

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


def test_verify_requires_authentication_when_requested() -> None:
    """An unsigned journal is rejected in mandatory HMAC mode."""

    integrity_only = ExecutionAuditProtection()

    protected = integrity_only.seal(
        _audit_payload()
    )

    with pytest.raises(
        ValueError,
        match="authentication is required",
    ):
        integrity_only.verify(
            protected,
            require_authentication=True,
        )


def test_verify_rejects_signed_journal_without_key() -> None:
    """A signed journal cannot be authenticated without its key."""

    signer = _authenticated_protection()
    verifier = ExecutionAuditProtection()

    protected = signer.seal(
        _audit_payload()
    )

    with pytest.raises(
        ValueError,
        match="no HMAC key is configured",
    ):
        verifier.verify(
            protected
        )


def test_seal_rejects_authenticated_journal_without_key() -> None:
    """An existing HMAC signature cannot be silently removed."""

    signer = _authenticated_protection()
    unsigned_protection = ExecutionAuditProtection()

    protected = signer.seal(
        _audit_payload()
    )

    with pytest.raises(
        ValueError,
        match="cannot be replaced or removed",
    ):
        unsigned_protection.seal(
            protected
        )


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
    resealed = protection.seal(
        first
    )

    assert first == second
    assert resealed == first