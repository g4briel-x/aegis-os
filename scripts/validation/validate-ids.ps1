<#
.SYNOPSIS
Validates registry entry ids.

.DESCRIPTION
Scans registry YAML files and checks that primary registry ids and entry ids are present and unique.
Related asset ids are references and are not counted as primary ids.

Exposes Test-AegisRegistryIds so it can be dot-sourced by an orchestrator
(e.g. validate-registry.ps1) and reused against an already-scanned file list.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\validation\validate-ids.ps1
#>

param(
    [string]$RegistryRoot = "registry"
)

function Test-AegisRegistryIds {
    param(
        [Parameter(Mandatory)]
        [System.IO.FileInfo[]]$YamlFiles
    )

    $ids = @{}
    $failures = [System.Collections.Generic.List[string]]::new()

    foreach ($file in $YamlFiles) {
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

            if ($insideRelatedAssets -and $line -match "^\s{2,}\w") {
                $insideRelatedAssets = $false
            }

            $isRegistryId = $line -match "^\s{2}id:\s*(.+)\s*$" -and -not $insideEntries
            $isEntryId = $line -match "^\s{2}-\s*id:\s*(.+)\s*$" -and $insideEntries -and -not $insideRelatedAssets

            if ($isRegistryId -or $isEntryId) {
                $id = $Matches[1].Trim().Trim('"').Trim("'")

                if ([string]::IsNullOrWhiteSpace($id)) {
                    $failures.Add("$($file.FullName):$lineNumber -> empty id")
                    Write-Host "BAD empty id at $($file.FullName):$lineNumber" -ForegroundColor Red
                    continue
                }

                if ($ids.ContainsKey($id)) {
                    $failures.Add("$($file.FullName):$lineNumber -> duplicate id '$id' also found at $($ids[$id])")
                    Write-Host "BAD duplicate id: $id" -ForegroundColor Red
                }
                else {
                    $ids[$id] = "$($file.FullName):$lineNumber"
                    Write-Host "OK  $id" -ForegroundColor Green
                }
            }
        }
    }

    return $failures
}

if ($MyInvocation.InvocationName -ne '.') {
    $ErrorActionPreference = "Stop"

    Write-Host "Aegis OS - ID Validation" -ForegroundColor Cyan

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

    $failures = Test-AegisRegistryIds -YamlFiles $yamlFiles

    if ($failures.Count -gt 0) {
        Write-Host ""
        Write-Host "ID validation failures:" -ForegroundColor Red

        foreach ($failure in $failures) {
            Write-Host "- $failure" -ForegroundColor Red
        }

        exit 1
    }

    Write-Host ""
    Write-Host "ID validation passed." -ForegroundColor Green
    exit 0
}
