"""Tests for execution audit HMAC configuration."""

from __future__ import annotations

from pathlib import Path

import pytest

from aegis_runtime.execution.audit_authentication_config import (
    AUDIT_HMAC_DEFAULT_KEY_ID,
    AUDIT_HMAC_KEY_ID_ENV,
    AUDIT_HMAC_SECRET_ENV,
    AUDIT_HMAC_SECRET_FILE_ENV,
    ExecutionAuditAuthenticationConfig,
)

_SECRET = (
    "0123456789abcdef"
    "0123456789abcdef"
)

_KEY_ID = "test-configuration-key-v1"


def test_loads_secret_from_environment() -> None:
    """Direct environment configuration builds an authenticator."""

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={
                AUDIT_HMAC_SECRET_ENV: _SECRET,
                AUDIT_HMAC_KEY_ID_ENV: _KEY_ID,
            },
        )
    )

    assert config is not None
    assert config.secret == _SECRET.encode("utf-8")
    assert config.key_id == _KEY_ID
    assert config.source == (
        f"environment:{AUDIT_HMAC_SECRET_ENV}"
    )

    authenticator = config.build_authenticator()

    assert authenticator.key_id == _KEY_ID


def test_loads_secret_from_relative_file(
    tmp_path: Path,
) -> None:
    """A relative secret-file path resolves from the working directory."""

    secret_file = tmp_path / "secrets" / "audit.key"
    secret_file.parent.mkdir(parents=True)

    secret_file.write_bytes(
        _SECRET.encode("utf-8") + b"\r\n"
    )

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={
                AUDIT_HMAC_SECRET_FILE_ENV: (
                    "secrets/audit.key"
                ),
                AUDIT_HMAC_KEY_ID_ENV: _KEY_ID,
            },
            working_directory=tmp_path,
        )
    )

    assert config is not None
    assert config.secret == _SECRET.encode("utf-8")
    assert config.key_id == _KEY_ID
    assert config.source == (
        f"file:{secret_file.resolve()}"
    )


def test_uses_default_key_id() -> None:
    """Missing public key ID uses the documented default."""

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={
                AUDIT_HMAC_SECRET_ENV: _SECRET,
            },
        )
    )

    assert config is not None
    assert config.key_id == AUDIT_HMAC_DEFAULT_KEY_ID


def test_optional_configuration_returns_none() -> None:
    """No configured secret is allowed in optional mode."""

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=False,
            environ={},
        )
    )

    assert config is None


def test_required_configuration_rejects_missing_secret() -> None:
    """Mandatory HMAC mode requires secret material."""

    with pytest.raises(
        ValueError,
        match="no secret is configured",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={},
        )


def test_rejects_ambiguous_secret_sources(
    tmp_path: Path,
) -> None:
    """Direct and file-based secrets cannot be configured together."""

    secret_file = tmp_path / "audit.key"
    secret_file.write_text(
        _SECRET,
        encoding="utf-8",
    )

    with pytest.raises(
        ValueError,
        match="configured from both",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={
                AUDIT_HMAC_SECRET_ENV: _SECRET,
                AUDIT_HMAC_SECRET_FILE_ENV: str(
                    secret_file
                ),
            },
        )


def test_rejects_missing_secret_file(
    tmp_path: Path,
) -> None:
    """A configured secret file must exist."""

    missing_file = tmp_path / "missing.key"

    with pytest.raises(
        FileNotFoundError,
        match="does not exist",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={
                AUDIT_HMAC_SECRET_FILE_ENV: str(
                    missing_file
                ),
            },
        )


def test_rejects_short_secret() -> None:
    """Configuration preserves minimum HMAC key-length enforcement."""

    with pytest.raises(
        ValueError,
        match="at least 32 bytes",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={
                AUDIT_HMAC_SECRET_ENV: "too-short",
            },
        )


def test_public_serialization_does_not_expose_secret() -> None:
    """Serialized configuration contains no secret material."""

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={
                AUDIT_HMAC_SECRET_ENV: _SECRET,
                AUDIT_HMAC_KEY_ID_ENV: _KEY_ID,
            },
        )
    )

    assert config is not None

    payload = config.to_dict()
    representation = repr(config)

    assert payload == {
        "configured": True,
        "key_id": _KEY_ID,
        "source": (
            f"environment:{AUDIT_HMAC_SECRET_ENV}"
        ),
    }

    assert "secret" not in payload
    assert _SECRET not in representation
    assert _SECRET not in str(payload)