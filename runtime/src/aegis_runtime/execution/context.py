"""Execution context models for the Aegis OS runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .models import ExecutionMode


@dataclass(slots=True)
class ResolvedExecutionInput:
    """One contract input resolved for an execution context."""

    name: str
    value: Any
    source: str
    required: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "value": self.value,
            "source": self.source,
            "required": self.required,
        }


@dataclass(slots=True)
class ExecutionEnvironment:
    """Metadata describing the environment of an execution."""

    name: str = "local"
    working_directory: str = ""
    python_version: str = ""
    platform: str = ""
    variables: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "working_directory": self.working_directory,
            "python_version": self.python_version,
            "platform": self.platform,
            "variables": dict(self.variables),
        }


@dataclass(slots=True)
class ExecutionArtifact:
    """One artifact declared or produced by an execution."""

    name: str
    artifact_type: str
    location: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "artifact_type": self.artifact_type,
            "location": self.location,
            "metadata": dict(self.metadata),
        }


@dataclass(slots=True)
class ExecutionContext:
    """Resolved runtime context for one Aegis asset execution."""

    target_asset_id: str
    mode: ExecutionMode
    parameters: dict[str, Any] = field(default_factory=dict)
    resolved_inputs: list[ResolvedExecutionInput] = field(default_factory=list)
    environment: ExecutionEnvironment = field(default_factory=ExecutionEnvironment)
    artifacts: list[ExecutionArtifact] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def input_values(self) -> dict[str, Any]:
        """Return resolved inputs as a name-to-value mapping."""

        return {
            resolved_input.name: resolved_input.value
            for resolved_input in self.resolved_inputs
        }

    def get_input(self, name: str, default: Any = None) -> Any:
        """Return one resolved input value."""

        return self.input_values.get(name, default)

    def add_artifact(self, artifact: ExecutionArtifact) -> None:
        """Attach an artifact declaration to the context."""

        self.artifacts.append(artifact)

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_asset_id": self.target_asset_id,
            "mode": self.mode.value,
            "parameters": dict(self.parameters),
            "resolved_inputs": [
                resolved_input.to_dict()
                for resolved_input in self.resolved_inputs
            ],
            "environment": self.environment.to_dict(),
            "artifacts": [
                artifact.to_dict()
                for artifact in self.artifacts
            ],
            "metadata": dict(self.metadata),
        }