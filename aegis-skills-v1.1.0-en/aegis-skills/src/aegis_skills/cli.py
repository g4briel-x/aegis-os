from __future__ import annotations

import argparse
from pathlib import Path

from .builder import build_archives
from .discovery import discover_skills
from .reporting import validation_json, validation_markdown
from .validation import validate_repository


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aegis-skills")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="validate the repository")
    validate.add_argument("--root", type=Path, default=Path.cwd())
    validate.add_argument("--strict", action="store_true")
    validate.add_argument("--check-dist", action="store_true")
    validate.add_argument(
        "--format",
        choices=("text", "markdown", "json"),
        default="text",
    )
    validate.add_argument("--output", type=Path)

    build = sub.add_parser("build", help="build standalone Claude skill ZIP files")
    build.add_argument("--root", type=Path, default=Path.cwd())
    build.add_argument("--clean", action="store_true")

    inventory = sub.add_parser("inventory", help="list discovered skills")
    inventory.add_argument("--root", type=Path, default=Path.cwd())
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "validate":
        result = validate_repository(
            args.root,
            check_dist=args.check_dist,
            strict=args.strict,
        )
        if args.format == "markdown":
            output = validation_markdown(result)
        elif args.format == "json":
            output = validation_json(result)
        else:
            status = "PASS" if result.is_valid else "FAIL"
            output = (
                f"skills={result.skills_checked} errors={len(result.errors)} "
                f"warnings={len(result.warnings)} status={status}\n"
            )
            for issue in result.issues:
                output += (
                    f"{issue.severity.upper()} {issue.code} {issue.path}: "
                    f"{issue.message}\n"
                )
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
        return 0 if result.is_valid else 1
    if args.command == "build":
        archives = build_archives(args.root, clean=args.clean)
        print(f"built {len(archives)} skill archives")
        return 0
    if args.command == "inventory":
        for record in discover_skills(args.root):
            relative = record.directory.relative_to(args.root)
            print(f"{record.name}\t{record.manifest.get('version', '')}\t{relative}")
        return 0
    return 2
