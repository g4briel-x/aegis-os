<#
.SYNOPSIS
Lists Aegis OS assets associated with a specific tag.

.USAGE
.\cli\aegis.ps1 tag:assets api
#>

param(
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 tag:assets <tag>" -ForegroundColor Yellow
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

$yamlFiles = @(
    Get-ChildItem -Path $registryRoot -Recurse -File |
    Where-Object {
        $_.Extension -in @(".yaml", ".yml")
    }
)

if ($yamlFiles.Count -eq 0) {
    Write-Host "No registry YAML files found." -ForegroundColor Yellow
    exit 0
}

$assetIds = @()

foreach ($file in $yamlFiles) {
    $lines = Get-Content -Path $file.FullName

    $currentId = ""
    $hasRequestedTag = $false
    $insideTags = $false

    foreach ($line in $lines) {
        if ($line -match '^\s{2}-\s*id:\s*(.+)\s*$') {
            if (
                -not [string]::IsNullOrWhiteSpace($currentId) -and
                $hasRequestedTag
            ) {
                $assetIds += $currentId
            }

            $currentId = $Matches[1].Trim()
            $currentId = $currentId.Trim('"')
            $currentId = $currentId.Trim("'")

            $hasRequestedTag = $false
            $insideTags = $false
            continue
        }

        if ([string]::IsNullOrWhiteSpace($currentId)) {
            continue
        }

        if ($line -match '^\s{4}tags:\s*(.*)\s*$') {
            $insideTags = $true
            $inlineTags = $Matches[1].Trim()

            if (-not [string]::IsNullOrWhiteSpace($inlineTags)) {
                $inlineTags = $inlineTags.TrimStart('[').TrimEnd(']')

                foreach ($tagItem in ($inlineTags -split ',')) {
                    $tag = $tagItem.Trim()
                    $tag = $tag.Trim('"')
                    $tag = $tag.Trim("'")

                    if ($tag -eq $Argument) {
                        $hasRequestedTag = $true
                    }
                }

                $insideTags = $false
            }

            continue
        }

        if ($insideTags -and $line -match '^\s{6,}-\s*(.+)\s*$') {
            $tag = $Matches[1].Trim()
            $tag = $tag.Trim('"')
            $tag = $tag.Trim("'")

            if ($tag -eq $Argument) {
                $hasRequestedTag = $true
            }

            continue
        }

        if ($insideTags -and $line -match '^\s{4}[A-Za-z0-9_-]+:\s*') {
            $insideTags = $false
        }
    }

    if (
        -not [string]::IsNullOrWhiteSpace($currentId) -and
        $hasRequestedTag
    ) {
        $assetIds += $currentId
    }
}

$uniqueAssetIds = @(
    $assetIds |
    Sort-Object -Unique
)

Write-Host "Assets with tag '$Argument':" -ForegroundColor Cyan
Write-Host ""

if ($uniqueAssetIds.Count -eq 0) {
    Write-Host "No assets found." -ForegroundColor Yellow
    exit 0
}

foreach ($assetId in $uniqueAssetIds) {
    Write-Host $assetId -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Total assets: $($uniqueAssetIds.Count)" -ForegroundColor Green

exit 0