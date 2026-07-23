"""Persistent execution workspace storage for Aegis OS."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .audit_protection import ExecutionAuditProtection
from .session_builder import ExecutionSessionBuildResult


@dataclass(slots=True, frozen=True)
class PersistedExecutionWorkspace:
    """Paths created while persisting one execution session."""

    workspace_path: Path
    session_manifest: Path
    context_manifest: Path
    inputs_manifest: Path
    audit_manifest: Path

    def to_dict(self) -> dict[str, str]:
        """Serialize persisted workspace paths."""

        return {
            "workspace_path": str(self.workspace_path),
            "session_manifest": str(self.session_manifest),
            "context_manifest": str(self.context_manifest),
            "inputs_manifest": str(self.inputs_manifest),
            "audit_manifest": str(self.audit_manifest),
        }


@dataclass(slots=True, frozen=True)
class StoredExecutionSession:
    """One execution session loaded from persistent storage."""

    workspace_path: Path
    session_manifest: Path
    payload: dict[str, Any]

    @property
    def session_id(self) -> str:
        """Return the stored execution session identifier."""

        session = self.payload.get(
            "session",
            {},
        )

        return str(
            session.get(
                "session_id",
                "",
            )
        )

    @property
    def workspace_id(self) -> str:
        """Return the stored execution workspace identifier."""

        workspace = self.payload.get(
            "workspace",
            {},
        )

        return str(
            workspace.get(
                "workspace_id",
                "",
            )
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize the stored session record."""

        return {
            "workspace_path": str(self.workspace_path),
            "session_manifest": str(self.session_manifest),
            "session_id": self.session_id,
            "workspace_id": self.workspace_id,
            "payload": self.payload,
        }


