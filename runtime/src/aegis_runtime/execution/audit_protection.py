"""Unified cryptographic protection for execution audit journals."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Self

from .audit_authentication import (
    ExecutionAuditAuthenticationVerification,
    ExecutionAuditAuthenticator,
)
from .audit_authentication_config import (
    ExecutionAuditAuthenticationConfig,
)
from .audit_integrity import (
    ExecutionAuditIntegrity,
    ExecutionAuditIntegrityVerification,
)

_AUTHENTICATION_FIELD = "authentication"


@dataclass(slots=True, frozen=True)
class ExecutionAuditProtectionVerification:
    """Successful verification of one protected audit journal."""

    integrity: ExecutionAuditIntegrityVerification
    authentication: (
        ExecutionAuditAuthenticationVerification
        | None
    )

    @property
    def ok(self) -> bool:
        """Return whether all applicable checks succeeded."""

        return (
            self.integrity.ok
            and (
                self.authentication is None
                or self.authentication.ok
            )
        )

    @property
    def authenticated(self) -> bool:
        """Return whether HMAC authentication was verified."""

        return self.authentication is not None

    def to_dict(self) -> dict[str, Any]:
        """Serialize the complete protection verification."""

        return {
            "ok": self.ok,
            "authenticated": self.authenticated,
            "integrity": self.integrity.to_dict(),
            "authentication": (
                self.authentication.to_dict()
                if self.authentication is not None
                else None
            ),
        }


class ExecutionAuditProtection:
    """Seal and verify audit journals with SHA-256 and HMAC."""

    def __init__(
        self,
        authenticator: ExecutionAuditAuthenticator | None = None,
    ) -> None:
        """Initialize cryptographic audit protection."""

        self._integrity = ExecutionAuditIntegrity()
        self._authenticator = authenticator

    @classmethod
    def from_environment(
        cls,
        *,
        required: bool = False,
        environ: Mapping[str, str] | None = None,
        working_directory: Path | str | None = None,
    ) -> Self:
        """Build protection from non-persistent environment settings."""

        config = (
            ExecutionAuditAuthenticationConfig.from_environment(
                required=required,
                environ=environ,
                working_directory=working_directory,
            )
        )

        authenticator = (
            config.build_authenticator()
            if config is not None
            else None
        )

        return cls(
            authenticator=authenticator
        )

    @property
    def authentication_configured(self) -> bool:
        """Return whether an HMAC key is configured."""

        return self._authenticator is not None

    @property
    def authentication_key_id(self) -> str | None:
        """Return the configured public key identifier."""

        if self._authenticator is None:
            return None

        return self._authenticator.key_id

    def seal(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Return a cryptographically protected journal copy."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be a JSON object."
            )

        declares_authentication = (
            _AUTHENTICATION_FIELD in payload
        )

        if (
            declares_authentication
            and self._authenticator is None
        ):
            raise ValueError(
                "Execution audit authentication cannot be "
                "replaced or removed because no HMAC key "
                "is configured."
            )

        sealed_payload = self._integrity.seal(
            payload
        )

        if self._authenticator is None:
            return sealed_payload

        return self._authenticator.authenticate(
            sealed_payload
        )

    def verify(
        self,
        payload: dict[str, Any],
        *,
        require_authentication: bool | None = None,
    ) -> ExecutionAuditProtectionVerification:
        """Verify integrity and applicable HMAC authentication."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be a JSON object."
            )

        integrity_verification = self._integrity.verify(
            payload
        )

        declares_authentication = (
            _AUTHENTICATION_FIELD in payload
        )
        authentication_payload = payload.get(
            _AUTHENTICATION_FIELD
        )

        if (
            declares_authentication
            and not isinstance(authentication_payload, dict)
        ):
            raise ValueError(
                "Execution audit authentication metadata "
                "must be a JSON object."
            )

        authentication_required = (
            self.authentication_configured
            if require_authentication is None
            else require_authentication
        )

        if not declares_authentication:
            if authentication_required:
                raise ValueError(
                    "Execution audit authentication is required "
                    "but the journal is unsigned."
                )

            return ExecutionAuditProtectionVerification(
                integrity=integrity_verification,
                authentication=None,
            )

        if self._authenticator is None:
            raise ValueError(
                "Execution audit authentication cannot be "
                "verified because no HMAC key is configured."
            )

        authentication_verification = (
            self._authenticator.verify(
                payload
            )
        )

        return ExecutionAuditProtectionVerification(
            integrity=integrity_verification,
            authentication=authentication_verification,
        )