"""Install a built Aegis wheel in a clean environment and exercise its CLIs."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import venv
from pathlib import Path


def _run(command: list[str]) -> str:
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def main(argv: list[str] | None = None) -> int:
    arguments = argv if argv is not None else sys.argv[1:]
    if len(arguments) != 1:
        print("Usage: verify-package-install.py <dist-directory>", file=sys.stderr)
        return 2

    wheels = sorted(Path(arguments[0]).glob("*.whl"))
    if len(wheels) != 1:
        print("Expected exactly one wheel artifact.", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory(prefix="aegis-wheel-check-") as temporary:
        environment = Path(temporary) / "venv"
        venv.EnvBuilder(with_pip=True).create(environment)
        scripts = environment / ("Scripts" if sys.platform == "win32" else "bin")
        python = scripts / ("python.exe" if sys.platform == "win32" else "python")
        aegis = scripts / ("aegis.exe" if sys.platform == "win32" else "aegis")
        aegis_runtime = scripts / (
            "aegis-runtime.exe" if sys.platform == "win32" else "aegis-runtime"
        )

        _run([str(python), "-m", "pip", "install", "--disable-pip-version-check", str(wheels[0])])
        module_output = _run([str(python), "-m", "aegis_runtime", "version"])
        aegis_output = _run([str(aegis), "version"])
        runtime_output = _run([str(aegis_runtime), "version"])

    if not all("Aegis OS Runtime" in output for output in (module_output, aegis_output, runtime_output)):
        print("Installed CLI entry points did not report the runtime version.", file=sys.stderr)
        return 1

    print(f"Installed and exercised wheel: {wheels[0].name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
