<#
.SYNOPSIS
Lists Aegis OS assets belonging to a specific domain.

.USAGE
.\cli\aegis.ps1 domain:assets security
#>

param(
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 domain:assets <domain>" -ForegroundColor Yellow
    exit 2
}

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

$assetIds = [System.Collections.Generic.List[string]]::new()

foreach ($file in $yamlFiles) {
    $lines = Get-Content -Path $file.FullName

    $insideEntry = $false
    $currentId = ""
    $currentDomain = ""

    foreach ($line in $lines) {
        if ($line -match '^\s{2}-\s*id:\s*(.+)\s*$') {
            if (
                $insideEntry -and
                $currentDomain -eq $Argument -and
                -not [string]::IsNullOrWhiteSpace($currentId)
            ) {
                $assetIds.Add($currentId)
            }

            $insideEntry = $true
            $currentId = $Matches[1].Trim().Trim('"').Trim("'")
            $currentDomain = ""
            continue
        }

        if ($insideEntry -and $line -match '^\s{4}domain:\s*(.+)\s*$') {
            $currentDomain = $Matches[1].Trim().Trim('"').Trim("'")
        }
    }

    if (
        $insideEntry -and
        $currentDomain -eq $Argument -and
        -not [string]::IsNullOrWhiteSpace($currentId)
    ) {
        $assetIds.Add($currentId)
    }
}

$uniqueAssetIds = @(
    $assetIds |
    Sort-Object -Unique
)

Write-Host "Assets in domain '$Argument':" -ForegroundColor Cyan
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