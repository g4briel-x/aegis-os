"""Configuration for execution audit HMAC authentication."""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Self

from .audit_authentication import (
    ExecutionAuditAuthenticator,
)

AUDIT_HMAC_SECRET_ENV = "AEGIS_AUDIT_HMAC_SECRET"
AUDIT_HMAC_SECRET_FILE_ENV = "AEGIS_AUDIT_HMAC_SECRET_FILE"
AUDIT_HMAC_KEY_ID_ENV = "AEGIS_AUDIT_HMAC_KEY_ID"
AUDIT_HMAC_DEFAULT_KEY_ID = "default"


@dataclass(slots=True, frozen=True)
class ExecutionAuditAuthenticationConfig:
    """Resolved non-persistent HMAC authentication configuration."""

    secret: bytes = field(
        repr=False
    )
    key_id: str
    source: str

    def __post_init__(self) -> None:
        """Normalize and validate the resolved configuration."""

        if not isinstance(
            self.secret,
            bytes,
        ):
            raise ValueError(
                "Execution audit HMAC secret "
                "must be bytes."
            )

        normalized_secret = bytes(
            self.secret
        )
        normalized_key_id = (
            self.key_id.strip()
        )
        normalized_source = (
            self.source.strip()
        )

        if not normalized_source:
            raise ValueError(
                "Execution audit HMAC configuration "
                "source cannot be empty."
            )

        # Construction performs the minimum secret-length
        # and key-ID validation in one central location.
        ExecutionAuditAuthenticator(
            normalized_secret,
            key_id=normalized_key_id,
        )

        object.__setattr__(
            self,
            "secret",
            normalized_secret,
        )
        object.__setattr__(
            self,
            "key_id",
            normalized_key_id,
        )
        object.__setattr__(
            self,
            "source",
            normalized_source,
        )

    @classmethod
    def from_environment(
        cls,
        *,
        required: bool = False,
        environ: Mapping[str, str] | None = None,
        working_directory: Path | str | None = None,
    ) -> Self | None:
        """Resolve HMAC configuration from environment settings."""

        environment = (
            os.environ
            if environ is None
            else environ
        )

        direct_secret = environment.get(
            AUDIT_HMAC_SECRET_ENV
        )
        secret_file_value = environment.get(
            AUDIT_HMAC_SECRET_FILE_ENV
        )

        direct_secret_configured = (
            direct_secret is not None
            and direct_secret != ""
        )

        secret_file_configured = (
            secret_file_value is not None
            and bool(
                secret_file_value.strip()
            )
        )

        if (
            direct_secret_configured
            and secret_file_configured
        ):
            raise ValueError(
                "Execution audit HMAC secret cannot be "
                "configured from both "
                f"{AUDIT_HMAC_SECRET_ENV} and "
                f"{AUDIT_HMAC_SECRET_FILE_ENV}."
            )

        if (
            not direct_secret_configured
            and not secret_file_configured
        ):
            if required:
                raise ValueError(
                    "Execution audit HMAC authentication "
                    "is required, but no secret is configured."
                )

            return None

        raw_key_id = environment.get(
            AUDIT_HMAC_KEY_ID_ENV
        )

        key_id = (
            AUDIT_HMAC_DEFAULT_KEY_ID
            if raw_key_id is None
            else raw_key_id
        )

        if direct_secret_configured:
            assert direct_secret is not None

            return cls(
                secret=direct_secret.encode(
                    "utf-8"
                ),
                key_id=key_id,
                source=(
                    "environment:"
                    f"{AUDIT_HMAC_SECRET_ENV}"
                ),
            )

        assert secret_file_value is not None

        base_directory = (
            Path.cwd()
            if working_directory is None
            else Path(
                working_directory
            )
        ).resolve()

        secret_file = Path(
            secret_file_value.strip()
        ).expanduser()

        if not secret_file.is_absolute():
            secret_file = (
                base_directory
                / secret_file
            )

        secret_file = secret_file.resolve()

        if not secret_file.is_file():
            raise FileNotFoundError(
                "Execution audit HMAC secret file "
                f"does not exist: {secret_file}"
            )

        # Only trailing line endings are removed.
        # Other bytes remain part of the secret.
        secret = secret_file.read_bytes().rstrip(
            b"\r\n"
        )

        return cls(
            secret=secret,
            key_id=key_id,
            source=f"file:{secret_file}",
        )

    def build_authenticator(
        self,
    ) -> ExecutionAuditAuthenticator:
        """Build an authenticator from the resolved configuration."""

        return ExecutionAuditAuthenticator(
            self.secret,
            key_id=self.key_id,
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize only non-secret configuration metadata."""

        return {
            "configured": True,
            "key_id": self.key_id,
            "source": self.source,
        }