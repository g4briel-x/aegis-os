## FILE: `cli/commands/config-check.ps1`

```powershell
<#
.SYNOPSIS
Checks Aegis OS configuration file presence.

.USAGE
.\cli\aegis.ps1 config:check
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Configuration Check" -ForegroundColor Cyan

$requiredFiles = @(
    "config\aegis.config.example.yaml",
    "config\aegis.config.local.example.yaml"
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
    Write-Host "Missing configuration files:" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "- $_" -ForegroundColor Red }
    exit 1
}

Write-Host ""
Write-Host "Configuration check passed." -ForegroundColor Green
exit 0
```