
<#
.SYNOPSIS
Shows the Aegis OS example configuration.

.USAGE
.\cli\aegis.ps1 config:show
#>

$ErrorActionPreference = "Stop"

$configPath = "config\aegis.config.example.yaml"

if (-not (Test-Path $configPath)) {
    Write-Host "Configuration file not found: $configPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Configuration" -ForegroundColor Cyan
Write-Host "Source: $configPath" -ForegroundColor Yellow
Write-Host ""

Get-Content $configPath | ForEach-Object {
    Write-Host $_
}

exit 0