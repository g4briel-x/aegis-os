"""Configuration discovery for execution audit authentication."""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Self

from .audit_authentication import (
    AUDIT_AUTHENTICATION_ALGORITHM,
    ExecutionAuditAuthenticator,
)

AUDIT_HMAC_SECRET_ENV = "AEGIS_AUDIT_HMAC_SECRET"
AUDIT_HMAC_SECRET_FILE_ENV = "AEGIS_AUDIT_HMAC_SECRET_FILE"
AUDIT_HMAC_KEY_ID_ENV = "AEGIS_AUDIT_HMAC_KEY_ID"
AUDIT_HMAC_DEFAULT_KEY_ID = "default"


@dataclass(slots=True, frozen=True)
class ExecutionAuditAuthenticationConfig:
    """Resolved non-persistent audit authentication settings."""

    secret: bytes = field(
        repr=False
    )
    key_id: str
    source: str

    def __post_init__(self) -> None:
        """Validate resolved authentication settings."""

        if not isinstance(self.secret, bytes):
            raise ValueError(
                "Execution audit authentication secret "
                "must be bytes."
            )

        if (
            not isinstance(self.source, str)
            or not self.source.strip()
        ):
            raise ValueError(
                "Execution audit authentication source "
                "must be non-empty text."
            )

        ExecutionAuditAuthenticator(
            self.secret,
            key_id=self.key_id,
        )

    @classmethod
    def from_environment(
        cls,
        *,
        required: bool = False,
        environ: Mapping[str, str] | None = None,
        working_directory: Path | str | None = None,
    ) -> Self | None:
        """Resolve authentication configuration from environment."""

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
        key_id_value = environment.get(
            AUDIT_HMAC_KEY_ID_ENV,
            AUDIT_HMAC_DEFAULT_KEY_ID,
        )

        has_direct_secret = (
            direct_secret is not None
            and direct_secret != ""
        )
        has_secret_file = (
            secret_file_value is not None
            and bool(secret_file_value.strip())
        )

        if has_direct_secret and has_secret_file:
            raise ValueError(
                "Execution audit authentication must use "
                f"either {AUDIT_HMAC_SECRET_ENV} or "
                f"{AUDIT_HMAC_SECRET_FILE_ENV}, not both."
            )

        if not has_direct_secret and not has_secret_file:
            if required:
                raise ValueError(
                    "Execution audit authentication is required. "
                    f"Set {AUDIT_HMAC_SECRET_ENV} or "
                    f"{AUDIT_HMAC_SECRET_FILE_ENV}."
                )

            return None

        key_id = (
            key_id_value.strip()
            if isinstance(key_id_value, str)
            else ""
        )

        if not key_id:
            key_id = AUDIT_HMAC_DEFAULT_KEY_ID

        if has_direct_secret:
            assert direct_secret is not None

            return cls(
                secret=direct_secret.encode(
                    "utf-8"
                ),
                key_id=key_id,
                source=AUDIT_HMAC_SECRET_ENV,
            )

        assert secret_file_value is not None

        secret_path = cls._resolve_secret_path(
            secret_file_value,
            working_directory=working_directory,
        )
        secret = cls._read_secret_file(
            secret_path
        )

        return cls(
            secret=secret,
            key_id=key_id,
            source=str(secret_path),
        )

    def build_authenticator(
        self,
    ) -> ExecutionAuditAuthenticator:
        """Build an authenticator from the resolved secret."""

        return ExecutionAuditAuthenticator(
            self.secret,
            key_id=self.key_id,
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize only non-secret configuration metadata."""

        return {
            "enabled": True,
            "algorithm": AUDIT_AUTHENTICATION_ALGORITHM,
            "key_id": self.key_id,
            "source": self.source,
        }

    @staticmethod
    def _resolve_secret_path(
        value: str,
        *,
        working_directory: Path | str | None,
    ) -> Path:
        """Resolve one secret file path safely."""

        path = Path(
            value.strip()
        ).expanduser()

        if not path.is_absolute():
            base = (
                Path(working_directory)
                if working_directory is not None
                else Path.cwd()
            )

            path = base / path

        path = path.resolve()

        if not path.exists():
            raise FileNotFoundError(
                "Execution audit authentication secret "
                f"file does not exist: {path}"
            )

        if not path.is_file():
            raise ValueError(
                "Execution audit authentication secret "
                f"path is not a file: {path}"
            )

        return path

    @staticmethod
    def _read_secret_file(
        path: Path,
    ) -> bytes:
        """Read secret bytes without retaining a trailing newline."""

        try:
            secret = path.read_bytes()
        except OSError as exc:
            raise OSError(
                "Unable to read execution audit "
                f"authentication secret file: {path}"
            ) from exc

        return secret.rstrip(
            b"\r\n"
        )