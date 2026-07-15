# Aegis OS CLI Runtime Commands

Version: v0.6.0  
Status: usable

## Role of this file

This file is the official CLI reference for PowerShell commands that delegate to the Python runtime.

## Command list

```text
runtime:status
runtime:validate
runtime:registry-list
runtime:asset-find
runtime:asset-show
```

## runtime:status

Role: show the Python runtime status.

```powershell
.\cli\aegis.ps1 runtime:status
```

## runtime:validate

Role: validate registries through the Python runtime.

```powershell
.\cli\aegis.ps1 runtime:validate
```

## runtime:registry-list

Role: list registries using the Python runtime.

```powershell
.\cli\aegis.ps1 runtime:registry-list
```

## runtime:asset-find

Role: search assets using the Python runtime.

```powershell
.\cli\aegis.ps1 runtime:asset-find security
```

## runtime:asset-show

Role: show one asset using the Python runtime.

```powershell
.\cli\aegis.ps1 runtime:asset-show security.review-api-security
```

## Runtime bridge behavior

The PowerShell command files are located in:

```text
cli/commands
```

Runtime bridge command files:

```text
runtime-status.ps1
runtime-validate.ps1
runtime-registry-list.ps1
runtime-asset-find.ps1
runtime-asset-show.ps1
```

Each bridge command resolves the repository root, selects the local `.venv` Python executable when available, then delegates to:

```powershell
python -m aegis_runtime
```

## Recommended smoke test

```powershell
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-runtime-commands.ps1
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```