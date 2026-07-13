## FILE: `cli/commands/config-path.ps1`

```powershell
<#
.SYNOPSIS
Shows Aegis OS configuration paths.

.USAGE
.\cli\aegis.ps1 config:path
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS Configuration Paths" -ForegroundColor Cyan
Write-Host ""

$paths = @(
    "config\aegis.config.example.yaml",
    "config\aegis.config.local.example.yaml",
    "config\aegis.config.local.yaml"
)

foreach ($path in $paths) {
    if (Test-Path $path) {
        Write-Host "OK  $path" -ForegroundColor Green
    }
    else {
        Write-Host "MISS $path" -ForegroundColor Yellow
    }
}

exit 0
```