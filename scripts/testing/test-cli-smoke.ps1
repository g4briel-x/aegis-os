<#
.SYNOPSIS
Runs all Aegis OS CLI smoke tests.

.DESCRIPTION
This script validates that the CLI command layer is wired correctly.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
#>

$ErrorActionPreference = "Stop"

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

    & pwsh -ExecutionPolicy Bypass -File $testPath

    if ($LASTEXITCODE -ne 0) {
        Write-Error "$test failed."
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "CLI smoke tests passed." -ForegroundColor Green
exit 0