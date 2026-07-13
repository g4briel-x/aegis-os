## FILE: `scripts/doctor/aegis-doctor.ps1`

```powershell
<#
.SYNOPSIS
Runs the Aegis OS repository health check.

.DESCRIPTION
Runs structure checks, required index checks, Git status, registry validation and report generation when available.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\doctor\aegis-doctor.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Doctor" -ForegroundColor Cyan
Write-Host "Running repository health checks..." -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

$checks = @(
    "check-repository-structure.ps1",
    "check-required-indexes.ps1",
    "check-git-status.ps1"
)

foreach ($check in $checks) {
    $checkPath = Join-Path $scriptRoot $check

    if (-not (Test-Path $checkPath)) {
        Write-Error "Doctor check missing: $checkPath"
        exit 1
    }

    Write-Host ""
    Write-Host "Running $check..." -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File $checkPath

    if ($LASTEXITCODE -ne 0) {
        Write-Error "$check failed."
        exit $LASTEXITCODE
    }
}

$validationScript = "scripts\validation\validate-all.ps1"

if (Test-Path $validationScript) {
    Write-Host ""
    Write-Host "Running registry validation..." -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File $validationScript

    if ($LASTEXITCODE -ne 0) {
        Write-Error "Registry validation failed."
        exit $LASTEXITCODE
    }
}
else {
    Write-Host "WARN Validation script not found: $validationScript" -ForegroundColor Yellow
}

$reportScript = "scripts\reports\generate-all-reports.ps1"

if (Test-Path $reportScript) {
    Write-Host ""
    Write-Host "Generating registry reports..." -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File $reportScript

    if ($LASTEXITCODE -ne 0) {
        Write-Error "Report generation failed."
        exit $LASTEXITCODE
    }
}
else {
    Write-Host "WARN Report script not found: $reportScript" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Aegis OS Doctor completed successfully." -ForegroundColor Green
exit 0
```