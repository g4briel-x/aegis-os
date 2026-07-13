# Aegis OS — Registry Validation Scripts Bundle

Ce fichier regroupe les scripts PowerShell de validation de la couche Registry :

- `scripts/README.md`
- `scripts/validation/validate-yaml.ps1`
- `scripts/validation/validate-paths.ps1`
- `scripts/validation/validate-ids.ps1`
- `scripts/validation/validate-related-assets.ps1`
- `scripts/validation/validate-registry.ps1`
- `scripts/validation/validate-all.ps1`

---

## FILE: `scripts/README.md`

# Aegis OS — Scripts

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains automation and validation scripts for Aegis OS.

The first script layer focuses on registry validation.

---

# 2. Script Categories

```text
scripts/validation
```

Purpose:

```text
Validates machine-readable registry files, asset paths, ids, duplicate entries and relationships.
```

---

# 3. Recommended Execution

Run from the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
```

---

# 4. Final Principle

> Scripts should make Aegis OS easier to verify before future automation, CLI and runtime layers are added.

---

## FILE: `scripts/validation/validate-yaml.ps1`

```powershell
<#
.SYNOPSIS
Validates that registry YAML files can be parsed.

.DESCRIPTION
This script checks YAML syntax for registry files.
It prefers the PowerShell module powershell-yaml when available.
If the module is missing, it performs a basic file existence and extension check.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-yaml.ps1
#>

param(
    [string]$RegistryRoot = "registry"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — YAML Validation" -ForegroundColor Cyan

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

$yamlFiles = Get-ChildItem -Path $RegistryRoot -Recurse -File -Include *.yaml, *.yml

if ($yamlFiles.Count -eq 0) {
    Write-Error "No YAML registry files found under $RegistryRoot"
    exit 1
}

$hasYamlModule = $false

try {
    Import-Module powershell-yaml -ErrorAction Stop
    $hasYamlModule = $true
}
catch {
    Write-Warning "powershell-yaml module not found. Running basic YAML file checks only."
}

$failures = @()

foreach ($file in $yamlFiles) {
    try {
        $content = Get-Content $file.FullName -Raw

        if ([string]::IsNullOrWhiteSpace($content)) {
            throw "File is empty"
        }

        if ($hasYamlModule) {
            $null = ConvertFrom-Yaml $content
        }

        Write-Host "OK  $($file.FullName)" -ForegroundColor Green
    }
    catch {
        $failures += "$($file.FullName): $($_.Exception.Message)"
        Write-Host "BAD $($file.FullName)" -ForegroundColor Red
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "YAML validation failures:" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "- $_" -ForegroundColor Red }
    exit 1
}

Write-Host "YAML validation passed." -ForegroundColor Green
exit 0
```

---

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

---

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

---

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

---

## FILE: `scripts/validation/validate-registry.ps1`

```powershell
<#
.SYNOPSIS
Runs core registry validations.

.DESCRIPTION
Executes YAML, path, id and related asset validation scripts.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-registry.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Registry Validation" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

$checks = @(
    "validate-yaml.ps1",
    "validate-paths.ps1",
    "validate-ids.ps1",
    "validate-related-assets.ps1"
)

foreach ($check in $checks) {
    $checkPath = Join-Path $scriptRoot $check

    if (-not (Test-Path $checkPath)) {
        Write-Error "Validation script missing: $checkPath"
        exit 1
    }

    Write-Host ""
    Write-Host "Running $check..." -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File $checkPath

    if ($LASTEXITCODE -ne 0) {
        Write-Error "$check failed."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "Registry validation passed." -ForegroundColor Green
exit 0
```

---

## FILE: `scripts/validation/validate-all.ps1`

```powershell
<#
.SYNOPSIS
Runs all available Aegis OS validation checks.

.DESCRIPTION
This is the main validation entrypoint for the repository.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Full Validation" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

$registryValidation = Join-Path $scriptRoot "validate-registry.ps1"

if (-not (Test-Path $registryValidation)) {
    Write-Error "Registry validation entrypoint missing: $registryValidation"
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $registryValidation

if ($LASTEXITCODE -ne 0) {
    Write-Error "Full validation failed."
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "All validation checks passed." -ForegroundColor Green
exit 0
```
