
<#
.SYNOPSIS
Lists Aegis OS tags from the tags registry.

.USAGE
.\cli\aegis.ps1 tag:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\tags\tags.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Tags registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Tags" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*name:\s*(.+)$" | ForEach-Object {
    $name = $_.Matches[0].Groups[1].Value.Trim()
    if ($name -ne "Tags Registry") {
        Write-Host $name -ForegroundColor Yellow
    }
}

exit 0
