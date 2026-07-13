## FILE: `cli/commands/pattern-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS patterns from the patterns registry.

.USAGE
.\cli\aegis.ps1 pattern:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\patterns\patterns.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Patterns registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Patterns" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*-\s*id:\s*(.+)$" | ForEach-Object {
    $id = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $id -ForegroundColor Yellow
}

exit 0
```