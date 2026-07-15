<#
.SYNOPSIS
Opens an Aegis OS asset path in Windows Explorer.

.DESCRIPTION
Finds an asset by ID inside registry YAML files, resolves its declared path,
then opens the corresponding file or folder.

.USAGE
.\cli\aegis.ps1 asset:open security.review-api-security
#>

param(
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:open <asset-id>" -ForegroundColor Yellow
    exit 2
}

$commandRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $commandRoot "..\..")

Set-Location $repoRoot

$registryRoot = "registry"

if (-not (Test-Path $registryRoot)) {
    Write-Host "Registry folder not found: $registryRoot" -ForegroundColor Red
    exit 3
}

$files = @(
    Get-ChildItem -Path $registryRoot -Recurse -File |
    Where-Object {
        $_.Extension -in @(".yaml", ".yml")
    }
)

$assetPath = $null
$sourceRegistry = $null

foreach ($file in $files) {
    $lines = Get-Content -Path $file.FullName
    $insideTarget = $false

    foreach ($line in $lines) {
        if ($line -match '^\s*-\s*id:\s*(.+)\s*$') {
            $id = $Matches[1].Trim()
            $id = $id.Trim('"')
            $id = $id.Trim("'")

            $insideTarget = ($id -eq $Argument)
            continue
        }

        if ($insideTarget -and $line -match '^\s*path:\s*(.+)\s*$') {
            $assetPath = $Matches[1].Trim()
            $assetPath = $assetPath.Trim('"')
            $assetPath = $assetPath.Trim("'")
            $sourceRegistry = $file.FullName
            break
        }
    }

    if ($assetPath) {
        break
    }
}

if ([string]::IsNullOrWhiteSpace($assetPath)) {
    Write-Host "Asset path not found for: $Argument" -ForegroundColor Red
    exit 5
}

$resolvedAssetPath = Join-Path $repoRoot $assetPath

if (-not (Test-Path $resolvedAssetPath)) {
    Write-Host "Declared asset path does not exist:" -ForegroundColor Red
    Write-Host $assetPath -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Registry:" -ForegroundColor Yellow
    Write-Host $sourceRegistry
    exit 6
}

Write-Host "Opening asset:" -ForegroundColor Cyan
Write-Host $Argument -ForegroundColor Yellow
Write-Host ""
Write-Host "Path:" -ForegroundColor Cyan
Write-Host $resolvedAssetPath

Start-Process explorer.exe $resolvedAssetPath

exit 0