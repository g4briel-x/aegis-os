# Install the Aegis CLI

The CLI is distributed by the Python package in `runtime/`; no shell profile
modification is required.

From the repository root:

```console
python -m pip install -e "./runtime[dev]"
aegis version
aegis --repo-root . status
```

For an isolated environment, create a virtual environment with
`python -m venv .venv`, run its Python executable directly, and install the
package with `-m pip`. The installed `aegis` launcher is placed in that
environment's standard scripts directory.

Uninstall with:

```console
python -m pip uninstall aegis-runtime
```
