## FILE: `cli/commands/validate.ps1`

```powershell
<#
.SYNOPSIS
Runs Aegis OS validation.
#>

$ErrorActionPreference = "Stop"

$scriptPath = "scripts\validation\validate-all.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Validation script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE
```
