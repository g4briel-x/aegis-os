<#
.SYNOPSIS
Checks required Aegis OS repository folders.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\doctor\check-repository-structure.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS - Repository Structure Check" -ForegroundColor Cyan

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
    "scripts\reports",
    "scripts\doctor",
    "scripts\testing",
    "cli",
    "cli\commands",
    "config",
    "reports",
    "install",
    ".github",
    ".github\workflows"
)

$failures = [System.Collections.Generic.List[object]]::new()

foreach ($folder in $requiredFolders) {
    if (Test-Path $folder) {
        Write-Host "OK  $folder" -ForegroundColor Green
    }
    else {
        Write-Host "BAD $folder" -ForegroundColor Red
        $failures.Add($folder)
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "Missing folders:" -ForegroundColor Red

    foreach ($failure in $failures) {
        Write-Host "- $failure" -ForegroundColor Red
    }

    exit 1
}

Write-Host ""
Write-Host "Repository structure check passed." -ForegroundColor Green
exit 0