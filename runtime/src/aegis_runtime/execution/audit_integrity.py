"""Cryptographic integrity protection for execution audit journals."""

from __future__ import annotations

import copy
import hashlib
import hmac
import json
from dataclasses import dataclass
from typing import Any


AUDIT_INTEGRITY_VERSION = 1
AUDIT_INTEGRITY_ALGORITHM = "sha256"
AUDIT_GENESIS_HASH = "0" * 64

_INTEGRITY_FIELD = "integrity"
_AUTHENTICATION_FIELD = "authentication"

_INTEGRITY_KEYS = {
    "version",
    "algorithm",
    "event_count",
    "genesis_hash",
    "root_hash",
    "manifest_hash",
    "journal_hash",
    "entries",
}

_ENTRY_KEYS = {
    "index",
    "event_id",
    "previous_hash",
    "event_hash",
}


@dataclass(slots=True, frozen=True)
class ExecutionAuditIntegrityVerification:
    """Successful verification result for one audit journal."""

    version: int
    algorithm: str
    event_count: int
    root_hash: str
    manifest_hash: str
    journal_hash: str

    @property
    def ok(self) -> bool:
        """Return whether integrity verification succeeded."""

        return True

    def to_dict(self) -> dict[str, Any]:
        """Serialize the integrity verification result."""

        return {
            "ok": self.ok,
            "version": self.version,
            "algorithm": self.algorithm,
            "event_count": self.event_count,
            "root_hash": self.root_hash,
            "manifest_hash": self.manifest_hash,
            "journal_hash": self.journal_hash,
        }


