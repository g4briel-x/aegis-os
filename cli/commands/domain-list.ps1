
<#
.SYNOPSIS
Lists Aegis OS domains from the domains registry.

.USAGE
.\cli\aegis.ps1 domain:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\domains\domains.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Domains registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Domains" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*slug:\s*(.+)$" | ForEach-Object {
    $slug = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $slug -ForegroundColor Yellow
}

exit 0
