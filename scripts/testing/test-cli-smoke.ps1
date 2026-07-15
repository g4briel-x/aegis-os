<#
.SYNOPSIS
Runs all Aegis OS CLI smoke tests.

.DESCRIPTION
This script validates that the CLI command layer is wired correctly.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
#>

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
Write-Host "Aegis OS - CLI Smoke Tests" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

$tests = @(
    "test-cli-files.ps1",
    "test-cli-core-commands.ps1",
    "test-cli-registry-commands.ps1",
    "test-cli-asset-commands.ps1",
    "test-cli-config-commands.ps1",
    "test-cli-metadata-commands.ps1"
)

foreach ($test in $tests) {
    $testPath = Join-Path $scriptRoot $test

    if (-not (Test-Path $testPath)) {
        Write-Error "Test script missing: $testPath"
        exit 1
    }

    Write-Host ""
    Write-Host "Running $test..." -ForegroundColor Yellow

    & $PSExe -ExecutionPolicy Bypass -File $testPath

    if ($LASTEXITCODE -ne 0) {
        Write-Error "$test failed."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "CLI smoke tests passed." -ForegroundColor Green
exit 0