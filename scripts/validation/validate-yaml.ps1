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

Write-Host "Aegis OS - YAML Validation" -ForegroundColor Cyan

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

$hasYamlModule = $false

try {
    Import-Module powershell-yaml -ErrorAction Stop
    $hasYamlModule = $true
    Write-Host "OK  powershell-yaml module loaded" -ForegroundColor Green
}
catch {
    Write-Host "WARN powershell-yaml module not found. Running basic YAML file checks only." -ForegroundColor Yellow
}

$failures = @()

foreach ($file in $yamlFiles) {
    try {
        $content = Get-Content $file.FullName -Raw

        if ([string]::IsNullOrWhiteSpace($content)) {
            throw "File is empty"
        }

        if ($hasYamlModule) {
            $null = ConvertFrom-Yaml -Yaml $content
        }

        Write-Host "OK  $($file.FullName)" -ForegroundColor Green
    }
    catch {
        $message = $_.Exception.Message
        $failures += "$($file.FullName): $message"

        Write-Host "BAD $($file.FullName)" -ForegroundColor Red
        Write-Host "    $message" -ForegroundColor Red
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "YAML validation failures:" -ForegroundColor Red

    foreach ($failure in $failures) {
        Write-Host "- $failure" -ForegroundColor Red
    }

    exit 1
}

Write-Host ""
Write-Host "YAML validation passed." -ForegroundColor Green
exit 0