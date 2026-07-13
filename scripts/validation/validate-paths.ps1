## FILE: `scripts/validation/validate-paths.ps1`

```powershell
<#
.SYNOPSIS
Validates that registry entry paths exist in the repository.

.DESCRIPTION
Scans registry YAML files for path fields and verifies that each path exists.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-paths.ps1
#>

param(
    [string]$RegistryRoot = "registry",
    [string]$RepositoryRoot = "."
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Registry Path Validation" -ForegroundColor Cyan

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

$yamlFiles = Get-ChildItem -Path $RegistryRoot -Recurse -File -Include *.yaml, *.yml
$failures = @()

foreach ($file in $yamlFiles) {
    $lines = Get-Content $file.FullName

    foreach ($line in $lines) {
        if ($line -match "^\s*path:\s*(.+)\s*$") {
            $relativePath = $Matches[1].Trim().Trim('"').Trim("'")
            $targetPath = Join-Path $RepositoryRoot $relativePath

            if (-not (Test-Path $targetPath)) {
                $failures += "$($file.FullName) -> missing path: $relativePath"
                Write-Host "BAD $relativePath" -ForegroundColor Red
            }
            else {
                Write-Host "OK  $relativePath" -ForegroundColor Green
            }
        }
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "Missing registry paths:" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "- $_" -ForegroundColor Red }
    exit 1
}

Write-Host "Path validation passed." -ForegroundColor Green
exit 0
```
