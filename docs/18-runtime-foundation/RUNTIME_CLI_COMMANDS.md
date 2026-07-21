# Runtime CLI Commands

Version: v0.6.0  
Status: usable

## Role of this file

This file documents the runtime commands available through the Aegis OS PowerShell CLI and the Python runtime CLI.

## PowerShell runtime commands

### runtime:status

Role: display the Python runtime status from the PowerShell CLI.

```powershell
.\cli\aegis.ps1 runtime:status
```

Expected output includes:

```text
Aegis OS Runtime Status
Version: 0.6.0
Repository: <local repository path>
Registries: 9
Assets: <asset count>
```

### runtime:registry-list

Role: list registry files using the Python runtime.

```powershell
.\cli\aegis.ps1 runtime:registry-list
```

Expected output includes each registry file, the number of loaded assets and the number of YAML errors.

### runtime:asset-find

Role: search assets using the Python runtime resolver.

```powershell
.\cli\aegis.ps1 runtime:asset-find security
```

This command searches across IDs, names, types, domains, paths, tags and relations.

### runtime:asset-show

Role: display one asset using the Python runtime resolver.

```powershell
.\cli\aegis.ps1 runtime:asset-show security.review-api-security
```

Expected output includes:

```text
ID
Name
Type
Domain
Path
Tags
Related assets
Registry
```

### runtime:validate

Role: validate registries using the Python runtime validator.

```powershell
.\cli\aegis.ps1 runtime:validate
```

The command passes when there are no blocking validation errors.

Warnings are displayed but do not block v0.6 validation.

## Direct Python commands

The same operations can be run directly with Python:

```powershell
python -m aegis_runtime version
python -m aegis_runtime status
python -m aegis_runtime registry list
python -m aegis_runtime asset find security
python -m aegis_runtime asset show security.review-api-security
python -m aegis_runtime validate
```

## Environment requirement

The runtime should be executed from the repository virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If the virtual environment is not activated, the system Python may not find:

```text
pytest
aegis_runtime
```

## Recommended validation sequence

```powershell
python -m pytest tests\runtime -q
.\cli\aegis.ps1 runtime:status
.\cli\aegis.ps1 runtime:registry-list
.\cli\aegis.ps1 runtime:asset-find security
.\cli\aegis.ps1 runtime:asset-show security.review-api-security
.\cli\aegis.ps1 runtime:validate
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
```
