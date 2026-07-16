"""Execution context builder for the Aegis OS runtime."""

from __future__ import annotations

import platform
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .context import (
    ExecutionArtifact,
    ExecutionContext,
    ExecutionEnvironment,
)
from .contracts import ExecutionContract
from .input_resolver import (
    ExecutionInputResolver,
    InputResolutionIssue,
    InputResolutionResult,
)
from .models import ExecutionMode


@dataclass(slots=True)
class ContextBuildIssue:
    """One issue detected while building an execution context."""

    severity: str
    code: str
    message: str

    def to_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
        }


@dataclass(slots=True)
class ExecutionContextBuildResult:
    """Result of building an execution context."""

    context: ExecutionContext
    input_resolution: InputResolutionResult
    issues: list[ContextBuildIssue] = field(default_factory=list)

    @property
    def errors(
        self,
    ) -> list[ContextBuildIssue | InputResolutionIssue]:
        return [
            *[
                issue
                for issue in self.issues
                if issue.severity == "error"
            ],
            *self.input_resolution.errors,
        ]

    @property
    def warnings(
        self,
    ) -> list[ContextBuildIssue | InputResolutionIssue]:
        return [
            *[
                issue
                for issue in self.issues
                if issue.severity == "warning"
            ],
            *self.input_resolution.warnings,
        ]

    @property
    def ok(self) -> bool:
        return not self.errors

    def add_issue(
        self,
        severity: str,
        code: str,
        message: str,
    ) -> None:
        self.issues.append(
            ContextBuildIssue(
                severity=severity,
                code=code,
                message=message,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "context": self.context.to_dict(),
            "input_resolution": self.input_resolution.to_dict(),
            "issues": [
                issue.to_dict()
                for issue in self.issues
            ],
        }


class ExecutionContextBuilder:
    """Build execution contexts from contracts and parameters."""

    def __init__(
        self,
        input_resolver: ExecutionInputResolver | None = None,
    ) -> None:
        self.input_resolver = (
            input_resolver or ExecutionInputResolver()
        )

    def build(
        self,
        contract: ExecutionContract,
        mode: ExecutionMode = ExecutionMode.DRY_RUN,
        parameters: dict[str, Any] | None = None,
    ) -> ExecutionContextBuildResult:
        """Build a resolved execution context."""

        supplied_parameters = dict(parameters or {})

        input_resolution = self.input_resolver.resolve(
            contract=contract,
            parameters=supplied_parameters,
        )

        context = ExecutionContext(
            target_asset_id=contract.asset_id,
            mode=mode,
            parameters=supplied_parameters,
            resolved_inputs=list(
                input_resolution.resolved_inputs
            ),
            environment=self._build_environment(),
            artifacts=self._build_artifacts(contract),
            metadata={
                "contract_type": contract.contract_type.value,
                "safety_level": contract.safety_level.value,
                "required_assets": list(
                    contract.required_assets
                ),
            },
        )

        result = ExecutionContextBuildResult(
            context=context,
            input_resolution=input_resolution,
        )

        if mode.value not in contract.allowed_modes:
            result.add_issue(
                severity="error",
                code="execution_mode_not_allowed",
                message=(
                    f"Execution mode '{mode.value}' is not "
                    f"allowed by contract '{contract.asset_id}'."
                ),
            )

        return result

    def _build_environment(self) -> ExecutionEnvironment:
        """Collect safe local execution environment metadata."""

        return ExecutionEnvironment(
            name="local",
            working_directory=str(Path.cwd()),
            python_version=platform.python_version(),
            platform=platform.platform(),
            variables={},
        )

    def _build_artifacts(
        self,
        contract: ExecutionContract,
    ) -> list[ExecutionArtifact]:
        """Declare the artifacts expected from contract outputs."""

        return [
            ExecutionArtifact(
                name=output.name,
                artifact_type="declared-output",
                metadata={
                    "description": output.description,
                    "status": "declared",
                },
            )
            for output in contract.outputs
        ]