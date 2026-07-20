"""Tests for execution audit authentication configuration."""

from __future__ import annotations

from pathlib import Path

import pytest

from aegis_runtime.execution.audit_authentication import (
    AUDIT_AUTHENTICATION_ALGORITHM,
)
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


def test_resolves_secret_from_environment() -> None:
    """A direct environment secret produces valid configuration."""

    environment = {
        AUDIT_HMAC_SECRET_ENV: _SECRET,
        AUDIT_HMAC_KEY_ID_ENV: "environment-key-v1",
    }

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ=environment,
        )
    )

    assert config is not None
    assert config.secret == _SECRET.encode("utf-8")
    assert config.key_id == "environment-key-v1"
    assert config.source == AUDIT_HMAC_SECRET_ENV

    metadata = config.to_dict()

    assert metadata == {
        "enabled": True,
        "algorithm": AUDIT_AUTHENTICATION_ALGORITHM,
        "key_id": "environment-key-v1",
        "source": AUDIT_HMAC_SECRET_ENV,
    }
    assert "secret" not in metadata
    assert _SECRET not in repr(config)


def test_resolves_secret_from_relative_file(
    tmp_path: Path,
) -> None:
    """A relative secret file is resolved from the working directory."""

    secret_path = (
        tmp_path
        / "secrets"
        / "audit-hmac.key"
    )
    secret_path.parent.mkdir(
        parents=True
    )
    secret_path.write_bytes(
        _SECRET.encode("utf-8")
        + b"\r\n"
    )

    environment = {
        AUDIT_HMAC_SECRET_FILE_ENV: (
            "secrets/audit-hmac.key"
        ),
        AUDIT_HMAC_KEY_ID_ENV: "file-key-v1",
    }

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ=environment,
            working_directory=tmp_path,
        )
    )

    assert config is not None
    assert config.secret == _SECRET.encode("utf-8")
    assert config.key_id == "file-key-v1"
    assert config.source == str(
        secret_path.resolve()
    )


def test_uses_default_key_identifier() -> None:
    """The default key identifier is used when none is supplied."""

    environment = {
        AUDIT_HMAC_SECRET_ENV: _SECRET,
    }

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ=environment,
        )
    )

    assert config is not None
    assert config.key_id == AUDIT_HMAC_DEFAULT_KEY_ID


def test_returns_none_when_authentication_is_optional() -> None:
    """Missing configuration is accepted in optional mode."""

    config = (
        ExecutionAuditAuthenticationConfig.from_environment(
            required=False,
            environ={},
        )
    )

    assert config is None


def test_rejects_missing_required_configuration() -> None:
    """Required authentication needs an environment or file secret."""

    with pytest.raises(
        ValueError,
        match="authentication is required",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ={},
        )


def test_rejects_ambiguous_secret_sources(
    tmp_path: Path,
) -> None:
    """Direct and file-based secrets cannot be enabled together."""

    secret_path = tmp_path / "audit-hmac.key"
    secret_path.write_text(
        _SECRET,
        encoding="utf-8",
    )

    environment = {
        AUDIT_HMAC_SECRET_ENV: _SECRET,
        AUDIT_HMAC_SECRET_FILE_ENV: str(
            secret_path
        ),
    }

    with pytest.raises(
        ValueError,
        match="not both",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ=environment,
        )


def test_rejects_missing_secret_file(
    tmp_path: Path,
) -> None:
    """A configured secret file must exist."""

    environment = {
        AUDIT_HMAC_SECRET_FILE_ENV: (
            "missing-audit-hmac.key"
        ),
    }

    with pytest.raises(
        FileNotFoundError,
        match="secret file does not exist",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ=environment,
            working_directory=tmp_path,
        )


def test_rejects_short_secret_from_environment() -> None:
    """Environment secrets must satisfy the minimum key length."""

    environment = {
        AUDIT_HMAC_SECRET_ENV: "short-secret",
    }

    with pytest.raises(
        ValueError,
        match="at least 32 bytes",
    ):
        ExecutionAuditAuthenticationConfig.from_environment(
            required=True,
            environ=environment,
        )