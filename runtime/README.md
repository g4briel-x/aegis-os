# Aegis OS Runtime

Version: 0.6.0

The Aegis OS Runtime is the Python execution foundation used to load, inspect,
resolve, and validate Aegis registries.

## Requirements

- Python 3.11 or newer
- Aegis OS repository checked out locally

## Installation

From the Aegis OS repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".\runtime[dev]"
```

## Commands

```powershell
python -m aegis_runtime version
python -m aegis_runtime status
python -m aegis_runtime registry list
python -m aegis_runtime asset show security.review-api-security
python -m aegis_runtime asset find security
python -m aegis_runtime asset domain security
python -m aegis_runtime asset tag api
python -m aegis_runtime validate
```

The installed console command is also available:

```powershell
aegis-runtime version
```

## Repository discovery

The runtime resolves the Aegis repository in this order:

1. `--repo-root`
2. `AEGIS_HOME`
3. The current directory and its parents
4. The package location and its parents

A valid repository contains at least a `registry` directory.

## Validation policy

The v0.6 validator treats malformed YAML, missing IDs, duplicate IDs, and
missing declared paths as errors. Unresolved `related_assets` references are
warnings in v0.6.