class ExecutionAuditIntegrity:
    """Seal and verify immutable execution audit journals."""

    def seal(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Return a sealed copy of one audit manifest."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be a JSON object."
            )

        sealed_payload = copy.deepcopy(
            payload
        )

        sealed_payload.pop(
            _INTEGRITY_FIELD,
            None,
        )
        sealed_payload.pop(
            _AUTHENTICATION_FIELD,
            None,
        )

        sealed_payload[_INTEGRITY_FIELD] = (
            self._build_integrity(
                sealed_payload
            )
        )

        return sealed_payload

    def verify(
        self,
        payload: dict[str, Any],
    ) -> ExecutionAuditIntegrityVerification:
        """Verify one sealed execution audit manifest."""

        if not isinstance(payload, dict):
            raise ValueError(
                "Execution audit payload must be a JSON object."
            )

        integrity = payload.get(
            _INTEGRITY_FIELD
        )

        if not isinstance(integrity, dict):
            raise ValueError(
                "Execution audit manifest has no valid "
                "integrity seal."
            )

        unexpected_keys = (
            set(integrity)
            - _INTEGRITY_KEYS
        )
        missing_keys = (
            _INTEGRITY_KEYS
            - set(integrity)
        )

        if missing_keys:
            names = ", ".join(
                sorted(missing_keys)
            )

            raise ValueError(
                "Execution audit integrity seal is missing "
                f"required fields: {names}"
            )

        if unexpected_keys:
            names = ", ".join(
                sorted(unexpected_keys)
            )

            raise ValueError(
                "Execution audit integrity seal contains "
                f"unsupported fields: {names}"
            )

        version = integrity.get(
            "version"
        )

        if (
            isinstance(version, bool)
            or not isinstance(version, int)
            or version != AUDIT_INTEGRITY_VERSION
        ):
            raise ValueError(
                "Unsupported execution audit integrity version."
            )

        algorithm = integrity.get(
            "algorithm"
        )

        if algorithm != AUDIT_INTEGRITY_ALGORITHM:
            raise ValueError(
                "Unsupported execution audit integrity algorithm."
            )

        stored_event_count = integrity.get(
            "event_count"
        )

        if (
            isinstance(stored_event_count, bool)
            or not isinstance(stored_event_count, int)
            or stored_event_count < 0
        ):
            raise ValueError(
                "Execution audit integrity event count "
                "must be a non-negative integer."
            )

        stored_genesis_hash = self._required_hash(
            integrity,
            "genesis_hash",
            "execution audit integrity seal",
        )
        stored_root_hash = self._required_hash(
            integrity,
            "root_hash",
            "execution audit integrity seal",
        )
        stored_manifest_hash = self._required_hash(
            integrity,
            "manifest_hash",
            "execution audit integrity seal",
        )
        stored_journal_hash = self._required_hash(
            integrity,
            "journal_hash",
            "execution audit integrity seal",
        )

        if not hmac.compare_digest(
            stored_genesis_hash,
            AUDIT_GENESIS_HASH,
        ):
            raise ValueError(
                "Execution audit integrity genesis hash "
                "is invalid."
            )

        stored_entries = integrity.get(
            "entries"
        )

        if not isinstance(stored_entries, list):
            raise ValueError(
                "Execution audit integrity entries "
                "must be a JSON array."
            )

        protected_payload = self._protected_payload(
            payload
        )

        expected_integrity = self._build_integrity(
            protected_payload
        )

        expected_event_count = expected_integrity[
            "event_count"
        ]

        if stored_event_count != expected_event_count:
            raise ValueError(
                "Execution audit integrity event count "
                "does not match the journal."
            )

        self._verify_entries(
            stored_entries=stored_entries,
            expected_entries=expected_integrity["entries"],
        )

        self._compare_hash(
            stored_root_hash,
            expected_integrity["root_hash"],
            "root hash",
        )
        self._compare_hash(
            stored_manifest_hash,
            expected_integrity["manifest_hash"],
            "manifest hash",
        )
        self._compare_hash(
            stored_journal_hash,
            expected_integrity["journal_hash"],
            "journal hash",
        )

        return ExecutionAuditIntegrityVerification(
            version=version,
            algorithm=algorithm,
            event_count=stored_event_count,
            root_hash=stored_root_hash,
            manifest_hash=stored_manifest_hash,
            journal_hash=stored_journal_hash,
        )

    def is_sealed(
        self,
        payload: dict[str, Any],
    ) -> bool:
        """Return whether a payload declares an integrity seal."""

        return isinstance(
            payload.get(_INTEGRITY_FIELD),
            dict,
        )

    def _build_integrity(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Build one deterministic journal integrity seal."""

        session_id = self._required_string(
            payload,
            "session_id",
            "execution audit manifest",
        )
        workspace_id = self._required_string(
            payload,
            "workspace_id",
            "execution audit manifest",
        )
        events = self._events(
            payload
        )

        previous_hash = AUDIT_GENESIS_HASH
        entries: list[dict[str, Any]] = []
        event_ids: set[str] = set()

        for index, event in enumerate(events):
            event_id = self._required_string(
                event,
                "event_id",
                (
                    "execution audit event "
                    f"at index {index}"
                ),
            )

            if event_id in event_ids:
                raise ValueError(
                    "Execution audit event IDs "
                    "must be unique."
                )

            event_ids.add(
                event_id
            )

            event_material = {
                "index": index,
                "previous_hash": previous_hash,
                "event": event,
            }

            event_hash = self._hash_value(
                event_material
            )

            entries.append(
                {
                    "index": index,
                    "event_id": event_id,
                    "previous_hash": previous_hash,
                    "event_hash": event_hash,
                }
            )

            previous_hash = event_hash

        root_hash = previous_hash

        protected_payload = self._protected_payload(
            payload
        )

        manifest_hash = self._hash_value(
            protected_payload
        )

        journal_material = {
            "version": AUDIT_INTEGRITY_VERSION,
            "algorithm": AUDIT_INTEGRITY_ALGORITHM,
            "session_id": session_id,
            "workspace_id": workspace_id,
            "event_count": len(events),
            "genesis_hash": AUDIT_GENESIS_HASH,
            "root_hash": root_hash,
            "manifest_hash": manifest_hash,
        }

        journal_hash = self._hash_value(
            journal_material
        )

        return {
            "version": AUDIT_INTEGRITY_VERSION,
            "algorithm": AUDIT_INTEGRITY_ALGORITHM,
            "event_count": len(events),
            "genesis_hash": AUDIT_GENESIS_HASH,
            "root_hash": root_hash,
            "manifest_hash": manifest_hash,
            "journal_hash": journal_hash,
            "entries": entries,
        }

    def _verify_entries(
        self,
        *,
        stored_entries: list[Any],
        expected_entries: list[dict[str, Any]],
    ) -> None:
        """Verify every stored event-chain entry."""

        if len(stored_entries) != len(expected_entries):
            raise ValueError(
                "Execution audit integrity entry count "
                "does not match the journal."
            )

        for index, (
            stored_entry,
            expected_entry,
        ) in enumerate(
            zip(
                stored_entries,
                expected_entries,
                strict=True,
            )
        ):
            if not isinstance(stored_entry, dict):
                raise ValueError(
                    "Execution audit integrity entry "
                    f"at index {index} must be a JSON object."
                )

            unexpected_keys = (
                set(stored_entry)
                - _ENTRY_KEYS
            )
            missing_keys = (
                _ENTRY_KEYS
                - set(stored_entry)
            )

            if missing_keys:
                names = ", ".join(
                    sorted(missing_keys)
                )

                raise ValueError(
                    "Execution audit integrity entry "
                    f"at index {index} is missing: {names}"
                )

            if unexpected_keys:
                names = ", ".join(
                    sorted(unexpected_keys)
                )

                raise ValueError(
                    "Execution audit integrity entry "
                    f"at index {index} contains unsupported "
                    f"fields: {names}"
                )

            stored_index = stored_entry.get(
                "index"
            )

            if (
                isinstance(stored_index, bool)
                or not isinstance(stored_index, int)
                or stored_index != index
            ):
                raise ValueError(
                    "Execution audit integrity entry index "
                    f"is invalid at position {index}."
                )

            stored_event_id = self._required_string(
                stored_entry,
                "event_id",
                (
                    "execution audit integrity entry "
                    f"at index {index}"
                ),
            )

            if stored_event_id != expected_entry["event_id"]:
                raise ValueError(
                    "Execution audit integrity event ID "
                    f"mismatch at index {index}."
                )

            stored_previous_hash = self._required_hash(
                stored_entry,
                "previous_hash",
                (
                    "execution audit integrity entry "
                    f"at index {index}"
                ),
            )
            stored_event_hash = self._required_hash(
                stored_entry,
                "event_hash",
                (
                    "execution audit integrity entry "
                    f"at index {index}"
                ),
            )

            self._compare_hash(
                stored_previous_hash,
                expected_entry["previous_hash"],
                (
                    "previous event hash "
                    f"at index {index}"
                ),
            )
            self._compare_hash(
                stored_event_hash,
                expected_entry["event_hash"],
                (
                    "event hash "
                    f"at index {index}"
                ),
            )

    def _events(
        self,
        payload: dict[str, Any],
    ) -> list[dict[str, Any]]:
        """Read and validate the audit event collection."""

        raw_events = payload.get(
            "events",
            [],
        )

        if not isinstance(raw_events, list):
            raise ValueError(
                "Execution audit events must "
                "be a JSON array."
            )

        events: list[dict[str, Any]] = []

        for index, event in enumerate(
            raw_events
        ):
            if not isinstance(event, dict):
                raise ValueError(
                    "Execution audit event "
                    f"at index {index} must be a JSON object."
                )

            events.append(
                copy.deepcopy(event)
            )

        return events

    def _protected_payload(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Return the manifest without cryptographic metadata."""

        protected_payload = copy.deepcopy(
            payload
        )

        protected_payload.pop(
            _INTEGRITY_FIELD,
            None,
        )
        protected_payload.pop(
            _AUTHENTICATION_FIELD,
            None,
        )

        return protected_payload

    def _hash_value(
        self,
        value: Any,
    ) -> str:
        """Hash one canonical JSON value with SHA-256."""

        canonical = self._canonical_json(
            value
        )

        return hashlib.sha256(
            canonical.encode("utf-8")
        ).hexdigest()

    def _canonical_json(
        self,
        value: Any,
    ) -> str:
        """Serialize one value as deterministic canonical JSON."""

        try:
            return json.dumps(
                value,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
        except (
            TypeError,
            ValueError,
        ) as exc:
            raise ValueError(
                "Execution audit data cannot be "
                "serialized as canonical JSON."
            ) from exc

    def _compare_hash(
        self,
        stored_hash: str,
        expected_hash: str,
        description: str,
    ) -> None:
        """Compare two SHA-256 hashes safely."""

        if not hmac.compare_digest(
            stored_hash,
            expected_hash,
        ):
            raise ValueError(
                "Execution audit integrity "
                f"{description} mismatch."
            )

    def _required_hash(
        self,
        payload: dict[str, Any],
        field_name: str,
        description: str,
    ) -> str:
        """Read one required lowercase SHA-256 hash."""

        value = payload.get(
            field_name
        )

        if (
            not isinstance(value, str)
            or len(value) != 64
            or value.lower() != value
            or any(
                character not in "0123456789abcdef"
                for character in value
            )
        ):
            raise ValueError(
                f"{description} requires a valid "
                f"'{field_name}' SHA-256 hash."
            )

        return value

    def _required_string(
        self,
        payload: dict[str, Any],
        field_name: str,
        description: str,
    ) -> str:
        """Read one required non-empty string."""

        value = payload.get(
            field_name
        )

        if (
            not isinstance(value, str)
            or not value.strip()
        ):
            raise ValueError(
                f"{description} requires a valid "
                f"'{field_name}' string."
            )

        return value.strip()