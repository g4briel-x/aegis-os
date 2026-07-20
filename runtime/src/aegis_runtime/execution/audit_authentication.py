"""HMAC authentication for execution audit journals."""

from __future__ import annotations

import copy
import hashlib
import hmac
import json
import re
from dataclasses import dataclass
from typing import Any

from .audit_integrity import (
    ExecutionAuditIntegrity,
)

AUDIT_AUTHENTICATION_VERSION = 1
AUDIT_AUTHENTICATION_ALGORITHM = "hmac-sha256"
AUDIT_AUTHENTICATION_CONTEXT = (
    "aegis.execution.audit.authentication.v1"
)
AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES = 32

_AUTHENTICATION_FIELD = "authentication"

_AUTHENTICATION_KEYS = {
    "version",
    "algorithm",
    "key_id",
    "journal_hash",
    "signature",
}

_KEY_ID_PATTERN = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"
)

_SHA256_PATTERN = re.compile(
    r"^[0-9a-f]{64}$"
)


@dataclass(slots=True, frozen=True)
class ExecutionAuditAuthenticationVerification:
    """Successful authentication result for one audit journal."""

    version: int
    algorithm: str
    key_id: str
    journal_hash: str
    signature: str

    @property
    def ok(self) -> bool:
        """Return whether authentication succeeded."""

        return True

    def to_dict(self) -> dict[str, Any]:
        """Serialize the authentication verification result."""

        return {
            "ok": self.ok,
            "version": self.version,
            "algorithm": self.algorithm,
            "key_id": self.key_id,
            "journal_hash": self.journal_hash,
            "signature": self.signature,
        }


