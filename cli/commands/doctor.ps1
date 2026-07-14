<#
.SYNOPSIS
Runs Aegis OS doctor.
#>

$ErrorActionPreference = "Stop"

$scriptPath = "scripts\doctor\aegis-doctor.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Doctor script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE