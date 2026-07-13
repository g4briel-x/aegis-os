## FILE: `scripts/reports/generate-asset-map.ps1`

```powershell
<#
.SYNOPSIS
Generates a simple asset map from registry files.
#>

param(
    [string]$RegistryRoot = "registry",
    [string]$OutputPath = "reports\registry\ASSET_MAP.md"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Generating Asset Map" -ForegroundColor Cyan

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

$outputDir = Split-Path -Parent $OutputPath
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

$yamlFiles = Get-ChildItem -Path $RegistryRoot -Recurse -File -Include *.yaml, *.yml
$entries = @()

foreach ($file in $yamlFiles) {
    $current = [ordered]@{
        id = ""
        type = ""
        domain = ""
        path = ""
        source = (Resolve-Path $file.FullName -Relative)
    }

    $linesInFile = Get-Content $file.FullName

    foreach ($line in $linesInFile) {
        if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
            if (-not [string]::IsNullOrWhiteSpace($current.id)) {
                $entries += [PSCustomObject]$current
            }

            $current = [ordered]@{
                id = $Matches[1].Trim().Trim('"').Trim("'")
                type = ""
                domain = ""
                path = ""
                source = (Resolve-Path $file.FullName -Relative)
            }
        }
        elseif ($line -match "^\s*type:\s*(.+)\s*$") {
            $current.type = $Matches[1].Trim().Trim('"').Trim("'")
        }
        elseif ($line -match "^\s*domain:\s*(.+)\s*$") {
            $current.domain = $Matches[1].Trim().Trim('"').Trim("'")
        }
        elseif ($line -match "^\s*path:\s*(.+)\s*$") {
            $current.path = $Matches[1].Trim().Trim('"').Trim("'")
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($current.id)) {
        $entries += [PSCustomObject]$current
    }
}

$lines = @()
$lines += "# Aegis OS — Asset Map"
$lines += ""
$lines += "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$lines += ""
$lines += "---"
$lines += ""
$lines += "# 1. Assets"
$lines += ""
$lines += "| ID | Type | Domain | Path | Source Registry |"
$lines += "|---|---|---|---|---|"

foreach ($entry in $entries | Sort-Object id) {
    $lines += "| `$($entry.id)` | $($entry.type) | $($entry.domain) | `$($entry.path)` | `$($entry.source)` |"
}

$lines += ""
$lines += "# 2. Final Principle"
$lines += ""
$lines += "> Asset maps help humans audit what the registries expose to tools."

$lines | Set-Content -Path $OutputPath -Encoding UTF8

Write-Host "Generated $OutputPath" -ForegroundColor Green
exit 0
```
