
<#
.SYNOPSIS
Lists Aegis OS docs from the docs registry.

.USAGE
.\cli\aegis.ps1 docs:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\docs\docs.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Docs registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Docs" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*-\s*id:\s*(.+)$" | ForEach-Object {
    $id = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $id -ForegroundColor Yellow
}

exit 0