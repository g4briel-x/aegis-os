"""Contract input resolution for the Aegis OS runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .context import ResolvedExecutionInput
from .contracts import ExecutionContract


@dataclass(slots=True)
class InputResolutionIssue:
    """One issue detected while resolving contract inputs."""

    severity: str
    code: str
    message: str
    input_name: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "input_name": self.input_name,
        }


@dataclass(slots=True)
class InputResolutionResult:
    """Result of resolving parameters against a contract."""

    resolved_inputs: list[ResolvedExecutionInput] = field(default_factory=list)
    issues: list[InputResolutionIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[InputResolutionIssue]:
        return [
            issue
            for issue in self.issues
            if issue.severity == "error"
        ]

    @property
    def warnings(self) -> list[InputResolutionIssue]:
        return [
            issue
            for issue in self.issues
            if issue.severity == "warning"
        ]

    @property
    def ok(self) -> bool:
        return not self.errors

    @property
    def values(self) -> dict[str, Any]:
        return {
            resolved_input.name: resolved_input.value
            for resolved_input in self.resolved_inputs
        }

    def add_issue(
        self,
        severity: str,
        code: str,
        message: str,
        input_name: str = "",
    ) -> None:
        self.issues.append(
            InputResolutionIssue(
                severity=severity,
                code=code,
                message=message,
                input_name=input_name,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "resolved_inputs": [
                resolved_input.to_dict()
                for resolved_input in self.resolved_inputs
            ],
            "issues": [
                issue.to_dict()
                for issue in self.issues
            ],
        }


class ExecutionInputResolver:
    """Resolve runtime parameters against execution contract inputs."""

    def resolve(
        self,
        contract: ExecutionContract,
        parameters: dict[str, Any] | None = None,
    ) -> InputResolutionResult:
        supplied_parameters = dict(parameters or {})
        result = InputResolutionResult()

        declared_names = {
            contract_input.name
            for contract_input in contract.inputs
        }

        for contract_input in contract.inputs:
            name = contract_input.name

            if name in supplied_parameters:
                result.resolved_inputs.append(
                    ResolvedExecutionInput(
                        name=name,
                        value=supplied_parameters[name],
                        source="parameter",
                        required=contract_input.required,
                    )
                )
                continue

            if name == "target_asset_id":
                result.resolved_inputs.append(
                    ResolvedExecutionInput(
                        name=name,
                        value=contract.asset_id,
                        source="runtime",
                        required=contract_input.required,
                    )
                )
                continue

            if contract_input.default is not None:
                result.resolved_inputs.append(
                    ResolvedExecutionInput(
                        name=name,
                        value=contract_input.default,
                        source="contract-default",
                        required=contract_input.required,
                    )
                )
                continue

            if contract_input.required:
                result.add_issue(
                    severity="error",
                    code="missing_required_input",
                    message=f"Required input '{name}' was not provided.",
                    input_name=name,
                )
                continue

            result.resolved_inputs.append(
                ResolvedExecutionInput(
                    name=name,
                    value=None,
                    source="optional",
                    required=False,
                )
            )

        unknown_parameters = sorted(
            set(supplied_parameters) - declared_names
        )

        for parameter_name in unknown_parameters:
            result.add_issue(
                severity="warning",
                code="unknown_input_parameter",
                message=(
                    f"Parameter '{parameter_name}' is not declared "
                    "by the execution contract."
                ),
                input_name=parameter_name,
            )

        return result