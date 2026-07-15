<#
.SYNOPSIS
Opens an Aegis OS asset in the file explorer.

.DESCRIPTION
Locates the asset path directly from registry YAML files and opens it.
Bug fix: no longer calls asset-path.ps1 as a subprocess (Write-Host output
is not captured by & powershell, so $pathOutput was always empty).

.USAGE
.\cli\aegis.ps1 asset:open <asset-id>
#>

param([string]$Argument = "")

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:open <asset-id>" -ForegroundColor Yellow
    exit 2
}

# Recherche directe dans le registre (évite le sous-processus dont la sortie
# Write-Host n'est pas capturée par & powershell)
$files = Get-ChildItem -Path "registry" -Recurse -File -Include *.yaml, *.yml
$assetPath = $null

foreach ($file in $files) {
    $lines = Get-Content $file.FullName
    $insideTarget = $false

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
            $id = $Matches[1].Trim().Trim('"').Trim("'")
            $insideTarget = ($id -eq $Argument)
            continue
        }

        if ($insideTarget -and $line -match "^\s*path:\s*(.+)\s*$") {
            $assetPath = $Matches[1].Trim().Trim('"').Trim("'")
            break
        }
    }

    if ($assetPath) { break }
}

if (-not $assetPath) {
    Write-Host "Asset not found in registry: $Argument" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $assetPath)) {
    Write-Host "Asset path not found in repository: $assetPath" -ForegroundColor Red
    exit 1
}

Invoke-Item $assetPath
exit 0
