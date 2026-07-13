## FILE: `scripts/reports/generate-registry-summary.ps1`

```powershell
<#
.SYNOPSIS
Generates a registry summary report.
#>

param(
    [string]$RegistryRoot = "registry",
    [string]$OutputPath = "reports\registry\REGISTRY_SUMMARY.md"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Generating Registry Summary" -ForegroundColor Cyan

if (-not (Test-Path $RegistryRoot)) {
    Write-Error "Registry root not found: $RegistryRoot"
    exit 1
}

$outputDir = Split-Path -Parent $OutputPath
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

$yamlFiles = Get-ChildItem -Path $RegistryRoot -Recurse -File -Include *.yaml, *.yml

$lines = @()
$lines += "# Aegis OS — Registry Summary"
$lines += ""
$lines += "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$lines += ""
$lines += "---"
$lines += ""
$lines += "# 1. Summary"
$lines += ""
$lines += "```text"
$lines += "Registry root: $RegistryRoot"
$lines += "Registry files: $($yamlFiles.Count)"
$lines += "```"
$lines += ""
$lines += "# 2. Registry Files"
$lines += ""

foreach ($file in $yamlFiles | Sort-Object FullName) {
    $relative = Resolve-Path $file.FullName -Relative
    $lines += "- `$relative`"
}

$lines += ""
$lines += "# 3. Final Principle"
$lines += ""
$lines += "> Registry summary reports help maintainers see which machine-readable catalogs exist."

$lines | Set-Content -Path $OutputPath -Encoding UTF8

Write-Host "Generated $OutputPath" -ForegroundColor Green
exit 0
```