class ExecutionAuditAuthenticator:
    """Authenticate execution audit journals with HMAC-SHA256."""

    def __init__(
        self,
        secret: str | bytes,
        *,
        key_id: str = "default",
    ) -> None:
        """Initialize one authenticator with secret key material."""

        self._secret = self._normalize_secret(
            secret
        )
        self._key_id = self._normalize_key_id(
            key_id
        )
        self._integrity = ExecutionAuditIntegrity()

    @property
    def key_id(self) -> str:
        """Return the non-secret key identifier."""

        return self._key_id

    def authenticate(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Return an authenticated copy of one sealed journal."""

        protected_payload = self._protected_payload(
            payload
        )

        integrity = self._integrity.verify(
            protected_payload
        )

        signature = self._signature(
            protected_payload,
            key_id=self._key_id,
            journal_hash=integrity.journal_hash,
        )

        authenticated_payload = copy.deepcopy(
            protected_payload
        )
        authenticated_payload[_AUTHENTICATION_FIELD] = {
            "version": AUDIT_AUTHENTICATION_VERSION,
            "algorithm": AUDIT_AUTHENTICATION_ALGORITHM,
            "key_id": self._key_id,
            "journal_hash": integrity.journal_hash,
            "signature": signature,
        }

        return authenticated_payload

    def verify(
        self,
        payload: dict[str, Any],
    ) -> ExecutionAuditAuthenticationVerification:
        """Verify one authenticated execution audit journal."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be a JSON object."
            )

        authentication = payload.get(
            _AUTHENTICATION_FIELD
        )

        if not isinstance(authentication, dict):
            raise ValueError(
                "Execution audit manifest has no valid "
                "authentication signature."
            )

        missing_keys = (
            _AUTHENTICATION_KEYS
            - set(authentication)
        )
        unexpected_keys = (
            set(authentication)
            - _AUTHENTICATION_KEYS
        )

        if missing_keys:
            names = ", ".join(
                sorted(missing_keys)
            )

            raise ValueError(
                "Execution audit authentication is missing "
                f"required fields: {names}"
            )

        if unexpected_keys:
            names = ", ".join(
                sorted(unexpected_keys)
            )

            raise ValueError(
                "Execution audit authentication contains "
                f"unsupported fields: {names}"
            )

        version = authentication.get(
            "version"
        )

        if (
            isinstance(version, bool)
            or not isinstance(version, int)
            or version != AUDIT_AUTHENTICATION_VERSION
        ):
            raise ValueError(
                "Unsupported execution audit "
                "authentication version."
            )

        algorithm = authentication.get(
            "algorithm"
        )

        if algorithm != AUDIT_AUTHENTICATION_ALGORITHM:
            raise ValueError(
                "Unsupported execution audit "
                "authentication algorithm."
            )

        key_id = self._required_key_id(
            authentication
        )

        if not hmac.compare_digest(
            key_id,
            self._key_id,
        ):
            raise ValueError(
                "Execution audit authentication key ID "
                "does not match the configured key."
            )

        stored_journal_hash = self._required_sha256(
            authentication,
            "journal_hash",
            "execution audit authentication",
        )
        stored_signature = self._required_sha256(
            authentication,
            "signature",
            "execution audit authentication",
        )

        protected_payload = self._protected_payload(
            payload
        )

        integrity = self._integrity.verify(
            protected_payload
        )

        if not hmac.compare_digest(
            stored_journal_hash,
            integrity.journal_hash,
        ):
            raise ValueError(
                "Execution audit authentication journal hash "
                "does not match the integrity seal."
            )

        expected_signature = self._signature(
            protected_payload,
            key_id=key_id,
            journal_hash=stored_journal_hash,
        )

        if not hmac.compare_digest(
            stored_signature,
            expected_signature,
        ):
            raise ValueError(
                "Execution audit authentication signature "
                "is invalid."
            )

        return ExecutionAuditAuthenticationVerification(
            version=version,
            algorithm=algorithm,
            key_id=key_id,
            journal_hash=stored_journal_hash,
            signature=stored_signature,
        )

    def is_authenticated(
        self,
        payload: dict[str, Any],
    ) -> bool:
        """Return whether a payload declares authentication."""

        return (
            isinstance(payload, dict)
            and isinstance(
                payload.get(_AUTHENTICATION_FIELD),
                dict,
            )
        )

    def _signature(
        self,
        payload: dict[str, Any],
        *,
        key_id: str,
        journal_hash: str,
    ) -> str:
        """Calculate one deterministic HMAC signature."""

        material = {
            "context": AUDIT_AUTHENTICATION_CONTEXT,
            "version": AUDIT_AUTHENTICATION_VERSION,
            "algorithm": AUDIT_AUTHENTICATION_ALGORITHM,
            "key_id": key_id,
            "journal_hash": journal_hash,
            "journal": payload,
        }

        return hmac.new(
            self._secret,
            self._canonical_bytes(material),
            hashlib.sha256,
        ).hexdigest()

    @staticmethod
    def _protected_payload(
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Return a copy without an authentication signature."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be a JSON object."
            )

        protected_payload = copy.deepcopy(
            payload
        )
        protected_payload.pop(
            _AUTHENTICATION_FIELD,
            None,
        )

        return protected_payload

    @staticmethod
    def _canonical_bytes(
        value: Any,
    ) -> bytes:
        """Serialize JSON material deterministically."""

        try:
            serialized = json.dumps(
                value,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            )
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "Execution audit authentication material "
                "must be valid deterministic JSON."
            ) from exc

        return serialized.encode(
            "utf-8"
        )

    @staticmethod
    def _normalize_secret(
        secret: str | bytes,
    ) -> bytes:
        """Validate and normalize secret key material."""

        if isinstance(secret, str):
            secret_bytes = secret.encode(
                "utf-8"
            )
        elif isinstance(secret, bytes):
            secret_bytes = secret
        else:
            raise ValueError(
                "Execution audit authentication secret "
                "must be text or bytes."
            )

        if (
            len(secret_bytes)
            < AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES
        ):
            raise ValueError(
                "Execution audit authentication secret "
                "must contain at least "
                f"{AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES} bytes."
            )

        return secret_bytes

    @staticmethod
    def _normalize_key_id(
        key_id: str,
    ) -> str:
        """Validate one public key identifier."""

        if not isinstance(key_id, str):
            raise ValueError(
                "Execution audit authentication key ID "
                "must be text."
            )

        if not _KEY_ID_PATTERN.fullmatch(
            key_id
        ):
            raise ValueError(
                "Execution audit authentication key ID must "
                "contain 1 to 128 letters, digits, dots, "
                "underscores, colons, or hyphens."
            )

        return key_id

    @staticmethod
    def _required_key_id(
        payload: dict[str, Any],
    ) -> str:
        """Read and validate one stored key identifier."""

        key_id = payload.get(
            "key_id"
        )

        if (
            not isinstance(key_id, str)
            or not _KEY_ID_PATTERN.fullmatch(key_id)
        ):
            raise ValueError(
                "Execution audit authentication key ID "
                "is invalid."
            )

        return key_id

    @staticmethod
    def _required_sha256(
        payload: dict[str, Any],
        field: str,
        context: str,
    ) -> str:
        """Read one strict lowercase SHA-256 hexadecimal value."""

        value = payload.get(
            field
        )

        if (
            not isinstance(value, str)
            or not _SHA256_PATTERN.fullmatch(value)
        ):
            raise ValueError(
                f"{context} field '{field}' must be a "
                "lowercase SHA-256 hexadecimal value."
            )

        return value