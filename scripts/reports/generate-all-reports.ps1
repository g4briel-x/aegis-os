## FILE: `scripts/reports/generate-all-reports.ps1`

```powershell
<#
.SYNOPSIS
Generates all Aegis OS reports.
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Generating All Reports" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

$reportScripts = @(
    "generate-registry-summary.ps1",
    "generate-asset-map.ps1",
    "generate-domain-report.ps1",
    "generate-release-report.ps1"
)

foreach ($script in $reportScripts) {
    $scriptPath = Join-Path $scriptRoot $script

    if (-not (Test-Path $scriptPath)) {
        Write-Error "Report script missing: $scriptPath"
        exit 1
    }

    Write-Host ""
    Write-Host "Running $script..." -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File $scriptPath

    if ($LASTEXITCODE -ne 0) {
        Write-Error "$script failed."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "All reports generated successfully." -ForegroundColor Green
exit 0
```