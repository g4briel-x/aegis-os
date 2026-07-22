# Aegis OS

Aegis OS is a registry-driven knowledge and execution framework. Version 0.7
uses one cross-platform Python CLI for discovery, validation, reporting,
generation and execution lifecycle operations.

## Install

Python 3.11 or newer is required.

```console
python -m pip install -e "./runtime[dev]"
```

The package installs two equivalent commands: `aegis` and `aegis-runtime`.
Every command is also available through `python -m aegis_runtime`.

## Start

```console
aegis --repo-root . info
aegis --repo-root . status
aegis --repo-root . registry list
aegis --repo-root . docs list
aegis --repo-root . asset find security
aegis --repo-root . asset search security --domain security --type skill --tag security
aegis --repo-root . asset show security.review-api-security
```

## Validate and test

```console
python -m pytest tests/runtime
aegis --repo-root . validate --strict-related
aegis --repo-root . doctor --skip-reports
aegis --repo-root . report generate all
```

The GitHub workflow repeats these checks on Linux, Windows and macOS.

## Generate a skill

```console
aegis --repo-root . generate skill generators/my-new-skill.yaml
aegis --repo-root . generate skills --definitions path/to/new-definitions
```

Generation refuses to overwrite tracked files. Pass `--force` only after
reviewing the target skill.

## Execute an asset

```console
aegis --repo-root . execution plan security.review-api-security
aegis --repo-root . execution contract security.review-api-security
aegis --repo-root . execution context security.review-api-security
aegis --repo-root . execution session security.review-api-security
```

Execution begins in safe planning and dry-run modes. Persisted sessions,
orchestration, lifecycle transitions and audit verification are documented in
[`docs/19-execution-foundation`](docs/19-execution-foundation).

## Repository map

- `runtime/`: Python package and command implementation
- `tests/runtime/`: unit and repository regression tests
- `registry/`: machine-readable asset catalogs
- `skills/`, `playbooks/`, `patterns/`, `templates/`: executable knowledge
- `docs/`: architecture and operating documentation
- `reports/registry/`: generated registry reports
- `generators/`: YAML definitions consumed by the Python generator

See [`QUICKSTART.md`](QUICKSTART.md), [`cli/README.md`](cli/README.md) and
[`CONTRIBUTING.md`](CONTRIBUTING.md) for the operating workflow.
