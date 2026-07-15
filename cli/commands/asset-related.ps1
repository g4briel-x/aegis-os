<#
.SYNOPSIS
Shows related assets for an Aegis OS asset.

.DESCRIPTION
Finds an asset by ID inside registry YAML files and displays the values
declared under related_assets.

.USAGE
.\cli\aegis.ps1 asset:related security.security-review-template
#>

param(
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:related <asset-id>" -ForegroundColor Yellow
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

$assetFound = $false
$sourceRegistry = $null
$relatedAssets = [System.Collections.Generic.List[string]]::new()

foreach ($file in $files) {
    $lines = Get-Content -Path $file.FullName

    $insideTarget = $false
    $insideRelatedAssets = $false

    foreach ($line in $lines) {
        if ($line -match '^\s*-\s*id:\s*(.+)\s*$') {
            if ($insideTarget) {
                break
            }

            $id = $Matches[1].Trim()
            $id = $id.Trim('"')
            $id = $id.Trim("'")

            $insideTarget = ($id -eq $Argument)
            $insideRelatedAssets = $false

            if ($insideTarget) {
                $assetFound = $true
                $sourceRegistry = $file.FullName
            }

            continue
        }

        if (-not $insideTarget) {
            continue
        }

        if ($line -match '^\s*related_assets:\s*(.*)\s*$') {
            $insideRelatedAssets = $true
            $inlineValue = $Matches[1].Trim()

            if (-not [string]::IsNullOrWhiteSpace($inlineValue)) {
                $inlineValue = $inlineValue.TrimStart('[').TrimEnd(']')

                foreach ($item in ($inlineValue -split ',')) {
                    $relatedAsset = $item.Trim()
                    $relatedAsset = $relatedAsset.Trim('"')
                    $relatedAsset = $relatedAsset.Trim("'")

                    if (-not [string]::IsNullOrWhiteSpace($relatedAsset)) {
                        $relatedAssets.Add($relatedAsset)
                    }
                }

                $insideRelatedAssets = $false
            }

            continue
        }

        if ($insideRelatedAssets -and $line -match '^\s{6,}-\s*(.+)\s*$') {
            $relatedAsset = $Matches[1].Trim()
            $relatedAsset = $relatedAsset.Trim('"')
            $relatedAsset = $relatedAsset.Trim("'")

            if (-not [string]::IsNullOrWhiteSpace($relatedAsset)) {
                $relatedAssets.Add($relatedAsset)
            }

            continue
        }

        if ($insideRelatedAssets -and $line -match '^\s{4}[A-Za-z0-9_-]+:\s*') {
            $insideRelatedAssets = $false
        }
    }

    if ($assetFound) {
        break
    }
}

if (-not $assetFound) {
    Write-Host "Asset not found: $Argument" -ForegroundColor Red
    exit 5
}

Write-Host ('Related assets for {0}:' -f $Argument) -ForegroundColor Cyan
Write-Host ""

if ($relatedAssets.Count -eq 0) {
    Write-Host "No related assets declared." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Registry:" -ForegroundColor Yellow
    Write-Host $sourceRegistry
    exit 0
}

$uniqueRelatedAssets = @(
    $relatedAssets |
    Sort-Object -Unique
)

foreach ($relatedAsset in $uniqueRelatedAssets) {
    Write-Host $relatedAsset -ForegroundColor Yellow
}

Write-Host ""
Write-Host ('Total related assets: {0}' -f $uniqueRelatedAssets.Count) -ForegroundColor Green
Write-Host ""
Write-Host "Registry:" -ForegroundColor Cyan
Write-Host $sourceRegistry

exit 0