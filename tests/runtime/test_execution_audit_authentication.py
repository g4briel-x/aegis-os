"""Tests for execution audit HMAC authentication."""

from __future__ import annotations

import copy
from typing import Any

import pytest

from aegis_runtime.execution.audit_authentication import (
    AUDIT_AUTHENTICATION_ALGORITHM,
    AUDIT_AUTHENTICATION_CONTEXT,
    AUDIT_AUTHENTICATION_VERSION,
    ExecutionAuditAuthenticator,
)
from aegis_runtime.execution.audit_integrity import (
    ExecutionAuditIntegrity,
)

_SECRET = (
    "0123456789abcdef"
    "0123456789abcdef"
)
_OTHER_SECRET = (
    "abcdef0123456789"
    "abcdef0123456789"
)
_KEY_ID = "test-audit-key-v1"


def _audit_payload() -> dict[str, Any]:
    """Build one representative execution audit journal."""

    return {
        "session_id": "session-authentication-test",
        "workspace_id": "workspace-authentication-test",
        "target_asset_id": "security.review-api-security",
        "mode": "dry-run",
        "state": "completed",
        "created_at": "2026-07-23T01:00:00+00:00",
        "updated_at": "2026-07-23T01:02:00+00:00",
        "started_at": "2026-07-23T01:00:10+00:00",
        "completed_at": "2026-07-23T01:02:00+00:00",
        "audit_metadata": {
            "actor": "test:audit-authentication",
        },
        "event_count": 2,
        "last_event_at": "2026-07-23T01:02:00+00:00",
        "events": [
            {
                "event_id": "event-authentication-0001",
                "event_type": "session-loaded",
                "session_id": "session-authentication-test",
                "workspace_id": "workspace-authentication-test",
                "timestamp": "2026-07-23T01:00:10+00:00",
                "actor": "test:audit-authentication",
                "message": "Execution session loaded.",
                "previous_state": None,
                "next_state": "context-ready",
                "metadata": {
                    "sequence": 1,
                },
            },
            {
                "event_id": "event-authentication-0002",
                "event_type": "session-completed",
                "session_id": "session-authentication-test",
                "workspace_id": "workspace-authentication-test",
                "timestamp": "2026-07-23T01:02:00+00:00",
                "actor": "test:audit-authentication",
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


def _sealed_payload() -> dict[str, Any]:
    """Build one SHA-256 integrity-sealed journal."""

    return ExecutionAuditIntegrity().seal(
        _audit_payload()
    )


def _authenticator() -> ExecutionAuditAuthenticator:
    """Build the default test authenticator."""

    return ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )


def test_authenticates_and_verifies_sealed_journal() -> None:
    """A valid integrity-sealed journal receives valid HMAC metadata."""

    authenticator = _authenticator()

    authenticated = authenticator.authenticate(
        _sealed_payload()
    )
    verification = authenticator.verify(
        authenticated
    )

    assert verification.ok
    assert verification.version == AUDIT_AUTHENTICATION_VERSION
    assert verification.algorithm == AUDIT_AUTHENTICATION_ALGORITHM
    assert verification.context == AUDIT_AUTHENTICATION_CONTEXT
    assert verification.key_id == _KEY_ID

    authentication = authenticated["authentication"]

    assert authentication["version"] == AUDIT_AUTHENTICATION_VERSION
    assert authentication["algorithm"] == AUDIT_AUTHENTICATION_ALGORITHM
    assert authentication["context"] == AUDIT_AUTHENTICATION_CONTEXT
    assert authentication["key_id"] == _KEY_ID
    assert len(authentication["journal_hash"]) == 64
    assert len(authentication["signature"]) == 64


def test_authentication_is_deterministic_and_idempotent() -> None:
    """Identical journal and key material produce identical output."""

    authenticator = _authenticator()
    sealed = _sealed_payload()

    first = authenticator.authenticate(
        sealed
    )
    second = authenticator.authenticate(
        sealed
    )
    repeated = authenticator.authenticate(
        first
    )

    assert first == second
    assert repeated == first


def test_rejects_secret_shorter_than_minimum() -> None:
    """Weak HMAC secrets are rejected during initialization."""

    with pytest.raises(
        ValueError,
        match="at least 32 bytes",
    ):
        ExecutionAuditAuthenticator(
            "too-short",
            key_id=_KEY_ID,
        )


def test_verification_rejects_wrong_secret() -> None:
    """A journal cannot be verified using different secret material."""

    authenticated = _authenticator().authenticate(
        _sealed_payload()
    )

    verifier = ExecutionAuditAuthenticator(
        _OTHER_SECRET,
        key_id=_KEY_ID,
    )

    with pytest.raises(
        ValueError,
        match="signature does not match",
    ):
        verifier.verify(
            authenticated
        )


def test_verification_rejects_wrong_key_id() -> None:
    """The public key identifier must match the configured key."""

    authenticated = _authenticator().authenticate(
        _sealed_payload()
    )

    verifier = ExecutionAuditAuthenticator(
        _SECRET,
        key_id="another-key-v1",
    )

    with pytest.raises(
        ValueError,
        match="key ID does not match",
    ):
        verifier.verify(
            authenticated
        )


def test_rejects_resealed_forged_journal() -> None:
    """Recalculating SHA-256 cannot recreate the original HMAC."""

    authenticator = _authenticator()

    authenticated = authenticator.authenticate(
        _sealed_payload()
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
        authenticator.verify(
            forged
        )


def test_verification_rejects_missing_authentication() -> None:
    """An integrity-only journal is not considered authenticated."""

    authenticator = _authenticator()
    sealed = _sealed_payload()

    assert not authenticator.is_authenticated(
        sealed
    )

    with pytest.raises(
        ValueError,
        match="metadata is missing",
    ):
        authenticator.verify(
            sealed
        )