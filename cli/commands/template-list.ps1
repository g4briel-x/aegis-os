## FILE: `cli/commands/template-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS templates from the templates registry.

.USAGE
.\cli\aegis.ps1 template:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\templates\templates.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Templates registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Templates" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*-\s*id:\s*(.+)$" | ForEach-Object {
    $id = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $id -ForegroundColor Yellow
}

exit 0
```