class ExecutionWorkspaceStore:
    """Persist successful execution sessions inside the repository."""

    def __init__(
        self,
        repo_root: Path | str,
        audit_protection: ExecutionAuditProtection | None = None,
    ) -> None:
        """Initialize persistent workspace storage."""

        self.repo_root = Path(
            repo_root
        ).resolve()

        if not self.repo_root.exists():
            raise FileNotFoundError(
                "Repository root does not exist: "
                f"{self.repo_root}"
            )

        if not self.repo_root.is_dir():
            raise ValueError(
                "Repository root is not a directory: "
                f"{self.repo_root}"
            )

        self._audit_protection = (
            ExecutionAuditProtection.from_environment(
                working_directory=self.repo_root,
            )
            if audit_protection is None
            else audit_protection
        )

    def persist(
        self,
        result: ExecutionSessionBuildResult,
    ) -> PersistedExecutionWorkspace:
        """Persist one successful session and its workspace manifests."""

        if not result.ok:
            raise ValueError(
                "Only a successful execution session "
                "can be persisted."
            )

        if result.session.context is None:
            raise ValueError(
                "Execution session has no resolved "
                "context to persist."
            )

        workspace_path = self._resolve_workspace_path(
            result.workspace.logical_path
        )

        if workspace_path.exists():
            raise FileExistsError(
                "Execution workspace already exists: "
                f"{workspace_path}"
            )

        workspace_path.mkdir(
            parents=True
        )

        self._create_declared_locations(
            workspace_path=workspace_path,
            result=result,
        )

        session_manifest = (
            workspace_path
            / "session.json"
        )

        context_manifest = self._location_path(
            workspace_path=workspace_path,
            result=result,
            location_name="execution-context",
        )

        inputs_manifest = self._location_path(
            workspace_path=workspace_path,
            result=result,
            location_name="resolved-inputs",
        )

        audit_manifest = self._location_path(
            workspace_path=workspace_path,
            result=result,
            location_name="session-audit",
        )

        self._write_json(
            session_manifest,
            {
                "session": result.session.to_dict(),
                "workspace": result.workspace.to_dict(),
                "build": {
                    "ok": result.ok,
                    "errors": len(
                        result.errors
                    ),
                    "warnings": len(
                        result.warnings
                    ),
                },
            },
        )

        self._write_json(
            context_manifest,
            result.session.context.to_dict(),
        )

        self._write_json(
            inputs_manifest,
            result.context_build.input_resolution.to_dict(),
        )

        audit_payload = {
            "session_id": (
                result.session.session_id
            ),
            "workspace_id": (
                result.workspace.workspace_id
            ),
            "target_asset_id": (
                result.session.target_asset_id
            ),
            "mode": (
                result.session.mode.value
            ),
            "state": (
                result.session.state.value
            ),
            "created_at": (
                result.session.created_at.isoformat()
            ),
            "updated_at": (
                result.session.updated_at.isoformat()
            ),
            "started_at": (
                result.session.started_at.isoformat()
                if result.session.started_at
                else None
            ),
            "completed_at": (
                result.session.completed_at.isoformat()
                if result.session.completed_at
                else None
            ),
            "audit_metadata": dict(
                result.session.audit_metadata
            ),
            "event_count": 0,
            "last_event_at": None,
            "events": [],
        }

        protected_audit_payload = (
            self._audit_protection.seal(
                audit_payload
            )
        )

        self._write_json(
            audit_manifest,
            protected_audit_payload,
        )

        return PersistedExecutionWorkspace(
            workspace_path=workspace_path,
            session_manifest=session_manifest,
            context_manifest=context_manifest,
            inputs_manifest=inputs_manifest,
            audit_manifest=audit_manifest,
        )

    def load(
        self,
        identifier: str,
    ) -> StoredExecutionSession:
        """Load a stored session by workspace ID or session ID."""

        normalized_identifier = (
            identifier.strip()
        )

        if not normalized_identifier:
            raise ValueError(
                "Session or workspace identifier "
                "cannot be empty."
            )

        if (
            normalized_identifier
            in {".", ".."}
            or "/" in normalized_identifier
            or "\\" in normalized_identifier
        ):
            raise ValueError(
                "Session or workspace identifier cannot "
                "contain path separators."
            )

        workspace_root = (
            self.repo_root
            / ".aegis"
            / "workspaces"
        ).resolve()

        direct_manifest = (
            workspace_root
            / normalized_identifier
            / "session.json"
        )

        if direct_manifest.is_file():
            return self._load_record(
                direct_manifest
            )

        if workspace_root.is_dir():
            for session_manifest in sorted(
                workspace_root.glob(
                    "*/session.json"
                )
            ):
                record = self._load_record(
                    session_manifest
                )

                if (
                    record.session_id
                    == normalized_identifier
                ):
                    return record

        raise FileNotFoundError(
            "Stored execution session was not found: "
            f"{normalized_identifier}"
        )

    def _resolve_workspace_path(
        self,
        logical_path: str,
    ) -> Path:
        """Resolve and validate a repository-relative workspace path."""

        relative_path = Path(
            logical_path
        )

        if relative_path.is_absolute():
            raise ValueError(
                "Execution workspace path must "
                "be repository-relative."
            )

        if ".." in relative_path.parts:
            raise ValueError(
                "Execution workspace path cannot "
                "traverse directories."
            )

        workspace_path = (
            self.repo_root
            / relative_path
        ).resolve()

        if (
            workspace_path
            != self.repo_root
            and self.repo_root
            not in workspace_path.parents
        ):
            raise ValueError(
                "Execution workspace resolves "
                "outside the repository."
            )

        return workspace_path

    def _create_declared_locations(
        self,
        workspace_path: Path,
        result: ExecutionSessionBuildResult,
    ) -> None:
        """Create directories required by declared locations."""

        for location in result.workspace.locations:
            target = self._safe_location_path(
                workspace_path=workspace_path,
                relative_path=location.relative_path,
            )

            if target.suffix:
                target.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )
            else:
                target.mkdir(
                    parents=True,
                    exist_ok=True,
                )

    def _location_path(
        self,
        workspace_path: Path,
        result: ExecutionSessionBuildResult,
        location_name: str,
    ) -> Path:
        """Resolve one required workspace location by name."""

        location = result.workspace.get_location(
            location_name
        )

        if location is None:
            raise ValueError(
                "Required workspace location "
                f"'{location_name}' is not declared."
            )

        return self._safe_location_path(
            workspace_path=workspace_path,
            relative_path=location.relative_path,
        )

    def _safe_location_path(
        self,
        workspace_path: Path,
        relative_path: str,
    ) -> Path:
        """Resolve a location while enforcing workspace isolation."""

        target = (
            workspace_path
            / Path(
                relative_path
            )
        ).resolve()

        resolved_workspace = (
            workspace_path.resolve()
        )

        if (
            target
            != resolved_workspace
            and resolved_workspace
            not in target.parents
        ):
            raise ValueError(
                "Workspace location resolves outside "
                "the execution workspace."
            )

        return target

    def _load_record(
        self,
        session_manifest: Path,
    ) -> StoredExecutionSession:
        """Load and validate one persisted session manifest."""

        try:
            payload = json.loads(
                session_manifest.read_text(
                    encoding="utf-8"
                )
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                "Stored execution session contains "
                "invalid JSON: "
                f"{session_manifest}"
            ) from exc

        if not isinstance(
            payload,
            dict,
        ):
            raise ValueError(
                "Stored execution session must "
                "contain a JSON object."
            )

        session = payload.get(
            "session"
        )

        workspace = payload.get(
            "workspace"
        )

        if (
            not isinstance(
                session,
                dict,
            )
            or not session.get(
                "session_id"
            )
        ):
            raise ValueError(
                "Stored execution session has "
                "no valid session ID."
            )

        if (
            not isinstance(
                workspace,
                dict,
            )
            or not workspace.get(
                "workspace_id"
            )
        ):
            raise ValueError(
                "Stored execution session has "
                "no valid workspace ID."
            )

        return StoredExecutionSession(
            workspace_path=(
                session_manifest.parent
            ),
            session_manifest=session_manifest,
            payload=payload,
        )

    def _write_json(
        self,
        path: Path,
        payload: dict[str, Any],
    ) -> None:
        """Write one UTF-8 JSON manifest."""

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            json.dumps(
                payload,
                indent=2,
                ensure_ascii=False,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )