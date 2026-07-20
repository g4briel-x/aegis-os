"""Command-line interface for the Aegis runtime."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Sequence

from . import __version__
from .asset_resolver import AssetResolver
from .config import AegisConfig
from .doctor import DoctorCheckResult, run_all_checks
from .execution import (
    ExecutionAuditEventType,
    ExecutionAuditHistoryReader,
    ExecutionAuditVerifier,
    ExecutionContextBuilder,
    ExecutionLifecycleAction,
    ExecutionLifecycleManager,
    ExecutionLifecycleStore,
    ExecutionMode,
    ExecutionOrchestrationStore,
    ExecutionOrchestrator,
    ExecutionSessionBuilder,
    ExecutionSessionLoader,
    ExecutionWorkspaceStore,
)
from .execution.contract_builder import ExecutionContractBuilder
from .execution.contract_validator import ExecutionContractValidator
from .execution.planner import ExecutionPlanner
from .execution.runner import ExecutionRunner
from .models import Asset
from .registry_loader import RegistryLoader
from .reports import REPORT_GENERATORS, generate_all_reports, generate_report
from .validator import RegistryValidator

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_REPOSITORY = 3
EXIT_VALIDATION = 4
EXIT_NOT_FOUND = 5


def _build_parser() -> argparse.ArgumentParser:
    """Build the Aegis runtime command-line parser."""

    parser = argparse.ArgumentParser(
        prog="aegis-runtime",
        description="Aegis OS Python runtime",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        help="Path to the Aegis OS repository root.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Render JSON output.",
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True,
    )

    commands.add_parser(
        "version",
        help="Show runtime version.",
    )
    commands.add_parser(
        "status",
        help="Show repository runtime status.",
    )

    registry = commands.add_parser(
        "registry",
        help="Registry operations.",
    )
    registry_commands = registry.add_subparsers(
        dest="registry_command",
        required=True,
    )
    registry_commands.add_parser(
        "list",
        help="List registry files.",
    )

    asset = commands.add_parser(
        "asset",
        help="Asset operations.",
    )
    asset_commands = asset.add_subparsers(
        dest="asset_command",
        required=True,
    )

    asset_show = asset_commands.add_parser(
        "show",
        help="Show one asset.",
    )
    asset_show.add_argument("asset_id")

    asset_find = asset_commands.add_parser(
        "find",
        help="Search assets.",
    )
    asset_find.add_argument("query")

    asset_domain = asset_commands.add_parser(
        "domain",
        help="List assets in a domain.",
    )
    asset_domain.add_argument("domain")

    asset_tag = asset_commands.add_parser(
        "tag",
        help="List assets with a tag.",
    )
    asset_tag.add_argument("tag")

    asset_type = asset_commands.add_parser(
        "type",
        help="List assets of a given type (skill, playbook, template, pattern, docs, ...).",
    )
    asset_type.add_argument("type")

    asset_related = asset_commands.add_parser(
        "related",
        help="List assets declared as related to a given asset.",
    )
    asset_related.add_argument("asset_id")

    asset_path = asset_commands.add_parser(
        "path",
        help="Print the resolved filesystem path of an asset.",
    )
    asset_path.add_argument("asset_id")

    asset_open = asset_commands.add_parser(
        "open",
        help="Open an asset's file with the OS default application.",
    )
    asset_open.add_argument("asset_id")

    config = commands.add_parser(
        "config",
        help="Repository configuration operations.",
    )
    config_commands = config.add_subparsers(
        dest="config_command",
        required=True,
    )
    config_commands.add_parser(
        "show",
        help="Print the merged repository configuration.",
    )
    config_commands.add_parser(
        "path",
        help="Print the paths of loaded configuration files.",
    )
    config_commands.add_parser(
        "check",
        help="Verify that repository configuration can be discovered and loaded.",
    )

    execution = commands.add_parser(
        "execution",
        help="Execution planning operations.",
    )
    execution_commands = execution.add_subparsers(
        dest="execution_command",
        required=True,
    )

    execution_plan = execution_commands.add_parser(
        "plan",
        help="Create an execution plan for an asset.",
    )
    execution_plan.add_argument("asset_id")

    execution_dry_run = execution_commands.add_parser(
        "dry-run",
        help="Create a safe dry-run report for an asset.",
    )
    execution_dry_run.add_argument("asset_id")

    execution_contract = execution_commands.add_parser(
        "contract",
        help="Build and validate an execution contract for an asset.",
    )
    execution_contract.add_argument("asset_id")

    execution_context = execution_commands.add_parser(
        "context",
        help="Build a resolved execution context for an asset.",
    )
    execution_context.add_argument("asset_id")
    execution_context.add_argument(
        "--mode",
        choices=[mode.value for mode in ExecutionMode],
        default=ExecutionMode.DRY_RUN.value,
        help="Execution mode used to build the context.",
    )
    execution_context.add_argument(
        "--input",
        action="append",
        default=[],
        metavar="NAME=VALUE",
        help=(
            "Runtime input parameter. "
            "May be supplied multiple times."
        ),
    )

    execution_session = execution_commands.add_parser(
        "session",
        help=(
            "Build an execution session with a logical workspace "
            "for an asset."
        ),
    )
    execution_session.add_argument("asset_id")
    execution_session.add_argument(
        "--mode",
        choices=[mode.value for mode in ExecutionMode],
        default=ExecutionMode.DRY_RUN.value,
        help="Execution mode used to build the session.",
    )
    execution_session.add_argument(
        "--input",
        action="append",
        default=[],
        metavar="NAME=VALUE",
        help=(
            "Runtime input parameter. "
            "May be supplied multiple times."
        ),
    )

    execution_session_show = execution_commands.add_parser(
        "session-show",
        help=(
            "Show one persisted execution session by "
            "workspace ID or session ID."
        ),
    )
    execution_session_show.add_argument(
        "identifier",
        help="Execution workspace ID or session ID.",
    )

    execution_orchestrate = execution_commands.add_parser(
        "orchestrate",
        help=(
            "Orchestrate one persisted execution session "
            "by workspace ID or session ID."
        ),
    )
    execution_orchestrate.add_argument(
        "identifier",
        help="Execution workspace ID or session ID.",
    )

    execution_audit_history = execution_commands.add_parser(
        "audit-history",
        help=(
            "Inspect the validated audit history of one "
            "persisted execution session."
        ),
    )
    execution_audit_history.add_argument(
        "identifier",
        help="Execution workspace ID or session ID.",
    )
    execution_audit_history.add_argument(
        "--event-type",
        choices=[
            event_type.value
            for event_type in ExecutionAuditEventType
        ],
        default="",
        help="Filter events by audit event type.",
    )
    execution_audit_history.add_argument(
        "--actor",
        default="",
        help="Filter events by exact actor identity.",
    )
    execution_audit_history.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of events to display.",
    )
    execution_audit_history.add_argument(
        "--reverse",
        action="store_true",
        help="Display the most recent events first.",
    )

    execution_audit_verify = execution_commands.add_parser(
        "audit-verify",
        help=(
            "Verify the structural and cryptographic integrity "
            "of one persisted execution audit journal."
        ),
    )
    execution_audit_verify.add_argument(
        "identifier",
        help="Execution workspace ID or session ID.",
    )

    execution_lifecycle = execution_commands.add_parser(
        "lifecycle",
        help=(
            "Apply a terminal lifecycle action to one "
            "persisted execution session."
        ),
    )
    execution_lifecycle.add_argument(
        "identifier",
        help="Execution workspace ID or session ID.",
    )
    execution_lifecycle.add_argument(
        "action",
        choices=[
            action.value
            for action in ExecutionLifecycleAction
        ],
        help="Terminal lifecycle action.",
    )
    execution_lifecycle.add_argument(
        "--reason",
        default="",
        help=(
            "Lifecycle reason. Required for fail "
            "and cancel actions."
        ),
    )
    execution_lifecycle.add_argument(
        "--actor",
        default="aegis-runtime",
        help="Identity responsible for the transition.",
    )

    validate = commands.add_parser(
        "validate",
        help="Validate registries.",
    )
    validate.add_argument(
        "--strict-related",
        action="store_true",
        help="Treat unresolved related assets as errors.",
    )

    doctor = commands.add_parser(
        "doctor",
        help="Run repository health checks.",
    )
    doctor.add_argument(
        "--skip-validate",
        action="store_true",
        help="Skip registry validation after the health checks.",
    )
    doctor.add_argument(
        "--skip-reports",
        action="store_true",
        help="Skip report generation after the health checks.",
    )

    report = commands.add_parser(
        "report",
        help="Registry report generation.",
    )
    report_commands = report.add_subparsers(
        dest="report_command",
        required=True,
    )
    report_generate = report_commands.add_parser(
        "generate",
        help="Generate one or all registry reports.",
    )
    report_generate.add_argument(
        "name",
        choices=[*REPORT_GENERATORS, "all"],
        help="Report to generate, or 'all' for every report.",
    )

    return parser


def _config_from_args(args: argparse.Namespace) -> AegisConfig:
    """Discover runtime configuration from CLI arguments."""

    return AegisConfig.discover(
        args.repo_root
        if args.repo_root
        else None
    )


def _print_json(payload: Any) -> None:
    """Print one JSON-compatible payload."""

    print(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
        )
    )


def _print_asset(
    asset: Asset,
    *,
    as_json: bool,
) -> None:
    """Print one registry asset."""

    if as_json:
        _print_json(asset.to_dict())
        return

    print(f"ID: {asset.id}")
    print(f"Name: {asset.name or '-'}")
    print(f"Type: {asset.type or '-'}")
    print(f"Domain: {asset.domain or '-'}")
    print(f"Path: {asset.path or '-'}")
    print(
        "Tags: "
        + (
            ", ".join(asset.tags)
            if asset.tags
            else "-"
        )
    )
    print(
        "Related assets: "
        + (
            ", ".join(asset.related_assets)
            if asset.related_assets
            else "-"
        )
    )

    if asset.source_file:
        print(f"Registry: {asset.source_file}")


def _print_asset_list(
    assets: list[Asset],
    *,
    as_json: bool,
) -> None:
    """Print a list of registry assets."""

    if as_json:
        _print_json(
            [asset.to_dict() for asset in assets]
        )
        return

    for asset in assets:
        details = [asset.id]

        if asset.domain:
            details.append(f"domain={asset.domain}")

        if asset.type:
            details.append(f"type={asset.type}")

        print(" | ".join(details))

    print(f"Total assets: {len(assets)}")


def _open_file(path: Path) -> None:
    """Open a file with the OS default application.

    Cross-platform by design (the original PowerShell asset:open command
    only worked on Windows via Start-Process explorer.exe): tries
    os.startfile on Windows, 'open' on macOS, and 'xdg-open' on Linux/BSD.
    """

    import platform
    import subprocess

    system = platform.system()

    if system == "Windows":
        os.startfile(path)  # type: ignore[attr-defined]
    elif system == "Darwin":
        subprocess.run(["open", str(path)], check=True)
    else:
        subprocess.run(["xdg-open", str(path)], check=True)


def _parse_execution_inputs(
    values: list[str],
) -> dict[str, str]:
    """Parse repeated NAME=VALUE execution input arguments."""

    parameters: dict[str, str] = {}

    for item in values:
        if "=" not in item:
            raise ValueError(
                f"Invalid execution input '{item}'. "
                "Expected NAME=VALUE."
            )

        name, value = item.split("=", 1)
        name = name.strip()

        if not name:
            raise ValueError(
                "Execution input name cannot be empty."
            )

        if name in parameters:
            raise ValueError(
                f"Execution input '{name}' "
                "was provided more than once."
            )

        parameters[name] = value

    return parameters


def _print_execution_plan(
    plan,
    *,
    as_json: bool,
) -> None:
    """Print one execution plan."""

    if as_json:
        _print_json(plan.to_dict())
        return

    print("Aegis OS Execution Plan")
    print(f"Target: {plan.target_asset_id}")
    print(f"Mode: {plan.mode.value}")
    print("")

    for step in plan.steps:
        print(f"{step.index}. {step.title}")
        print(f"   Action: {step.action}")
        print(f"   Status: {step.status.value}")

        if step.asset_id:
            print(f"   Asset: {step.asset_id}")

        if step.asset_type:
            print(f"   Type: {step.asset_type}")

        print("")

    print(f"Total steps: {len(plan.steps)}")


def _print_execution_report(
    report,
    *,
    as_json: bool,
) -> None:
    """Print one execution dry-run report."""

    if as_json:
        _print_json(report.to_dict())
        return

    print("Aegis OS Execution Dry Run")
    print(f"Status: {report.status.value}")
    print(f"Message: {report.message}")
    print("")

    _print_execution_plan(
        report.plan,
        as_json=False,
    )


def _print_execution_contract_result(
    result,
    *,
    as_json: bool,
) -> None:
    """Print one execution contract validation result."""

    if as_json:
        _print_json(result.to_dict())
        return

    contract = result.contract

    print("Aegis OS Execution Contract")
    print(f"Asset: {contract.asset_id}")
    print(f"Type: {contract.contract_type.value}")
    print(f"Safety: {contract.safety_level.value}")
    print(
        "Allowed modes: "
        + ", ".join(contract.allowed_modes)
    )
    print("")

    print("Inputs:")

    if contract.inputs:
        for item in contract.inputs:
            required = (
                "required"
                if item.required
                else "optional"
            )
            print(f"- {item.name} ({required})")
    else:
        print("- none")

    print("")
    print("Outputs:")

    if contract.outputs:
        for item in contract.outputs:
            print(f"- {item.name}")
    else:
        print("- none")

    print("")
    print("Required assets:")

    if contract.required_assets:
        for asset_id in contract.required_assets:
            print(f"- {asset_id}")
    else:
        print("- none")

    print("")
    print("Forbidden actions:")

    if contract.forbidden_actions:
        for action in contract.forbidden_actions:
            print(f"- {action}")
    else:
        print("- none")

    print("")
    print(
        "Validation: "
        f"{'passed' if result.ok else 'failed'}"
    )
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")

    for issue in result.issues:
        print(
            f"[{issue.severity.upper()}] "
            f"{issue.code}: {issue.message}"
        )


def _print_execution_context_result(
    result,
    *,
    as_json: bool,
) -> None:
    """Print one execution context build result."""

    if as_json:
        _print_json(result.to_dict())
        return

    context = result.context

    print("Aegis OS Execution Context")
    print(f"Target: {context.target_asset_id}")
    print(f"Mode: {context.mode.value}")
    print(
        "Build: "
        f"{'passed' if result.ok else 'failed'}"
    )
    print("")

    print("Resolved inputs:")

    if context.resolved_inputs:
        for item in context.resolved_inputs:
            required = (
                "required"
                if item.required
                else "optional"
            )
            print(
                f"- {item.name}={item.value} "
                f"[source={item.source}, {required}]"
            )
    else:
        print("- none")

    print("")
    print("Environment:")
    print(f"- name: {context.environment.name}")
    print(
        "- working directory: "
        f"{context.environment.working_directory}"
    )
    print(
        "- Python: "
        f"{context.environment.python_version}"
    )
    print(f"- platform: {context.environment.platform}")
    print("")

    print("Declared artifacts:")

    if context.artifacts:
        for artifact in context.artifacts:
            print(
                f"- {artifact.name} "
                f"[type={artifact.artifact_type}]"
            )
    else:
        print("- none")

    print("")
    print(
        "Input resolution: "
        f"{'passed' if result.input_resolution.ok else 'failed'}"
    )
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")

    all_issues = [
        *result.issues,
        *result.input_resolution.issues,
    ]

    for issue in all_issues:
        print(
            f"[{issue.severity.upper()}] "
            f"{issue.code}: {issue.message}"
        )


def _print_execution_session_result(
    result,
    persisted=None,
    *,
    as_json: bool,
) -> None:
    """Print one execution session build result."""

    if as_json:
        payload = result.to_dict()
        payload["persistence"] = (
            persisted.to_dict()
            if persisted is not None
            else None
        )
        _print_json(payload)
        return

    session = result.session
    workspace = result.workspace

    print("Aegis OS Execution Session")
    print(f"Session: {session.session_id}")
    print(f"Target: {session.target_asset_id}")
    print(f"Mode: {session.mode.value}")
    print(f"State: {session.state.value}")
    print(
        "Build: "
        f"{'passed' if result.ok else 'failed'}"
    )
    print("")

    print("Workspace:")
    print(f"- ID: {workspace.workspace_id}")
    print(f"- state: {workspace.state.value}")
    print(f"- logical path: {workspace.logical_path}")
    print(f"- isolation key: {workspace.isolation_key}")
    print("")

    print("Reserved locations:")

    if workspace.locations:
        for location in workspace.locations:
            access = (
                "writable"
                if location.writable
                else "read-only"
            )
            print(
                f"- {location.name}: "
                f"{location.relative_path} [{access}]"
            )
    else:
        print("- none")

    print("")
    print("Persistence:")

    if persisted is not None:
        print(f"- workspace: {persisted.workspace_path}")
        print(f"- session: {persisted.session_manifest}")
        print(f"- context: {persisted.context_manifest}")
        print(f"- inputs: {persisted.inputs_manifest}")
        print(f"- audit: {persisted.audit_manifest}")
    else:
        print("- not persisted")

    print("")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")

    all_issues = [
        *result.issues,
        *result.context_build.issues,
        *result.context_build.input_resolution.issues,
    ]

    for issue in all_issues:
        print(
            f"[{issue.severity.upper()}] "
            f"{issue.code}: {issue.message}"
        )


def _print_stored_execution_session(
    record,
    *,
    as_json: bool,
) -> None:
    """Print one persisted execution session."""

    if as_json:
        _print_json(record.to_dict())
        return

    payload = record.payload
    session = payload.get("session", {})
    build = payload.get("build", {})

    print("Aegis OS Stored Execution Session")
    print(f"Session: {record.session_id}")
    print(f"Workspace: {record.workspace_id}")
    print(
        "Target: "
        f"{session.get('target_asset_id', '-')}"
    )
    print(f"Mode: {session.get('mode', '-')}")
    print(f"State: {session.get('state', '-')}")
    print(
        "Build: "
        f"{'passed' if build.get('ok') else 'failed'}"
    )
    print("")

    print("Storage:")
    print(f"- workspace: {record.workspace_path}")
    print(f"- session: {record.session_manifest}")
    print(
        "- context: "
        f"{record.workspace_path / 'context' / 'execution-context.json'}"
    )
    print(
        "- inputs: "
        f"{record.workspace_path / 'inputs' / 'resolved-inputs.json'}"
    )
    print(
        "- audit: "
        f"{record.workspace_path / 'audit' / 'session.json'}"
    )


def _print_execution_orchestration_result(
    result,
    persisted,
    *,
    as_json: bool,
) -> None:
    """Print one persistent orchestration result."""

    if as_json:
        payload = result.to_dict()
        payload["persistence"] = persisted.to_dict()
        _print_json(payload)
        return

    session = result.session

    print("Aegis OS Execution Orchestration")
    print(f"Session: {session.session_id}")
    print(f"Workspace: {session.workspace_id}")
    print(f"Target: {session.target_asset_id}")
    print(f"Mode: {session.mode.value}")
    print(f"State: {session.state.value}")
    print(
        "Orchestration: "
        f"{'passed' if result.ok else 'failed'}"
    )
    print("")

    print("Audit events:")

    for event in result.events:
        transition = ""

        if event.previous_state and event.next_state:
            transition = (
                f" [{event.previous_state}"
                f" -> {event.next_state}]"
            )

        print(
            f"- {event.event_type.value}: "
            f"{event.message}{transition}"
        )

    print("")
    print("Persistence:")
    print(f"- session: {persisted.session_manifest}")
    print(f"- audit: {persisted.audit_manifest}")
    print(f"- events written: {persisted.event_count}")


def _print_execution_audit_history(
    history,
    events,
    *,
    as_json: bool,
) -> None:
    """Print one validated execution audit history."""

    if as_json:
        payload = history.to_dict()
        payload["selected_event_count"] = len(events)
        payload["events"] = [
            event.to_dict()
            for event in events
        ]
        _print_json(payload)
        return

    print("Aegis OS Execution Audit History")
    print(f"Session: {history.session_id}")
    print(f"Workspace: {history.workspace_id}")
    print(f"Target: {history.target_asset_id}")
    print(f"Mode: {history.mode.value}")
    print(f"State: {history.state.value}")
    print(
        "Events: "
        f"{len(events)} selected / "
        f"{history.event_count} total"
    )
    print(f"Audit: {history.audit_manifest}")
    print("")

    if not events:
        print("No audit events matched the selection.")
        return

    for index, event in enumerate(
        events,
        start=1,
    ):
        transition = ""

        if event.previous_state and event.next_state:
            transition = (
                f" [{event.previous_state}"
                f" -> {event.next_state}]"
            )

        print(
            f"{index}. {event.timestamp} "
            f"| {event.event_type.value} "
            f"| actor={event.actor}"
        )
        print(
            f"   {event.message}{transition}"
        )

        if event.metadata:
            print(
                "   Metadata: "
                + json.dumps(
                    event.metadata,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )


def _print_execution_audit_verification(
    report,
    *,
    as_json: bool,
) -> None:
    """Print one successful audit integrity verification report."""

    if as_json:
        _print_json(report.to_dict())
        return

    integrity = report.integrity

    print("Aegis OS Execution Audit Verification")
    print(f"Status: {'passed' if report.ok else 'failed'}")
    print(f"Session: {report.session_id}")
    print(f"Workspace: {report.workspace_id}")
    print(f"Target: {report.target_asset_id}")
    print(f"Mode: {report.mode.value}")
    print(f"State: {report.state.value}")
    print(f"Events: {report.event_count}")
    print(f"Audit: {report.audit_manifest}")
    print("")
    print("Integrity:")
    print(f"- version: {integrity.version}")
    print(f"- algorithm: {integrity.algorithm}")
    print(f"- root hash: {integrity.root_hash}")
    print(f"- manifest hash: {integrity.manifest_hash}")
    print(f"- journal hash: {integrity.journal_hash}")


def _print_execution_lifecycle_result(
    result,
    persisted,
    *,
    as_json: bool,
) -> None:
    """Print one persisted terminal lifecycle result."""

    if as_json:
        payload = result.to_dict()
        payload["persistence"] = persisted.to_dict()
        _print_json(payload)
        return

    session = result.session

    print("Aegis OS Execution Lifecycle")
    print(f"Session: {session.session_id}")
    print(f"Workspace: {session.workspace_id}")
    print(f"Target: {session.target_asset_id}")
    print(f"Mode: {session.mode.value}")
    print(f"Action: {result.action.value}")
    print(f"State: {session.state.value}")
    print(f"Reason: {result.reason}")
    print(f"Actor: {result.actor}")
    print(
        "Lifecycle: "
        f"{'passed' if result.ok else 'failed'}"
    )
    print("")

    print("Audit events:")

    for event in result.events:
        transition = ""

        if event.previous_state and event.next_state:
            transition = (
                f" [{event.previous_state}"
                f" -> {event.next_state}]"
            )

        print(
            f"- {event.event_type.value}: "
            f"{event.message}{transition}"
        )

    print("")
    print("Persistence:")
    print(f"- session: {persisted.session_manifest}")
    print(f"- audit: {persisted.audit_manifest}")
    print(f"- events written: {persisted.event_count}")
    print(f"- terminal state: {persisted.terminal_state}")


def _handle_execution_context(
    args: argparse.Namespace,
    resolver: AssetResolver,
) -> int:
    """Build and print one execution context."""

    asset = resolver.require(args.asset_id)
    contract = (
        ExecutionContractBuilder()
        .build_from_asset(asset)
    )
    contract_validation = (
        ExecutionContractValidator()
        .validate(contract)
    )

    if not contract_validation.ok:
        _print_execution_contract_result(
            contract_validation,
            as_json=args.json,
        )
        return EXIT_VALIDATION

    try:
        parameters = _parse_execution_inputs(
            args.input
        )
    except ValueError as exc:
        print(
            f"Input error: {exc}",
            file=sys.stderr,
        )
        return EXIT_USAGE

    result = ExecutionContextBuilder().build(
        contract=contract,
        mode=ExecutionMode(args.mode),
        parameters=parameters,
    )

    _print_execution_context_result(
        result,
        as_json=args.json,
    )

    return (
        EXIT_OK
        if result.ok
        else EXIT_VALIDATION
    )


def _handle_execution_session(
    args: argparse.Namespace,
    resolver: AssetResolver,
    config: AegisConfig,
) -> int:
    """Build, persist, and print one execution session."""

    asset = resolver.require(args.asset_id)
    contract = (
        ExecutionContractBuilder()
        .build_from_asset(asset)
    )
    contract_validation = (
        ExecutionContractValidator()
        .validate(contract)
    )

    if not contract_validation.ok:
        _print_execution_contract_result(
            contract_validation,
            as_json=args.json,
        )
        return EXIT_VALIDATION

    try:
        parameters = _parse_execution_inputs(
            args.input
        )
    except ValueError as exc:
        print(
            f"Input error: {exc}",
            file=sys.stderr,
        )
        return EXIT_USAGE

    result = ExecutionSessionBuilder().build(
        contract=contract,
        mode=ExecutionMode(args.mode),
        parameters=parameters,
    )

    persisted = None

    if result.ok:
        try:
            persisted = ExecutionWorkspaceStore(
                config.repo_root
            ).persist(result)
        except (OSError, ValueError) as exc:
            print(
                f"Workspace persistence error: {exc}",
                file=sys.stderr,
            )
            return EXIT_REPOSITORY

    _print_execution_session_result(
        result,
        persisted=persisted,
        as_json=args.json,
    )

    return (
        EXIT_OK
        if result.ok
        else EXIT_VALIDATION
    )


def _handle_session_show(
    args: argparse.Namespace,
    config: AegisConfig,
) -> int:
    """Load and print one persisted execution session."""

    store = ExecutionWorkspaceStore(
        config.repo_root
    )

    try:
        record = store.load(
            args.identifier
        )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_NOT_FOUND
    except ValueError as exc:
        print(
            f"Stored session validation error: {exc}",
            file=sys.stderr,
        )
        return EXIT_VALIDATION
    except OSError as exc:
        print(
            f"Stored session repository error: {exc}",
            file=sys.stderr,
        )
        return EXIT_REPOSITORY

    _print_stored_execution_session(
        record,
        as_json=args.json,
    )

    return EXIT_OK


def _handle_orchestration(
    args: argparse.Namespace,
    config: AegisConfig,
) -> int:
    """Orchestrate and persist one stored execution session."""

    workspace_store = ExecutionWorkspaceStore(
        config.repo_root
    )

    try:
        record = workspace_store.load(
            args.identifier
        )
        session = ExecutionSessionLoader().load(
            record
        )
        result = ExecutionOrchestrator().orchestrate(
            session
        )
        persisted = ExecutionOrchestrationStore().persist(
            record=record,
            result=result,
        )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_NOT_FOUND
    except ValueError as exc:
        print(
            f"Orchestration validation error: {exc}",
            file=sys.stderr,
        )
        return EXIT_VALIDATION
    except OSError as exc:
        print(
            f"Orchestration repository error: {exc}",
            file=sys.stderr,
        )
        return EXIT_REPOSITORY

    _print_execution_orchestration_result(
        result,
        persisted,
        as_json=args.json,
    )

    return EXIT_OK


def _handle_audit_history(
    args: argparse.Namespace,
    config: AegisConfig,
) -> int:
    """Load, select, and print one execution audit history."""

    workspace_store = ExecutionWorkspaceStore(
        config.repo_root
    )

    try:
        record = workspace_store.load(
            args.identifier
        )
        history = ExecutionAuditHistoryReader().load(
            record
        )
        selected_event_type = (
            ExecutionAuditEventType(
                args.event_type
            )
            if args.event_type
            else None
        )
        events = history.select(
            event_type=selected_event_type,
            actor=args.actor,
            limit=args.limit,
            reverse=args.reverse,
        )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_NOT_FOUND
    except ValueError as exc:
        print(
            f"Audit history validation error: {exc}",
            file=sys.stderr,
        )
        return EXIT_VALIDATION
    except OSError as exc:
        print(
            f"Audit history repository error: {exc}",
            file=sys.stderr,
        )
        return EXIT_REPOSITORY

    _print_execution_audit_history(
        history,
        events,
        as_json=args.json,
    )

    return EXIT_OK


def _handle_audit_verification(
    args: argparse.Namespace,
    config: AegisConfig,
) -> int:
    """Verify and print one persistent execution audit journal."""

    workspace_store = ExecutionWorkspaceStore(
        config.repo_root
    )

    try:
        record = workspace_store.load(
            args.identifier
        )
        report = ExecutionAuditVerifier().verify(
            record
        )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_NOT_FOUND
    except ValueError as exc:
        print(
            f"Audit verification error: {exc}",
            file=sys.stderr,
        )
        return EXIT_VALIDATION
    except OSError as exc:
        print(
            f"Audit verification repository error: {exc}",
            file=sys.stderr,
        )
        return EXIT_REPOSITORY

    _print_execution_audit_verification(
        report,
        as_json=args.json,
    )

    return EXIT_OK


def _handle_lifecycle(
    args: argparse.Namespace,
    config: AegisConfig,
) -> int:
    """Apply and persist one terminal lifecycle transition."""

    workspace_store = ExecutionWorkspaceStore(
        config.repo_root
    )

    try:
        record = workspace_store.load(
            args.identifier
        )
        session = ExecutionSessionLoader().load(
            record
        )
        result = ExecutionLifecycleManager().transition(
            session=session,
            action=ExecutionLifecycleAction(
                args.action
            ),
            reason=args.reason,
            actor=args.actor,
        )
        persisted = ExecutionLifecycleStore().persist(
            record=record,
            result=result,
        )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_NOT_FOUND
    except ValueError as exc:
        print(
            f"Lifecycle validation error: {exc}",
            file=sys.stderr,
        )
        return EXIT_VALIDATION
    except OSError as exc:
        print(
            f"Lifecycle repository error: {exc}",
            file=sys.stderr,
        )
        return EXIT_REPOSITORY

    _print_execution_lifecycle_result(
        result,
        persisted,
        as_json=args.json,
    )

    return EXIT_OK


def _handle_execution(
    args: argparse.Namespace,
    resolver: AssetResolver,
    config: AegisConfig,
) -> int:
    """Dispatch execution subcommands."""

    planner = ExecutionPlanner(resolver)

    try:
        if args.execution_command == "plan":
            plan = planner.create_plan(
                args.asset_id,
                mode=ExecutionMode.PLAN,
            )
            _print_execution_plan(
                plan,
                as_json=args.json,
            )
            return EXIT_OK

        if args.execution_command == "dry-run":
            report = ExecutionRunner(planner).dry_run(
                args.asset_id
            )
            _print_execution_report(
                report,
                as_json=args.json,
            )
            return EXIT_OK

        if args.execution_command == "contract":
            asset = resolver.require(
                args.asset_id
            )
            contract = (
                ExecutionContractBuilder()
                .build_from_asset(asset)
            )
            result = (
                ExecutionContractValidator()
                .validate(contract)
            )
            _print_execution_contract_result(
                result,
                as_json=args.json,
            )
            return (
                EXIT_OK
                if result.ok
                else EXIT_VALIDATION
            )

        if args.execution_command == "context":
            return _handle_execution_context(
                args,
                resolver,
            )

        if args.execution_command == "session":
            return _handle_execution_session(
                args,
                resolver,
                config,
            )

        if args.execution_command == "session-show":
            return _handle_session_show(
                args,
                config,
            )

        if args.execution_command == "orchestrate":
            return _handle_orchestration(
                args,
                config,
            )

        if args.execution_command == "audit-history":
            return _handle_audit_history(
                args,
                config,
            )

        if args.execution_command == "audit-verify":
            return _handle_audit_verification(
                args,
                config,
            )

        if args.execution_command == "lifecycle":
            return _handle_lifecycle(
                args,
                config,
            )

    except KeyError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_NOT_FOUND

    return EXIT_USAGE


def main(
    argv: Sequence[str] | None = None,
) -> int:
    """Run the Aegis runtime CLI."""

    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "version":
        payload = {
            "name": "Aegis Runtime",
            "version": __version__,
        }

        if args.json:
            _print_json(payload)
        else:
            print("Aegis OS Runtime")
            print(f"Version: {__version__}")

        return EXIT_OK

    try:
        config = _config_from_args(args)
    except (FileNotFoundError, ValueError) as exc:
        print(
            f"Repository error: {exc}",
            file=sys.stderr,
        )
        return EXIT_REPOSITORY

    loader = RegistryLoader(config.repo_root)
    documents = loader.load_all()
    resolver = AssetResolver(documents)

    if args.command == "status":
        payload = {
            "version": __version__,
            "repo_root": str(config.repo_root),
            "registry_root": str(config.registry_root),
            "registry_count": len(documents),
            "asset_count": len(resolver.assets),
            "loaded_config_files": [
                str(path)
                for path in config.loaded_files
            ],
        }

        if args.json:
            _print_json(payload)
        else:
            print("Aegis OS Runtime Status")
            print(f"Version: {payload['version']}")
            print(f"Repository: {payload['repo_root']}")
            print(f"Registries: {payload['registry_count']}")
            print(f"Assets: {payload['asset_count']}")

        return EXIT_OK

    if (
        args.command == "registry"
        and args.registry_command == "list"
    ):
        payload = [
            {
                "name": document.name,
                "path": str(document.path),
                "assets": len(document.assets),
                "errors": len(document.errors),
            }
            for document in documents
        ]

        if args.json:
            _print_json(payload)
        else:
            for item in payload:
                print(
                    f"{item['name']} "
                    f"| assets={item['assets']} "
                    f"| errors={item['errors']} "
                    f"| {item['path']}"
                )

            print(f"Total registries: {len(payload)}")

        return EXIT_OK

    if args.command == "asset":
        if args.asset_command == "show":
            asset = resolver.by_id(args.asset_id)

            if asset is None:
                print(
                    f"Asset not found: {args.asset_id}",
                    file=sys.stderr,
                )
                return EXIT_NOT_FOUND

            _print_asset(
                asset,
                as_json=args.json,
            )
            return EXIT_OK

        if args.asset_command == "find":
            _print_asset_list(
                resolver.find(args.query),
                as_json=args.json,
            )
            return EXIT_OK

        if args.asset_command == "domain":
            _print_asset_list(
                resolver.by_domain(args.domain),
                as_json=args.json,
            )
            return EXIT_OK

        if args.asset_command == "tag":
            _print_asset_list(
                resolver.by_tag(args.tag),
                as_json=args.json,
            )
            return EXIT_OK

        if args.asset_command == "type":
            _print_asset_list(
                resolver.by_type(args.type),
                as_json=args.json,
            )
            return EXIT_OK

        if args.asset_command == "related":
            asset = resolver.by_id(args.asset_id)

            if asset is None:
                print(
                    f"Asset not found: {args.asset_id}",
                    file=sys.stderr,
                )
                return EXIT_NOT_FOUND

            _print_asset_list(
                resolver.related(args.asset_id),
                as_json=args.json,
            )
            return EXIT_OK

        if args.asset_command == "path":
            asset = resolver.by_id(args.asset_id)

            if asset is None:
                print(
                    f"Asset not found: {args.asset_id}",
                    file=sys.stderr,
                )
                return EXIT_NOT_FOUND

            if not asset.path:
                print(
                    f"Asset has no declared path: {args.asset_id}",
                    file=sys.stderr,
                )
                return EXIT_NOT_FOUND

            resolved_path = config.repo_root / asset.path

            if args.json:
                _print_json(
                    {
                        "asset_id": asset.id,
                        "declared_path": asset.path,
                        "resolved_path": str(resolved_path),
                        "exists": resolved_path.exists(),
                    }
                )
            else:
                print(str(resolved_path))

            return EXIT_OK

        if args.asset_command == "open":
            asset = resolver.by_id(args.asset_id)

            if asset is None:
                print(
                    f"Asset not found: {args.asset_id}",
                    file=sys.stderr,
                )
                return EXIT_NOT_FOUND

            if not asset.path:
                print(
                    f"Asset has no declared path: {args.asset_id}",
                    file=sys.stderr,
                )
                return EXIT_NOT_FOUND

            resolved_path = config.repo_root / asset.path

            if not resolved_path.exists():
                print(
                    f"Declared asset path does not exist: {resolved_path}",
                    file=sys.stderr,
                )
                return EXIT_NOT_FOUND

            try:
                _open_file(resolved_path)
            except (OSError, FileNotFoundError) as exc:
                print(
                    f"Could not open asset file: {exc}",
                    file=sys.stderr,
                )
                return EXIT_REPOSITORY

            print(f"Opened: {resolved_path}")
            return EXIT_OK

    if args.command == "config":
        if args.config_command == "show":
            if args.json:
                _print_json(config.values)
            else:
                print(
                    json.dumps(
                        config.values,
                        indent=2,
                        ensure_ascii=False,
                    )
                )
            return EXIT_OK

        if args.config_command == "path":
            payload = [str(path) for path in config.loaded_files]

            if args.json:
                _print_json(payload)
            else:
                if payload:
                    for path in payload:
                        print(path)
                else:
                    print("No configuration files loaded.")

            return EXIT_OK

        if args.config_command == "check":
            payload = {
                "repo_root": str(config.repo_root),
                "registry_root": str(config.registry_root),
                "config_root": str(config.config_root),
                "loaded_config_files": [
                    str(path) for path in config.loaded_files
                ],
                "registry_root_exists": config.registry_root.exists(),
            }

            if args.json:
                _print_json(payload)
            else:
                print("Aegis OS Runtime Configuration Check")
                print(f"Repository root: {payload['repo_root']}")
                print(f"Registry root: {payload['registry_root']} "
                      f"(exists: {payload['registry_root_exists']})")
                print(f"Config root: {payload['config_root']}")
                print(
                    "Loaded config files: "
                    + (
                        ", ".join(payload["loaded_config_files"])
                        if payload["loaded_config_files"]
                        else "-"
                    )
                )

            if not payload["registry_root_exists"]:
                return EXIT_REPOSITORY

            return EXIT_OK

    if args.command == "execution":
        return _handle_execution(
            args,
            resolver,
            config,
        )

    if args.command == "validate":
        validator = RegistryValidator(
            config.repo_root,
            unresolved_related_as_error=(
                args.strict_related
            ),
        )
        report = validator.validate(
            documents
        )

        if args.json:
            _print_json(report.to_dict())
        else:
            print("Aegis OS Runtime Validation")
            print(f"Registries: {report.registry_count}")
            print(f"Assets: {report.asset_count}")
            print(f"Errors: {len(report.errors)}")
            print(f"Warnings: {len(report.warnings)}")

            for issue in report.issues:
                location = ""

                if issue.asset_id:
                    location += (
                        f" asset={issue.asset_id}"
                    )

                if issue.source_file:
                    location += (
                        f" file={issue.source_file}"
                    )

                print(
                    f"[{issue.severity.upper()}] "
                    f"{issue.code}: {issue.message}"
                    f"{location}"
                )

            print(
                "Validation passed."
                if report.ok
                else "Validation failed."
            )

        return (
            EXIT_OK
            if report.ok
            else EXIT_VALIDATION
        )

    if args.command == "doctor":
        checks = run_all_checks(config.repo_root)
        checks_ok = all(check.ok for check in checks)

        validation_report = None
        if not args.skip_validate:
            validator = RegistryValidator(config.repo_root)
            validation_report = validator.validate(documents)

        generated_reports: list[str] = []
        if not args.skip_reports and checks_ok:
            registry_files = loader.registry_files()
            generated_reports = [
                item.name
                for item in generate_all_reports(
                    resolver,
                    config.repo_root,
                    registry_files,
                )
            ]

        if args.json:
            _print_json(
                {
                    "checks": [check.to_dict() for check in checks],
                    "checks_ok": checks_ok,
                    "validation": (
                        validation_report.to_dict()
                        if validation_report is not None
                        else None
                    ),
                    "reports_generated": generated_reports,
                }
            )
        else:
            print("Aegis OS - Doctor")
            print("Running repository health checks...")

            for check in checks:
                print("")
                print(f"Running {check.name}...")

                for warning in check.warnings:
                    print(f"WARN {warning}")

                if check.ok:
                    print(f"{check.name} passed.")
                else:
                    print(f"{check.name} failed.")
                    for failure in check.failures:
                        print(f"- {failure}")

            if validation_report is not None:
                print("")
                print("Running registry validation...")
                print(
                    "Registry validation passed."
                    if validation_report.ok
                    else "Registry validation failed."
                )

            if generated_reports:
                print("")
                print("Generating registry reports...")
                for name in generated_reports:
                    print(f"Generated: {name}")

            print("")
            if checks_ok and (
                validation_report is None or validation_report.ok
            ):
                print("Aegis OS Doctor completed successfully.")
            else:
                print("Aegis OS Doctor found problems.")

        doctor_ok = checks_ok and (
            validation_report is None or validation_report.ok
        )
        return EXIT_OK if doctor_ok else EXIT_VALIDATION

    if args.command == "report":
        if args.report_command == "generate":
            registry_files = loader.registry_files()

            if args.name == "all":
                generated = generate_all_reports(
                    resolver,
                    config.repo_root,
                    registry_files,
                )
            else:
                generated = [
                    generate_report(
                        args.name,
                        resolver,
                        config.repo_root,
                        registry_files,
                    )
                ]

            if args.json:
                _print_json([item.to_dict() for item in generated])
            else:
                print("Aegis OS - Generate Reports")
                for item in generated:
                    print(f"Generated: {item.name} -> {item.path}")

            return EXIT_OK

    parser.print_help()
    return EXIT_USAGE


if __name__ == "__main__":
    raise SystemExit(main())