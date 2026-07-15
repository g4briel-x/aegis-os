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
