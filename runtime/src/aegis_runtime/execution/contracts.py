"""Execution contract models for Aegis OS runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class ExecutionContractType(StrEnum):
    """Supported execution contract types."""

    PLAYBOOK = "playbook"
    SKILL = "skill"


class ExecutionSafetyLevel(StrEnum):
    """Safety levels for future executable actions."""

    SAFE_READ_ONLY = "safe-read-only"
    SAFE_DRY_RUN = "safe-dry-run"
    REQUIRES_APPROVAL = "requires-approval"
    BLOCKED = "blocked"


@dataclass(slots=True)
class ExecutionInput:
    """Input required by an execution contract."""

    name: str
    description: str = ""
    required: bool = False
    default: Any = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "required": self.required,
            "default": self.default,
        }


@dataclass(slots=True)
class ExecutionOutput:
    """Output produced by an execution contract."""

    name: str
    description: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
        }


@dataclass(slots=True)
class ExecutionContract:
    """Execution contract for a playbook or skill."""

    asset_id: str
    contract_type: ExecutionContractType
    safety_level: ExecutionSafetyLevel = ExecutionSafetyLevel.SAFE_DRY_RUN
    description: str = ""
    allowed_modes: list[str] = field(default_factory=lambda: ["plan", "dry-run"])
    inputs: list[ExecutionInput] = field(default_factory=list)
    outputs: list[ExecutionOutput] = field(default_factory=list)
    required_assets: list[str] = field(default_factory=list)
    forbidden_actions: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def is_safe_for_dry_run(self) -> bool:
        return self.safety_level in {
            ExecutionSafetyLevel.SAFE_READ_ONLY,
            ExecutionSafetyLevel.SAFE_DRY_RUN,
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "asset_id": self.asset_id,
            "contract_type": self.contract_type.value,
            "safety_level": self.safety_level.value,
            "description": self.description,
            "allowed_modes": list(self.allowed_modes),
            "inputs": [item.to_dict() for item in self.inputs],
            "outputs": [item.to_dict() for item in self.outputs],
            "required_assets": list(self.required_assets),
            "forbidden_actions": list(self.forbidden_actions),
            "metadata": dict(self.metadata),
        }


@dataclass(slots=True)
class ContractValidationIssue:
    """One issue found while validating an execution contract."""

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
class ContractValidationResult:
    """Validation result for one execution contract."""

    contract: ExecutionContract
    issues: list[ContractValidationIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[ContractValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "error"]

    @property
    def warnings(self) -> list[ContractValidationIssue]:
        return [issue for issue in self.issues if issue.severity == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors

    def add_issue(self, severity: str, code: str, message: str) -> None:
        self.issues.append(
            ContractValidationIssue(
                severity=severity,
                code=code,
                message=message,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "contract": self.contract.to_dict(),
            "issues": [issue.to_dict() for issue in self.issues],
        }