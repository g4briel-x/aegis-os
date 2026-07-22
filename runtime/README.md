# Aegis Runtime

The runtime is the single Python implementation of the Aegis OS command line.
It loads and validates registries, resolves assets, generates reports and
skills, and manages safe execution sessions.

## Install

```console
python -m pip install -e "./runtime[dev]"
```

## Entrypoints

```console
aegis version
aegis-runtime version
python -m aegis_runtime version
```

The three entrypoints are equivalent. Repository operations accept a global
`--repo-root` option and machine-readable output through global `--json`.

```console
aegis --repo-root . --json status
aegis --repo-root . validate --strict-related
python -m pytest tests/runtime
```

The package requires Python 3.11+ and PyYAML. Development installs also include
pytest.
