<#
.SYNOPSIS
Validates that registry YAML files can be parsed.

.DESCRIPTION
This script checks YAML syntax for registry files.
It prefers the PowerShell module powershell-yaml when available.
If the module is missing, it performs a basic file existence and extension check.

Exposes Test-AegisYamlFiles so it can be dot-sourced by an orchestrator
(e.g. validate-registry.ps1) and reused against an already-scanned file list,
instead of every check re-scanning the registry folder on its own.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\validation\validate-yaml.ps1
#>

param(
    [string]$RegistryRoot = "registry"
)

function Test-AegisYamlFiles {
    param(
        [Parameter(Mandatory)]
        [System.IO.FileInfo[]]$YamlFiles
    )

    $hasYamlModule = $false

    try {
        Import-Module powershell-yaml -ErrorAction Stop
        $hasYamlModule = $true
        Write-Host "OK  powershell-yaml module loaded" -ForegroundColor Green
    }
    catch {
        Write-Host "WARN powershell-yaml module not found. Running basic YAML file checks only." -ForegroundColor Yellow
    }

    $failures = [System.Collections.Generic.List[string]]::new()

    foreach ($file in $YamlFiles) {
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
            $failures.Add("$($file.FullName): $message")

            Write-Host "BAD $($file.FullName)" -ForegroundColor Red
            Write-Host "    $message" -ForegroundColor Red
        }
    }

    return $failures
}

# Only run as a standalone check when invoked directly (not dot-sourced by
# an orchestrator that wants to call Test-AegisYamlFiles itself).
if ($MyInvocation.InvocationName -ne '.') {
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

    $failures = Test-AegisYamlFiles -YamlFiles $yamlFiles

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
}
