## FILE: `scripts/doctor/check-required-indexes.ps1`

```powershell
<#
.SYNOPSIS
Checks required Aegis OS index and manifest files.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\doctor\check-required-indexes.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Required Indexes Check" -ForegroundColor Cyan

$requiredFiles = @(
    "MANIFEST.md",
    "docs\INDEX.md",
    "skills\INDEX.md",
    "playbooks\INDEX.md",
    "patterns\INDEX.md",
    "templates\INDEX.md",
    "registry\INDEX.md",
    "reports\README.md",
    "scripts\README.md"
)

$failures = @()

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "OK  $file" -ForegroundColor Green
    }
    else {
        Write-Host "BAD $file" -ForegroundColor Red
        $failures += $file
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "Missing required files:" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "- $_" -ForegroundColor Red }
    exit 1
}

Write-Host "Required indexes check passed." -ForegroundColor Green
exit 0
```
