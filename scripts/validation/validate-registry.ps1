<#
.SYNOPSIS
Runs core registry validations.

.DESCRIPTION
Executes YAML, path, id and related asset validation scripts.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-registry.ps1
#>

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
Write-Host "Aegis OS - Registry Validation" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

$checks = @(
    "validate-yaml.ps1",
    "validate-paths.ps1",
    "validate-ids.ps1",
    "validate-related-assets.ps1"
)

foreach ($check in $checks) {
    $checkPath = Join-Path $scriptRoot $check

    if (-not (Test-Path $checkPath)) {
        Write-Error "Validation script missing: $checkPath"
        exit 1
    }

    Write-Host ""
    Write-Host "Running $check..." -ForegroundColor Yellow

    & $PSExe -ExecutionPolicy Bypass -File $checkPath

    if ($LASTEXITCODE -ne 0) {
        Write-Error "$check failed."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "Registry validation passed." -ForegroundColor Green
exit 0