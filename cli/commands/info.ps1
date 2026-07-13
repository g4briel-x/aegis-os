## FILE: `cli/commands/info.ps1`

```powershell
<#
.SYNOPSIS
Shows Aegis OS project information.

.USAGE
.\cli\aegis.ps1 info
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Project Info" -ForegroundColor Cyan
Write-Host ""

Write-Host "Identity:" -ForegroundColor Yellow
Write-Host "  Name: Aegis OS"
Write-Host "  Type: AI operating framework"
Write-Host "  Stage: CLI foundation"
Write-Host ""

Write-Host "Core Paths:" -ForegroundColor Yellow

$paths = @(
    "core",
    "shared",
    "docs",
    "skills",
    "playbooks",
    "patterns",
    "templates",
    "registry",
    "scripts",
    "cli",
    "config",
    "reports"
)

foreach ($path in $paths) {
    if (Test-Path $path) {
        Write-Host "  OK   $path" -ForegroundColor Green
    }
    else {
        Write-Host "  MISS $path" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Entrypoints:" -ForegroundColor Yellow

$entrypoints = @(
    "cli\aegis.ps1",
    "scripts\doctor\aegis-doctor.ps1",
    "scripts\validation\validate-all.ps1",
    "scripts\reports\generate-all-reports.ps1",
    "scripts\testing\test-cli-smoke.ps1"
)

foreach ($entrypoint in $entrypoints) {
    if (Test-Path $entrypoint) {
        Write-Host "  OK   $entrypoint" -ForegroundColor Green
    }
    else {
        Write-Host "  MISS $entrypoint" -ForegroundColor Yellow
    }
}

exit 0
```