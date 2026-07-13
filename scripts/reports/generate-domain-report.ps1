## FILE: `scripts/reports/generate-domain-report.ps1`

```powershell
<#
.SYNOPSIS
Generates a domain report from the domains registry.
#>

param(
    [string]$DomainsRegistryPath = "registry\domains\domains.registry.yaml",
    [string]$OutputPath = "reports\registry\DOMAIN_REPORT.md"
)

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Generating Domain Report" -ForegroundColor Cyan

if (-not (Test-Path $DomainsRegistryPath)) {
    Write-Error "Domains registry not found: $DomainsRegistryPath"
    exit 1
}

$outputDir = Split-Path -Parent $OutputPath
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

$content = Get-Content $DomainsRegistryPath
$domainNames = @()

foreach ($line in $content) {
    if ($line -match "^\s*name:\s*(.+)\s*$") {
        $name = $Matches[1].Trim().Trim('"').Trim("'")
        if ($name -ne "Domains Registry") {
            $domainNames += $name
        }
    }
}

$lines = @()
$lines += "# Aegis OS — Domain Report"
$lines += ""
$lines += "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$lines += ""
$lines += "---"
$lines += ""
$lines += "# 1. Domains"
$lines += ""

foreach ($domain in $domainNames | Sort-Object) {
    $lines += "- $domain"
}

$lines += ""
$lines += "# 2. Count"
$lines += ""
$lines += "```text"
$lines += "Total domains: $($domainNames.Count)"
$lines += "```"
$lines += ""
$lines += "# 3. Final Principle"
$lines += ""
$lines += "> Domain reports show how Aegis OS is organized by responsibility."

$lines | Set-Content -Path $OutputPath -Encoding UTF8

Write-Host "Generated $OutputPath" -ForegroundColor Green
exit 0
```
