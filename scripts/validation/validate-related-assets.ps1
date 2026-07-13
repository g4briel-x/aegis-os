## FILE: `scripts/validation/validate-related-assets.ps1`

```powershell
<#
.SYNOPSIS
Validates that related asset references point to known ids.

.DESCRIPTION
Scans registry YAML files, collects declared ids, then verifies related_assets ids.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-related-assets.ps1
#>

param(
    [string]$RegistryRoot = "registry"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Related Asset Validation" -ForegroundColor Cyan

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

$yamlFiles = Get-ChildItem -Path $RegistryRoot -Recurse -File -Include *.yaml, *.yml
$declaredIds = New-Object System.Collections.Generic.HashSet[string]
$relatedIds = @()

foreach ($file in $yamlFiles) {
    $lines = Get-Content $file.FullName

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
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

    foreach ($line in $lines) {
        if ($line -match "^\s*related_assets:\s*$") {
            $insideRelatedAssets = $true
            continue
        }

        if ($insideRelatedAssets -and $line -match "^\s{0,4}[a-zA-Z_]+:\s*" -and $line -notmatch "^\s*-\s*id:") {
            $insideRelatedAssets = $false
        }

        if ($insideRelatedAssets -and $line -match "^\s*-\s*id:\s*(.+)\s*$") {
            $relatedId = $Matches[1].Trim().Trim('"').Trim("'")
            $relatedIds += [PSCustomObject]@{
                File = $file.FullName
                Id = $relatedId
            }
        }
    }
}

$failures = @()

foreach ($ref in $relatedIds) {
    if (-not $declaredIds.Contains($ref.Id)) {
        $failures += "$($ref.File) -> unknown related asset: $($ref.Id)"
        Write-Host "BAD $($ref.Id)" -ForegroundColor Red
    }
    else {
        Write-Host "OK  $($ref.Id)" -ForegroundColor Green
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "Unknown related assets found:" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "- $_" -ForegroundColor Red }
    exit 1
}

Write-Host "Related asset validation passed." -ForegroundColor Green
exit 0
```
