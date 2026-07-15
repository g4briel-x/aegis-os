
<#
.SYNOPSIS
Generates Aegis OS registry reports.
#>

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
$scriptPath = "scripts\reports\generate-all-reports.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Report script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& $PSExe -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE