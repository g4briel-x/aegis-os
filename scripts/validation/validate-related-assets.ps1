<#
.SYNOPSIS
Validates that related asset references point to known ids.

.DESCRIPTION
Scans registry YAML files, collects declared primary ids, then checks related_assets ids.
Unknown related assets are reported as warnings during v0.5 because some conceptual assets
such as core.identity or framework.skills may not yet have dedicated registry entries.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-related-assets.ps1
#>

param(
    [string]$RegistryRoot = "registry"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS - Related Asset Validation" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

$yamlFiles = @(
    Get-ChildItem -Path $RegistryRoot -Recurse -File |
    Where-Object {
        $_.Extension -eq ".yaml" -or $_.Extension -eq ".yml"
    }
)

if ($yamlFiles.Count -eq 0) {
    Write-Error "No YAML registry files found under $RegistryRoot"
    exit 1
}

$declaredIds = New-Object System.Collections.Generic.HashSet[string]
$relatedRefs = @()

foreach ($file in $yamlFiles) {
    $lines = Get-Content $file.FullName
    $insideEntries = $false
    $insideRelatedAssets = $false
    $lineNumber = 0

    foreach ($line in $lines) {
        $lineNumber++

        if ($line -match "^\s*entries:\s*$") {
            $insideEntries = $true
            $insideRelatedAssets = $false
            continue
        }

        if ($line -match "^\s*related_assets:\s*$") {
            $insideRelatedAssets = $true
            continue
        }

        if ($insideRelatedAssets -and $line -match "^\s{2}-\s*id:\s*(.+)\s*$") {
            $insideRelatedAssets = $false
        }

        $isRegistryId = $line -match "^\s{2}id:\s*(.+)\s*$" -and -not $insideEntries
        $isEntryId = $line -match "^\s{2}-\s*id:\s*(.+)\s*$" -and $insideEntries -and -not $insideRelatedAssets

        if ($isRegistryId -or $isEntryId) {
            $id = $Matches[1].Trim().Trim('"').Trim("'")

            if (-not [string]::IsNullOrWhiteSpace($id)) {
                [void]$declaredIds.Add($id)
            }
        }
    }
}

foreach ($file in $yamlFiles) {
    $lines = Get-Content $file.FullName
    $insideRelatedAssets = $false
    $lineNumber = 0

    foreach ($line in $lines) {
        $lineNumber++

        if ($line -match "^\s*related_assets:\s*$") {
            $insideRelatedAssets = $true
            continue
        }

        if ($insideRelatedAssets -and $line -match "^\s{2}-\s*id:\s*(.+)\s*$") {
            $insideRelatedAssets = $false
        }

        if ($insideRelatedAssets -and $line -match "^\s{6,}-\s*id:\s*(.+)\s*$") {
            $relatedId = $Matches[1].Trim().Trim('"').Trim("'")

            if (-not [string]::IsNullOrWhiteSpace($relatedId)) {
                $relatedRefs += [PSCustomObject]@{
                    File = $file.FullName
                    Line = $lineNumber
                    Id   = $relatedId
                }
            }
        }
    }
}

$warnings = @()

foreach ($ref in $relatedRefs) {
    if ($declaredIds.Contains($ref.Id)) {
        Write-Host "OK   $($ref.Id)" -ForegroundColor Green
    }
    else {
        $warnings += "$($ref.File):$($ref.Line) -> unknown related asset: $($ref.Id)"
        Write-Host "WARN $($ref.Id)" -ForegroundColor Yellow
    }
}

if ($warnings.Count -gt 0) {
    Write-Host ""
    Write-Host "Unknown related assets found as warnings:" -ForegroundColor Yellow

    foreach ($warning in $warnings) {
        Write-Host "- $warning" -ForegroundColor Yellow
    }

    Write-Host ""
    Write-Host "Related asset validation passed with warnings." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Related asset validation passed." -ForegroundColor Green
exit 0