"""Execution session builder for the Aegis OS runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .context_builder import (
    ExecutionContextBuilder,
    ExecutionContextBuildResult,
)
from .contracts import ExecutionContract
from .models import ExecutionMode
from .session import (
    ExecutionSession,
    ExecutionSessionState,
)
from .workspace import (
    ExecutionWorkspace,
    WorkspaceLocation,
)


@dataclass(slots=True)
class SessionBuildIssue:
    """One issue detected while building an execution session."""

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
class ExecutionSessionBuildResult:
    """Result of building an execution session and workspace."""

    session: ExecutionSession
    workspace: ExecutionWorkspace
    context_build: ExecutionContextBuildResult
    issues: list[SessionBuildIssue] = field(
        default_factory=list
    )

    @property
    def errors(self) -> list[Any]:
        """Return all blocking session and context issues."""

        return [
            *[
                issue
                for issue in self.issues
                if issue.severity == "error"
            ],
            *self.context_build.errors,
        ]

    @property
    def warnings(self) -> list[Any]:
        """Return all non-blocking session and context issues."""

        return [
            *[
                issue
                for issue in self.issues
                if issue.severity == "warning"
            ],
            *self.context_build.warnings,
        ]

    @property
    def ok(self) -> bool:
        """Return whether the session was built successfully."""

        return (
            not self.errors
            and self.session.context is not None
            and self.workspace.state.value == "ready"
        )

    def add_issue(
        self,
        severity: str,
        code: str,
        message: str,
    ) -> None:
        """Attach one issue to the session build result."""

        self.issues.append(
            SessionBuildIssue(
                severity=severity,
                code=code,
                message=message,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize the complete session build result."""

        return {
            "ok": self.ok,
            "session": self.session.to_dict(),
            "workspace": self.workspace.to_dict(),
            "context_build": self.context_build.to_dict(),
            "issues": [
                issue.to_dict()
                for issue in self.issues
            ],
        }


class ExecutionSessionBuilder:
    """Build execution sessions with logical isolated workspaces."""

    def __init__(
        self,
        context_builder: ExecutionContextBuilder | None = None,
    ) -> None:
        self.context_builder = (
            context_builder or ExecutionContextBuilder()
        )

    def build(
        self,
        contract: ExecutionContract,
        mode: ExecutionMode = ExecutionMode.DRY_RUN,
        parameters: dict[str, Any] | None = None,
    ) -> ExecutionSessionBuildResult:
        """Build one execution session and its logical workspace."""

        context_build = self.context_builder.build(
            contract=contract,
            mode=mode,
            parameters=parameters,
        )

        session = ExecutionSession(
            target_asset_id=contract.asset_id,
            mode=mode,
            audit_metadata={
                "contract_type": contract.contract_type.value,
                "safety_level": contract.safety_level.value,
            },
            metadata={
                "required_assets": list(
                    contract.required_assets
                ),
            },
        )

        workspace = ExecutionWorkspace(
            session_id=session.session_id,
            metadata={
                "target_asset_id": contract.asset_id,
                "mode": mode.value,
                "safety_level": contract.safety_level.value,
            },
        )

        result = ExecutionSessionBuildResult(
            session=session,
            workspace=workspace,
            context_build=context_build,
        )

        try:
            self._declare_workspace_locations(
                workspace=workspace,
                context_build=context_build,
            )
        except ValueError as exc:
            result.add_issue(
                severity="error",
                code="workspace_location_error",
                message=str(exc),
            )

        session.workspace_id = workspace.workspace_id

        if result.errors:
            session.transition_to(
                ExecutionSessionState.FAILED
            )
            return result

        session.attach_context(context_build.context)
        workspace.mark_ready()

        return result

    def _declare_workspace_locations(
        self,
        workspace: ExecutionWorkspace,
        context_build: ExecutionContextBuildResult,
    ) -> None:
        """Reserve standard logical workspace locations."""

        standard_locations = [
            WorkspaceLocation(
                name="resolved-inputs",
                relative_path="inputs/resolved-inputs.json",
                purpose=(
                    "Future serialized resolved input manifest."
                ),
                writable=False,
            ),
            WorkspaceLocation(
                name="execution-context",
                relative_path="context/execution-context.json",
                purpose=(
                    "Future serialized execution context manifest."
                ),
                writable=False,
            ),
            WorkspaceLocation(
                name="artifacts",
                relative_path="artifacts",
                purpose=(
                    "Logical root for future execution artifacts."
                ),
                writable=False,
            ),
            WorkspaceLocation(
                name="session-audit",
                relative_path="audit/session.json",
                purpose=(
                    "Future execution session audit manifest."
                ),
                writable=False,
            ),
        ]

        for location in standard_locations:
            workspace.add_location(location)

        for artifact in context_build.context.artifacts:
            workspace.add_location(
                WorkspaceLocation(
                    name=f"artifact:{artifact.name}",
                    relative_path=(
                        f"artifacts/{artifact.name}"
                    ),
                    purpose=(
                        "Reserved logical location for "
                        f"artifact '{artifact.name}'."
                    ),
                    writable=False,
                    metadata={
                        "artifact_type": artifact.artifact_type,
                        "status": artifact.metadata.get(
                            "status",
                            "declared",
                        ),
                    },
                )
            )