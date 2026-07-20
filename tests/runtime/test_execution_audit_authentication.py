"""Tests for execution audit journal HMAC authentication."""

from __future__ import annotations

import copy
from typing import Any

import pytest

from aegis_runtime.execution.audit_authentication import (
    AUDIT_AUTHENTICATION_ALGORITHM,
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
_ALTERNATE_SECRET = (
    "abcdef0123456789"
    "abcdef0123456789"
)
_KEY_ID = "test-audit-key-v1"


def _audit_payload() -> dict[str, Any]:
    """Build one representative execution audit manifest."""

    return {
        "session_id": "session-test-authentication",
        "workspace_id": "workspace-test-authentication",
        "target_asset_id": "security.review-api-security",
        "mode": "dry-run",
        "state": "completed",
        "created_at": "2026-07-18T00:00:00+00:00",
        "updated_at": "2026-07-18T00:02:00+00:00",
        "event_count": 2,
        "events": [
            {
                "event_id": "event-authentication-0001",
                "event_type": "session-loaded",
                "session_id": "session-test-authentication",
                "workspace_id": "workspace-test-authentication",
                "timestamp": "2026-07-18T00:00:30+00:00",
                "actor": "test:authentication",
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
                "session_id": "session-test-authentication",
                "workspace_id": "workspace-test-authentication",
                "timestamp": "2026-07-18T00:02:00+00:00",
                "actor": "test:authentication",
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
    """Build one valid integrity-sealed audit journal."""

    return ExecutionAuditIntegrity().seal(
        _audit_payload()
    )


def test_authenticates_and_verifies_audit_journal() -> None:
    """A sealed audit journal receives a valid HMAC signature."""

    authenticator = ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )
    payload = _sealed_payload()
    original_payload = copy.deepcopy(
        payload
    )

    authenticated = authenticator.authenticate(
        payload
    )
    verification = authenticator.verify(
        authenticated
    )

    assert payload == original_payload
    assert "authentication" not in payload
    assert authenticator.is_authenticated(
        authenticated
    )
    assert verification.ok
    assert (
        verification.version
        == AUDIT_AUTHENTICATION_VERSION
    )
    assert (
        verification.algorithm
        == AUDIT_AUTHENTICATION_ALGORITHM
    )
    assert verification.key_id == _KEY_ID
    assert (
        verification.journal_hash
        == authenticated["integrity"]["journal_hash"]
    )
    assert len(verification.signature) == 64

    verification_payload = verification.to_dict()

    assert verification_payload["ok"] is True
    assert verification_payload["key_id"] == _KEY_ID
    assert (
        verification_payload["signature"]
        == verification.signature
    )


def test_authentication_is_deterministic_and_idempotent() -> None:
    """Identical journals and keys produce one stable signature."""

    authenticator = ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )
    payload = _sealed_payload()

    first = authenticator.authenticate(
        payload
    )
    second = authenticator.authenticate(
        copy.deepcopy(payload)
    )
    reauthenticated = authenticator.authenticate(
        first
    )

    assert first == second
    assert reauthenticated == first


def test_rejects_secret_shorter_than_minimum() -> None:
    """Authentication keys must contain at least 32 bytes."""

    with pytest.raises(
        ValueError,
        match="at least 32 bytes",
    ):
        ExecutionAuditAuthenticator(
            "short-secret",
            key_id=_KEY_ID,
        )


def test_verify_rejects_wrong_secret() -> None:
    """A different secret cannot authenticate the journal."""

    signer = ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )
    verifier = ExecutionAuditAuthenticator(
        _ALTERNATE_SECRET,
        key_id=_KEY_ID,
    )

    authenticated = signer.authenticate(
        _sealed_payload()
    )

    with pytest.raises(
        ValueError,
        match="signature is invalid",
    ):
        verifier.verify(
            authenticated
        )


def test_verify_rejects_wrong_key_identifier() -> None:
    """The configured key identifier must match the signature."""

    signer = ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )
    verifier = ExecutionAuditAuthenticator(
        _SECRET,
        key_id="replacement-key-v2",
    )

    authenticated = signer.authenticate(
        _sealed_payload()
    )

    with pytest.raises(
        ValueError,
        match="key ID does not match",
    ):
        verifier.verify(
            authenticated
        )


def test_verify_rejects_resealed_forged_journal() -> None:
    """Recomputing SHA-256 seals cannot recreate the HMAC."""

    authenticator = ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )
    integrity = ExecutionAuditIntegrity()

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
        "Execution event was maliciously rewritten."
    )

    forged = integrity.seal(
        forged
    )
    forged["authentication"] = (
        original_authentication
    )

    integrity_verification = integrity.verify(
        {
            key: value
            for key, value in forged.items()
            if key != "authentication"
        }
    )

    assert integrity_verification.ok

    with pytest.raises(
        ValueError,
        match="journal hash does not match",
    ):
        authenticator.verify(
            forged
        )


def test_verify_rejects_missing_authentication() -> None:
    """An unsigned journal cannot pass authentication."""

    authenticator = ExecutionAuditAuthenticator(
        _SECRET,
        key_id=_KEY_ID,
    )
    payload = _sealed_payload()

    assert not authenticator.is_authenticated(
        payload
    )

    with pytest.raises(
        ValueError,
        match="no valid authentication signature",
    ):
        authenticator.verify(
            payload
        )