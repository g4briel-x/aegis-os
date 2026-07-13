## FILE: `cli/commands/report.ps1`

```powershell
<#
.SYNOPSIS
Generates Aegis OS registry reports.
#>

$ErrorActionPreference = "Stop"

$scriptPath = "scripts\reports\generate-all-reports.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Report script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE
```