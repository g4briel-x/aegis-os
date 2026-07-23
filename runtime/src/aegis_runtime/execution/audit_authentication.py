"""HMAC authentication for execution audit journals."""

from __future__ import annotations

import copy
import hashlib
import hmac
import json
from dataclasses import dataclass
from typing import Any

from .audit_integrity import ExecutionAuditIntegrity

AUDIT_AUTHENTICATION_VERSION = 1
AUDIT_AUTHENTICATION_ALGORITHM = "hmac-sha256"
AUDIT_AUTHENTICATION_CONTEXT = (
    "aegis.execution.audit.authentication.v1"
)
AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES = 32

_AUTHENTICATION_FIELD = "authentication"
_INTEGRITY_FIELD = "integrity"

_AUTHENTICATION_FIELDS = {
    "version",
    "algorithm",
    "context",
    "key_id",
    "journal_hash",
    "signature",
}


@dataclass(slots=True, frozen=True)
class ExecutionAuditAuthenticationVerification:
    """Successful HMAC verification result."""

    version: int
    algorithm: str
    context: str
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
            "context": self.context,
            "key_id": self.key_id,
            "journal_hash": self.journal_hash,
            "signature": self.signature,
        }


class ExecutionAuditAuthenticator:
    """Authenticate integrity-sealed journals with HMAC-SHA256."""

    __slots__ = (
        "_secret",
        "_key_id",
        "_integrity",
    )

    def __init__(
        self,
        secret: str | bytes,
        *,
        key_id: str,
    ) -> None:
        """Initialize the authenticator with secret key material."""

        secret_bytes = self._normalize_secret(
            secret
        )
        normalized_key_id = key_id.strip()

        if (
            len(secret_bytes)
            < AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES
        ):
            raise ValueError(
                "Execution audit HMAC secret must contain "
                f"at least "
                f"{AUDIT_AUTHENTICATION_MINIMUM_KEY_BYTES} "
                "bytes."
            )

        if not normalized_key_id:
            raise ValueError(
                "Execution audit HMAC key ID "
                "cannot be empty."
            )

        self._secret = secret_bytes
        self._key_id = normalized_key_id
        self._integrity = ExecutionAuditIntegrity()

    @property
    def key_id(self) -> str:
        """Return the public identifier of the configured key."""

        return self._key_id

    def authenticate(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Return an authenticated copy of an integrity-sealed journal."""

        unsigned_payload = self._unsigned_payload(
            payload
        )

        self._verify_integrity(
            unsigned_payload
        )

        journal_hash = self._journal_hash(
            unsigned_payload
        )

        signature = self._signature(
            unsigned_payload
        )

        authenticated_payload = copy.deepcopy(
            unsigned_payload
        )

        authenticated_payload[
            _AUTHENTICATION_FIELD
        ] = {
            "version": AUDIT_AUTHENTICATION_VERSION,
            "algorithm": AUDIT_AUTHENTICATION_ALGORITHM,
            "context": AUDIT_AUTHENTICATION_CONTEXT,
            "key_id": self._key_id,
            "journal_hash": journal_hash,
            "signature": signature,
        }

        return authenticated_payload

    def verify(
        self,
        payload: dict[str, Any],
    ) -> ExecutionAuditAuthenticationVerification:
        """Verify journal integrity and its HMAC signature."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be "
                "a JSON object."
            )

        authentication = payload.get(
            _AUTHENTICATION_FIELD
        )

        if not isinstance(
            authentication,
            dict,
        ):
            raise ValueError(
                "Execution audit authentication "
                "metadata is missing."
            )

        if set(authentication) != _AUTHENTICATION_FIELDS:
            raise ValueError(
                "Execution audit authentication metadata "
                "contains an invalid field set."
            )

        version = authentication.get(
            "version"
        )
        algorithm = authentication.get(
            "algorithm"
        )
        context = authentication.get(
            "context"
        )
        key_id = authentication.get(
            "key_id"
        )
        declared_journal_hash = authentication.get(
            "journal_hash"
        )
        declared_signature = authentication.get(
            "signature"
        )

        if (
            not isinstance(version, int)
            or isinstance(version, bool)
            or version != AUDIT_AUTHENTICATION_VERSION
        ):
            raise ValueError(
                "Unsupported execution audit "
                "authentication version."
            )

        if algorithm != AUDIT_AUTHENTICATION_ALGORITHM:
            raise ValueError(
                "Unsupported execution audit "
                "authentication algorithm."
            )

        if context != AUDIT_AUTHENTICATION_CONTEXT:
            raise ValueError(
                "Execution audit authentication "
                "context does not match."
            )

        if key_id != self._key_id:
            raise ValueError(
                "Execution audit authentication "
                "key ID does not match."
            )

        self._require_sha256_hex(
            declared_journal_hash,
            field_name="journal hash",
        )

        self._require_sha256_hex(
            declared_signature,
            field_name="signature",
        )

        unsigned_payload = self._unsigned_payload(
            payload
        )

        self._verify_integrity(
            unsigned_payload
        )

        actual_journal_hash = self._journal_hash(
            unsigned_payload
        )

        if not hmac.compare_digest(
            declared_journal_hash,
            actual_journal_hash,
        ):
            raise ValueError(
                "Execution audit authentication "
                "journal hash does not match."
            )

        expected_signature = self._signature(
            unsigned_payload
        )

        if not hmac.compare_digest(
            declared_signature,
            expected_signature,
        ):
            raise ValueError(
                "Execution audit HMAC signature "
                "does not match."
            )

        return ExecutionAuditAuthenticationVerification(
            version=version,
            algorithm=algorithm,
            context=context,
            key_id=key_id,
            journal_hash=declared_journal_hash,
            signature=declared_signature,
        )

    def is_authenticated(
        self,
        payload: dict[str, Any],
    ) -> bool:
        """Return whether a journal declares authentication."""

        return (
            isinstance(payload, dict)
            and isinstance(
                payload.get(
                    _AUTHENTICATION_FIELD
                ),
                dict,
            )
        )

    def _verify_integrity(
        self,
        payload: dict[str, Any],
    ) -> None:
        """Require a valid SHA-256 integrity seal."""

        verification = self._integrity.verify(
            payload
        )

        if not verification.ok:
            raise ValueError(
                "Execution audit integrity "
                "verification failed."
            )

    def _journal_hash(
        self,
        payload: dict[str, Any],
    ) -> str:
        """Read the verified journal hash."""

        integrity = payload.get(
            _INTEGRITY_FIELD
        )

        if not isinstance(
            integrity,
            dict,
        ):
            raise ValueError(
                "Execution audit integrity metadata "
                "is missing."
            )

        journal_hash = integrity.get(
            "journal_hash"
        )

        self._require_sha256_hex(
            journal_hash,
            field_name="integrity journal hash",
        )

        return journal_hash

    def _signature(
        self,
        payload: dict[str, Any],
    ) -> str:
        """Calculate the deterministic HMAC signature."""

        material = {
            "version": AUDIT_AUTHENTICATION_VERSION,
            "algorithm": AUDIT_AUTHENTICATION_ALGORITHM,
            "context": AUDIT_AUTHENTICATION_CONTEXT,
            "key_id": self._key_id,
            "journal": payload,
        }

        serialized = json.dumps(
            material,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode(
            "utf-8"
        )

        return hmac.new(
            self._secret,
            serialized,
            hashlib.sha256,
        ).hexdigest()

    def _unsigned_payload(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Return a copy without authentication metadata."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be "
                "a JSON object."
            )

        unsigned_payload = copy.deepcopy(
            payload
        )

        unsigned_payload.pop(
            _AUTHENTICATION_FIELD,
            None,
        )

        return unsigned_payload

    def _normalize_secret(
        self,
        secret: str | bytes,
    ) -> bytes:
        """Normalize secret material into bytes."""

        if isinstance(secret, str):
            return secret.encode(
                "utf-8"
            )

        if isinstance(secret, bytes):
            return bytes(
                secret
            )

        raise ValueError(
            "Execution audit HMAC secret must "
            "be text or bytes."
        )

    def _require_sha256_hex(
        self,
        value: Any,
        *,
        field_name: str,
    ) -> None:
        """Require one lowercase 64-character SHA-256 value."""

        if (
            not isinstance(value, str)
            or len(value) != 64
            or any(
                character
                not in "0123456789abcdef"
                for character in value
            )
        ):
            raise ValueError(
                "Execution audit authentication "
                f"{field_name} is invalid."
            )