## FILE: `scripts/validation/validate-ids.ps1`

```powershell
<#
.SYNOPSIS
Validates duplicate ids across registry files.

.DESCRIPTION
Scans registry YAML files for id fields and reports duplicates.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-ids.ps1
#>

param(
    [string]$RegistryRoot = "registry"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Registry ID Validation" -ForegroundColor Cyan

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

$yamlFiles = Get-ChildItem -Path $RegistryRoot -Recurse -File -Include *.yaml, *.yml
$idMap = @{}
$duplicates = @()

foreach ($file in $yamlFiles) {
    $lines = Get-Content $file.FullName

    foreach ($line in $lines) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$" -or $line -match "^\s*id:\s*(.+)\s*$") {
            $id = $Matches[1].Trim().Trim('"').Trim("'")

            if ([string]::IsNullOrWhiteSpace($id)) {
                continue
            }

            if ($idMap.ContainsKey($id)) {
                $duplicates += "$id appears in $($idMap[$id]) and $($file.FullName)"
                Write-Host "DUP $id" -ForegroundColor Red
            }
            else {
                $idMap[$id] = $file.FullName
                Write-Host "OK  $id" -ForegroundColor Green
            }
        }
    }
}

if ($duplicates.Count -gt 0) {
    Write-Host ""
    Write-Host "Duplicate ids found:" -ForegroundColor Red
    $duplicates | ForEach-Object { Write-Host "- $_" -ForegroundColor Red }
    exit 1
}

Write-Host "ID validation passed." -ForegroundColor Green
exit 0
```
