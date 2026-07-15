<#
.SYNOPSIS
Generates all Aegis OS registry reports.

.DESCRIPTION
Runs all report generation scripts from scripts/reports.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\reports\generate-all-reports.ps1
#>

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
Write-Host "Aegis OS - Generate All Reports" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

$reports = @(
    "generate-registry-summary.ps1",
    "generate-asset-map.ps1",
    "generate-domain-report.ps1",
    "generate-release-report.ps1"
)

foreach ($report in $reports) {
    $reportPath = Join-Path $scriptRoot $report

    if (-not (Test-Path $reportPath)) {
        Write-Error "Report script missing: $reportPath"
        exit 1
    }

    Write-Host ""
    Write-Host "Running $report..." -ForegroundColor Yellow

    & $PSExe -ExecutionPolicy Bypass -File $reportPath

    if ($LASTEXITCODE -ne 0) {
        Write-Error "$report failed."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "All reports generated successfully." -ForegroundColor Green
exit 0