## FILE: `scripts/reports/generate-release-report.ps1`

```powershell
<#
.SYNOPSIS
Generates a release report from the releases registry.
#>

param(
    [string]$ReleasesRegistryPath = "registry\releases\releases.registry.yaml",
    [string]$OutputPath = "reports\registry\RELEASE_REPORT.md"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Generating Release Report" -ForegroundColor Cyan

if (-not (Test-Path $ReleasesRegistryPath)) {
    Write-Error "Releases registry not found: $ReleasesRegistryPath"
    exit 1
}

$outputDir = Split-Path -Parent $OutputPath
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

$content = Get-Content $ReleasesRegistryPath
$releases = @()
$current = [ordered]@{
    id = ""
    name = ""
    version = ""
    status = ""
    maturity = ""
}

foreach ($line in $content) {
    if ($line -match "^\s*-\s*id:\s*(release\..+)\s*$") {
        if (-not [string]::IsNullOrWhiteSpace($current.id)) {
            $releases += [PSCustomObject]$current
        }

        $current = [ordered]@{
            id = $Matches[1].Trim()
            name = ""
            version = ""
            status = ""
            maturity = ""
        }
    }
    elseif ($line -match "^\s*name:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($current.id)) {
        $current.name = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*version:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($current.id)) {
        $current.version = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*status:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($current.id)) {
        $current.status = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*maturity:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($current.id)) {
        $current.maturity = $Matches[1].Trim()
    }
}

if (-not [string]::IsNullOrWhiteSpace($current.id)) {
    $releases += [PSCustomObject]$current
}

$lines = @()
$lines += "# Aegis OS — Release Report"
$lines += ""
$lines += "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$lines += ""
$lines += "---"
$lines += ""
$lines += "# 1. Releases"
$lines += ""
$lines += "| ID | Name | Version | Status | Maturity |"
$lines += "|---|---|---|---|---|"

foreach ($release in $releases) {
    $lines += "| `$($release.id)` | $($release.name) | $($release.version) | $($release.status) | $($release.maturity) |"
}

$lines += ""
$lines += "# 2. Final Principle"
$lines += ""
$lines += "> Release reports make Aegis OS progress visible."

$lines | Set-Content -Path $OutputPath -Encoding UTF8

Write-Host "Generated $OutputPath" -ForegroundColor Green
exit 0
```
