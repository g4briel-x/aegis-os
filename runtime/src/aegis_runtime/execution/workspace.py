"""Execution workspace models for the Aegis OS runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import PurePosixPath
from typing import Any
from uuid import uuid4


class ExecutionWorkspaceState(StrEnum):
    """Supported logical workspace lifecycle states."""

    DECLARED = "declared"
    READY = "ready"
    SEALED = "sealed"
    RELEASED = "released"


def normalize_workspace_path(relative_path: str) -> str:
    """Validate and normalize a logical workspace-relative path."""

    value = relative_path.strip().replace("\\", "/")

    if not value:
        raise ValueError(
            "Workspace-relative path cannot be empty."
        )

    path = PurePosixPath(value)

    if path.is_absolute():
        raise ValueError(
            "Workspace location must use a relative path."
        )

    if ".." in path.parts:
        raise ValueError(
            "Workspace location cannot traverse parent directories."
        )

    if path.parts and path.parts[0].endswith(":"):
        raise ValueError(
            "Workspace location cannot use a drive-qualified path."
        )

    return path.as_posix()


@dataclass(slots=True)
class WorkspaceLocation:
    """One reserved logical location inside an execution workspace."""

    name: str
    relative_path: str
    purpose: str = ""
    writable: bool = False
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        self.name = self.name.strip()

        if not self.name:
            raise ValueError(
                "Workspace location name cannot be empty."
            )

        self.relative_path = normalize_workspace_path(
            self.relative_path
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize the logical workspace location."""

        return {
            "name": self.name,
            "relative_path": self.relative_path,
            "purpose": self.purpose,
            "writable": self.writable,
            "metadata": dict(self.metadata),
        }


@dataclass(slots=True)
class ExecutionWorkspace:
    """Logical isolated workspace assigned to one execution session."""

    session_id: str
    workspace_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    state: ExecutionWorkspaceState = (
        ExecutionWorkspaceState.DECLARED
    )
    root_path: str = ".aegis/workspaces"
    isolation_key: str = ""
    locations: list[WorkspaceLocation] = field(
        default_factory=list
    )
    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def __post_init__(self) -> None:
        self.session_id = self.session_id.strip()

        if not self.session_id:
            raise ValueError(
                "Execution workspace requires a session ID."
            )

        self.root_path = normalize_workspace_path(
            self.root_path
        )

        if not self.isolation_key:
            self.isolation_key = self.session_id

    @property
    def logical_path(self) -> str:
        """Return the complete logical workspace path."""

        return (
            PurePosixPath(self.root_path)
            / self.workspace_id
        ).as_posix()

    @property
    def is_terminal(self) -> bool:
        """Return whether the workspace can no longer be modified."""

        return self.state in {
            ExecutionWorkspaceState.SEALED,
            ExecutionWorkspaceState.RELEASED,
        }

    def add_location(
        self,
        location: WorkspaceLocation,
    ) -> None:
        """Reserve a logical location inside the workspace."""

        if self.is_terminal:
            raise ValueError(
                "A sealed or released workspace cannot be modified."
            )

        existing_names = {
            item.name
            for item in self.locations
        }

        existing_paths = {
            item.relative_path
            for item in self.locations
        }

        if location.name in existing_names:
            raise ValueError(
                f"Workspace location '{location.name}' "
                "is already declared."
            )

        if location.relative_path in existing_paths:
            raise ValueError(
                f"Workspace path '{location.relative_path}' "
                "is already reserved."
            )

        self.locations.append(location)

    def get_location(
        self,
        name: str,
    ) -> WorkspaceLocation | None:
        """Return one workspace location by name."""

        for location in self.locations:
            if location.name == name:
                return location

        return None

    def mark_ready(self) -> None:
        """Mark the logical workspace as ready."""

        if self.state != ExecutionWorkspaceState.DECLARED:
            raise ValueError(
                "Only a declared workspace can become ready."
            )

        self.state = ExecutionWorkspaceState.READY

    def seal(self) -> None:
        """Prevent further logical workspace modifications."""

        if self.state == ExecutionWorkspaceState.RELEASED:
            raise ValueError(
                "A released workspace cannot be sealed."
            )

        self.state = ExecutionWorkspaceState.SEALED

    def release(self) -> None:
        """Mark the workspace as released."""

        self.state = ExecutionWorkspaceState.RELEASED

    def to_dict(self) -> dict[str, Any]:
        """Serialize the execution workspace."""

        return {
            "workspace_id": self.workspace_id,
            "session_id": self.session_id,
            "state": self.state.value,
            "root_path": self.root_path,
            "logical_path": self.logical_path,
            "isolation_key": self.isolation_key,
            "locations": [
                location.to_dict()
                for location in self.locations
            ],
            "metadata": dict(self.metadata),
        }