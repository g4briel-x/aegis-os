"""Command-line interface for the Aegis runtime."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from . import __version__
from .asset_resolver import AssetResolver
from .config import AegisConfig
from .models import Asset
from .registry_loader import RegistryLoader
from .validator import RegistryValidator
from .execution import (
    ExecutionContextBuilder,
    ExecutionMode,
    ExecutionSessionBuilder,
    ExecutionWorkspaceStore,
)

from .execution.planner import ExecutionPlanner
from .execution.runner import ExecutionRunner
from .execution.contract_builder import ExecutionContractBuilder
from .execution.contract_validator import ExecutionContractValidator

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_REPOSITORY = 3
EXIT_VALIDATION = 4
EXIT_NOT_FOUND = 5


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aegis-runtime", description="Aegis OS Python runtime")
    parser.add_argument("--repo-root", type=Path, help="Path to the Aegis OS repository root.")
    parser.add_argument("--json", action="store_true", help="Render JSON output.")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("version", help="Show runtime version.")
    commands.add_parser("status", help="Show repository runtime status.")

    registry = commands.add_parser("registry", help="Registry operations.")
    registry_commands = registry.add_subparsers(dest="registry_command", required=True)
    registry_commands.add_parser("list", help="List registry files.")

    asset = commands.add_parser("asset", help="Asset operations.")
    asset_commands = asset.add_subparsers(dest="asset_command", required=True)
    asset_show = asset_commands.add_parser("show", help="Show one asset.")
    asset_show.add_argument("asset_id")
    asset_find = asset_commands.add_parser("find", help="Search assets.")
    asset_find.add_argument("query")
    asset_domain = asset_commands.add_parser("domain", help="List assets in a domain.")
    asset_domain.add_argument("domain")
    asset_tag = asset_commands.add_parser("tag", help="List assets with a tag.")
    asset_tag.add_argument("tag")

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
        help="Runtime input parameter. May be supplied multiple times.",
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
        help="Runtime input parameter. May be supplied multiple times.",
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

    validate = commands.add_parser("validate", help="Validate registries.")
    validate.add_argument(
        "--strict-related",
        action="store_true",
        help="Treat unresolved related assets as errors.",
    )
    return parser


def _config_from_args(args: argparse.Namespace) -> AegisConfig:
    return AegisConfig.discover(args.repo_root if args.repo_root else None)


def _print_asset(asset: Asset, *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(asset.to_dict(), indent=2, ensure_ascii=False))
        return
    print(f"ID: {asset.id}")
    print(f"Name: {asset.name or '-'}")
    print(f"Type: {asset.type or '-'}")
    print(f"Domain: {asset.domain or '-'}")
    print(f"Path: {asset.path or '-'}")
    print(f"Tags: {', '.join(asset.tags) if asset.tags else '-'}")
    print("Related assets: " + (", ".join(asset.related_assets) if asset.related_assets else "-"))
    if asset.source_file:
        print(f"Registry: {asset.source_file}")


def _print_asset_list(assets: list[Asset], *, as_json: bool) -> None:
    if as_json:
        print(json.dumps([asset.to_dict() for asset in assets], indent=2, ensure_ascii=False))
        return
    for asset in assets:
        details = [asset.id]
        if asset.domain:
            details.append(f"domain={asset.domain}")
        if asset.type:
            details.append(f"type={asset.type}")
        print(" | ".join(details))
    print(f"Total assets: {len(assets)}")


def _parse_execution_inputs(values: list[str]) -> dict[str, str]:
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
                f"Execution input '{name}' was provided more than once."
            )

        parameters[name] = value

    return parameters


def _print_execution_plan(plan, *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(plan.to_dict(), indent=2, ensure_ascii=False))
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


def _print_execution_report(report, *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
        return

    print("Aegis OS Execution Dry Run")
    print(f"Status: {report.status.value}")
    print(f"Message: {report.message}")
    print("")

    _print_execution_plan(report.plan, as_json=False)


def _print_execution_contract_result(result, *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
        return

    contract = result.contract

    print("Aegis OS Execution Contract")
    print(f"Asset: {contract.asset_id}")
    print(f"Type: {contract.contract_type.value}")
    print(f"Safety: {contract.safety_level.value}")
    print(f"Allowed modes: {', '.join(contract.allowed_modes)}")
    print("")

    print("Inputs:")
    if contract.inputs:
        for item in contract.inputs:
            required = "required" if item.required else "optional"
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

    print(f"Validation: {'passed' if result.ok else 'failed'}")
    print(f"Errors: {len(result.errors)}")
    print(f"Warnings: {len(result.warnings)}")

    for issue in result.issues:
        print(f"[{issue.severity.upper()}] {issue.code}: {issue.message}")



def _print_execution_context_result(
    result,
    *,
    as_json: bool,
) -> None:
    """Print one execution context build result."""

    if as_json:
        print(
            json.dumps(
                result.to_dict(),
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    context = result.context

    print("Aegis OS Execution Context")
    print(f"Target: {context.target_asset_id}")
    print(f"Mode: {context.mode.value}")
    print(f"Build: {'passed' if result.ok else 'failed'}")
    print("")

    print("Resolved inputs:")
    if context.resolved_inputs:
        for item in context.resolved_inputs:
            required = "required" if item.required else "optional"
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
        f"- Python: {context.environment.python_version}"
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
        f"Input resolution: "
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

        print(
            json.dumps(
                payload,
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    session = result.session
    workspace = result.workspace

    print("Aegis OS Execution Session")
    print(f"Session: {session.session_id}")
    print(f"Target: {session.target_asset_id}")
    print(f"Mode: {session.mode.value}")
    print(f"State: {session.state.value}")
    print(f"Build: {'passed' if result.ok else 'failed'}")
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
        print(
            json.dumps(
                record.to_dict(),
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    payload = record.payload
    session = payload.get("session", {})
    workspace = payload.get("workspace", {})
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


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "version":
        payload = {"name": "Aegis Runtime", "version": __version__}
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print("Aegis OS Runtime")
            print(f"Version: {__version__}")
        return EXIT_OK

    try:
        config = _config_from_args(args)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Repository error: {exc}", file=sys.stderr)
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
            "loaded_config_files": [str(path) for path in config.loaded_files],
        }
        if args.json:
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print("Aegis OS Runtime Status")
            print(f"Version: {payload['version']}")
            print(f"Repository: {payload['repo_root']}")
            print(f"Registries: {payload['registry_count']}")
            print(f"Assets: {payload['asset_count']}")
        return EXIT_OK

    if args.command == "registry" and args.registry_command == "list":
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
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            for item in payload:
                print(
                    f"{item['name']} | assets={item['assets']} | "
                    f"errors={item['errors']} | {item['path']}"
                )
            print(f"Total registries: {len(payload)}")
        return EXIT_OK

    if args.command == "asset":
        if args.asset_command == "show":
            asset = resolver.by_id(args.asset_id)
            if asset is None:
                print(f"Asset not found: {args.asset_id}", file=sys.stderr)
                return EXIT_NOT_FOUND
            _print_asset(asset, as_json=args.json)
            return EXIT_OK
        if args.asset_command == "find":
            _print_asset_list(resolver.find(args.query), as_json=args.json)
            return EXIT_OK
        if args.asset_command == "domain":
            _print_asset_list(resolver.by_domain(args.domain), as_json=args.json)
            return EXIT_OK
        if args.asset_command == "tag":
            _print_asset_list(resolver.by_tag(args.tag), as_json=args.json)
            return EXIT_OK

    if args.command == "execution":
        planner = ExecutionPlanner(resolver)

        try:
            if args.execution_command == "plan":
                plan = planner.create_plan(
                    args.asset_id,
                    mode=ExecutionMode.PLAN,
                )
                _print_execution_plan(plan, as_json=args.json)
                return EXIT_OK

            if args.execution_command == "dry-run":
                runner = ExecutionRunner(planner)
                report = runner.dry_run(args.asset_id)
                _print_execution_report(report, as_json=args.json)
                return EXIT_OK

            if args.execution_command == "contract":
                asset = resolver.require(args.asset_id)
                builder = ExecutionContractBuilder()
                validator = ExecutionContractValidator()
                contract = builder.build_from_asset(asset)
                result = validator.validate(contract)
                _print_execution_contract_result(result, as_json=args.json)
                return EXIT_OK if result.ok else EXIT_VALIDATION

            if args.execution_command == "context":
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

            if args.execution_command == "session-show":
                store = ExecutionWorkspaceStore(
                    config.repo_root
                )

                try:
                    record = store.load(
                        args.identifier
                    )
                except FileNotFoundError as exc:
                    print(
                        str(exc),
                        file=sys.stderr,
                    )
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


            if args.execution_command == "session":
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

        except KeyError as exc:
            print(str(exc), file=sys.stderr)
            return EXIT_NOT_FOUND

    if args.command == "validate":
        validator = RegistryValidator(
            config.repo_root,
            unresolved_related_as_error=args.strict_related,
        )
        report = validator.validate(documents)
        if args.json:
            print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
        else:
            print("Aegis OS Runtime Validation")
            print(f"Registries: {report.registry_count}")
            print(f"Assets: {report.asset_count}")
            print(f"Errors: {len(report.errors)}")
            print(f"Warnings: {len(report.warnings)}")
            for issue in report.issues:
                location = ""
                if issue.asset_id:
                    location += f" asset={issue.asset_id}"
                if issue.source_file:
                    location += f" file={issue.source_file}"
                print(f"[{issue.severity.upper()}] {issue.code}: {issue.message}{location}")
            print("Validation passed." if report.ok else "Validation failed.")
        return EXIT_OK if report.ok else EXIT_VALIDATION

    parser.print_help()
    return EXIT_USAGE


if __name__ == "__main__":
    raise SystemExit(main())
