<#
.SYNOPSIS
Runs Aegis OS doctor.
#>

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
$scriptPath = "scripts\doctor\aegis-doctor.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Doctor script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& $PSExe -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE