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
