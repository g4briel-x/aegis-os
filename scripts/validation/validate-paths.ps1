<#
.SYNOPSIS
Validates that registry entry paths exist in the repository.

.DESCRIPTION
Scans registry YAML files for path fields and verifies that each path exists.

Exposes Test-AegisRegistryPaths so it can be dot-sourced by an orchestrator
(e.g. validate-registry.ps1) and reused against an already-scanned file list.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\validation\validate-paths.ps1
#>

param(
    [string]$RegistryRoot = "registry",
    [string]$RepositoryRoot = "."
)

function Test-AegisRegistryPaths {
    param(
        [Parameter(Mandatory)]
        [System.IO.FileInfo[]]$YamlFiles,

        [string]$RepositoryRoot = "."
    )

    $failures = [System.Collections.Generic.List[string]]::new()

    foreach ($file in $YamlFiles) {
        $lines = Get-Content $file.FullName

        foreach ($line in $lines) {
            if ($line -match "^\s*path:\s*(.+)\s*$") {
                $relativePath = $Matches[1].Trim().Trim('"').Trim("'")

                if ([string]::IsNullOrWhiteSpace($relativePath)) {
                    $failures.Add("$($file.FullName) -> empty path value")
                    Write-Host "BAD empty path in $($file.FullName)" -ForegroundColor Red
                    continue
                }

                $targetPath = Join-Path $RepositoryRoot $relativePath

                if (-not (Test-Path $targetPath)) {
                    $failures.Add("$($file.FullName) -> missing path: $relativePath")
                    Write-Host "BAD $relativePath" -ForegroundColor Red
                }
                else {
                    Write-Host "OK  $relativePath" -ForegroundColor Green
                }
            }
        }
    }

    return $failures
}

if ($MyInvocation.InvocationName -ne '.') {
    $ErrorActionPreference = "Stop"

    Write-Host "Aegis OS - Registry Path Validation" -ForegroundColor Cyan

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

    $failures = Test-AegisRegistryPaths -YamlFiles $yamlFiles -RepositoryRoot $RepositoryRoot

    if ($failures.Count -gt 0) {
        Write-Host ""
        Write-Host "Missing registry paths:" -ForegroundColor Red

        foreach ($failure in $failures) {
            Write-Host "- $failure" -ForegroundColor Red
        }

        exit 1
    }

    Write-Host ""
    Write-Host "Path validation passed." -ForegroundColor Green
    exit 0
}
