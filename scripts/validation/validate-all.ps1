## FILE: `scripts/validation/validate-all.ps1`

```powershell
<#
.SYNOPSIS
Runs all available Aegis OS validation checks.

.DESCRIPTION
This is the main validation entrypoint for the repository.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Full Validation" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

$registryValidation = Join-Path $scriptRoot "validate-registry.ps1"

if (-not (Test-Path $registryValidation)) {
    Write-Error "Registry validation entrypoint missing: $registryValidation"
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $registryValidation

if ($LASTEXITCODE -ne 0) {
    Write-Error "Full validation failed."
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "All validation checks passed." -ForegroundColor Green
exit 0
```
