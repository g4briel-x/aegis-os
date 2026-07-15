<#
.SYNOPSIS
Runs all available Aegis OS validation checks.

.DESCRIPTION
This is the main validation entrypoint for the repository.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
#>

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
Write-Host "Aegis OS - Full Validation" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

$registryValidation = Join-Path $scriptRoot "validate-registry.ps1"

if (-not (Test-Path $registryValidation)) {
    Write-Error "Registry validation entrypoint missing: $registryValidation"
    exit 1
}

Write-Host ""
Write-Host "Running registry validation..." -ForegroundColor Yellow

& $PSExe -ExecutionPolicy Bypass -File $registryValidation

if ($LASTEXITCODE -ne 0) {
    Write-Error "Full validation failed."
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "All validation checks passed." -ForegroundColor Green
exit 0