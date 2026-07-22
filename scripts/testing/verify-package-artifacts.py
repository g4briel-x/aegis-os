"""Verify that Aegis OS build artifacts contain the runtime and CLI metadata."""

from __future__ import annotations

import sys
import tarfile
from pathlib import Path
from zipfile import ZipFile


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _verify_wheel(path: Path) -> None:
    with ZipFile(path) as archive:
        names = set(archive.namelist())
        metadata_name = next(
            (name for name in names if name.endswith(".dist-info/METADATA")),
            None,
        )
        metadata = archive.read(metadata_name).decode("utf-8") if metadata_name else ""
    _require("aegis_runtime/cli.py" in names, "Wheel is missing aegis_runtime/cli.py")
    _require("aegis_runtime/py.typed" in names, "Wheel is missing py.typed")
    _require(
        metadata_name is not None,
        "Wheel is missing package metadata.",
    )
    _require(
        "License-Expression: LicenseRef-Aegis-OS-BSL-1.1" in metadata,
        "Wheel has an unexpected license expression.",
    )
    _require(
        any(name.endswith(".dist-info/entry_points.txt") for name in names),
        "Wheel is missing console entry points.",
    )


def _verify_sdist(path: Path) -> None:
    with tarfile.open(path, "r:gz") as archive:
        names = archive.getnames()
    _require(
        any(name.endswith("/src/aegis_runtime/cli.py") for name in names),
        "Source distribution is missing aegis_runtime/cli.py",
    )
    _require(
        any(name.endswith("/pyproject.toml") for name in names),
        "Source distribution is missing pyproject.toml.",
    )


def main(argv: list[str] | None = None) -> int:
    arguments = argv if argv is not None else sys.argv[1:]
    if len(arguments) != 1:
        print("Usage: verify-package-artifacts.py <dist-directory>", file=sys.stderr)
        return 2

    dist_dir = Path(arguments[0])
    wheels = sorted(dist_dir.glob("*.whl"))
    sdists = sorted(dist_dir.glob("*.tar.gz"))
    try:
        _require(len(wheels) == 1, "Expected exactly one wheel artifact.")
        _require(len(sdists) == 1, "Expected exactly one source distribution artifact.")
        _verify_wheel(wheels[0])
        _verify_sdist(sdists[0])
    except (OSError, ValueError, tarfile.TarError) as exc:
        print(f"Package verification failed: {exc}", file=sys.stderr)
        return 1

    print(f"Verified wheel: {wheels[0].name}")
    print(f"Verified source distribution: {sdists[0].name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
