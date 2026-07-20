<#
.SYNOPSIS
Runs core registry validations.

.DESCRIPTION
Executes YAML, path, id and related asset validation checks.

Performance note: previously this orchestrator spawned a brand new pwsh
process for each of the 4 checks below, and each check independently
re-scanned the entire registry folder with Get-ChildItem -Recurse.
That meant 4 process spawns + 4 full directory scans for a single
`validate-registry` run. This version scans the registry once, dot-sources
the check scripts (which only defines their functions - see the
Test-AegisXxx guard in each file), and calls each function in-process with
the shared file list.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\validation\validate-registry.ps1
#>

param(
    [string]$RegistryRoot = "registry"
)

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
Write-Host "Aegis OS - Registry Validation" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

# Single shared scan, reused by every check below instead of each check
# scanning the registry folder on its own.
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

$checkScripts = @(
    "validate-yaml.ps1",
    "validate-paths.ps1",
    "validate-ids.ps1",
    "validate-related-assets.ps1"
)

foreach ($check in $checkScripts) {
    $checkPath = Join-Path $scriptRoot $check

    if (-not (Test-Path $checkPath)) {
        Write-Error "Validation script missing: $checkPath"
        exit 1
    }
}

# Dot-sourcing here only *defines* Test-AegisYamlFiles / Test-AegisRegistryPaths /
# Test-AegisRegistryIds / Test-AegisRelatedAssets in this scope - each script's
# own standalone-run logic is skipped because of its dot-source guard.
. (Join-Path $scriptRoot "validate-yaml.ps1")
. (Join-Path $scriptRoot "validate-paths.ps1")
. (Join-Path $scriptRoot "validate-ids.ps1")
. (Join-Path $scriptRoot "validate-related-assets.ps1")

$overallFailures = [System.Collections.Generic.List[string]]::new()

Write-Host ""
Write-Host "Running YAML validation..." -ForegroundColor Yellow
$yamlFailures = Test-AegisYamlFiles -YamlFiles $yamlFiles
foreach ($failure in $yamlFailures) { $overallFailures.Add("[yaml] $failure") }

Write-Host ""
Write-Host "Running path validation..." -ForegroundColor Yellow
$pathFailures = Test-AegisRegistryPaths -YamlFiles $yamlFiles -RepositoryRoot "."
foreach ($failure in $pathFailures) { $overallFailures.Add("[paths] $failure") }

Write-Host ""
Write-Host "Running id validation..." -ForegroundColor Yellow
$idFailures = Test-AegisRegistryIds -YamlFiles $yamlFiles
foreach ($failure in $idFailures) { $overallFailures.Add("[ids] $failure") }

Write-Host ""
Write-Host "Running related asset validation..." -ForegroundColor Yellow
$relatedWarnings = Test-AegisRelatedAssets -YamlFiles $yamlFiles

if ($overallFailures.Count -gt 0) {
    Write-Host ""
    Write-Host "Registry validation failures:" -ForegroundColor Red

    foreach ($failure in $overallFailures) {
        Write-Host "- $failure" -ForegroundColor Red
    }

    exit 1
}

if ($relatedWarnings.Count -gt 0) {
    Write-Host ""
    Write-Host "Registry validation passed with warnings (unknown related assets):" -ForegroundColor Yellow

    foreach ($warning in $relatedWarnings) {
        Write-Host "- $warning" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Registry validation passed." -ForegroundColor Green
exit 0
