## FILE: `scripts/doctor/check-repository-structure.ps1`

```powershell
<#
.SYNOPSIS
Checks required Aegis OS repository folders.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\doctor\check-repository-structure.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Repository Structure Check" -ForegroundColor Cyan

$requiredFolders = @(
    "core",
    "shared",
    "docs",
    "skills",
    "playbooks",
    "patterns",
    "templates",
    "registry",
    "scripts",
    "scripts\validation",
    "scripts\reports"
)

$failures = @()

foreach ($folder in $requiredFolders) {
    if (Test-Path $folder) {
        Write-Host "OK  $folder" -ForegroundColor Green
    }
    else {
        Write-Host "BAD $folder" -ForegroundColor Red
        $failures += $folder
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "Missing folders:" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "- $_" -ForegroundColor Red }
    exit 1
}

Write-Host "Repository structure check passed." -ForegroundColor Green
exit 0
```
