<#
.SYNOPSIS
Runs Aegis OS CLI runtime command tests.

.DESCRIPTION
Checks that PowerShell CLI commands correctly delegate to the Python runtime.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-runtime-commands.ps1
#>

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot '..\..')

Set-Location $repoRoot

Write-Host 'Aegis OS - CLI Runtime Command Test' -ForegroundColor Cyan

$commands = @(
    @('runtime:status', ''),
    @('runtime:registry-list', ''),
    @('runtime:asset-find', 'security'),
    @('runtime:asset-show', 'security.review-api-security'),
    @('runtime:execution-plan', 'security.review-api-security'),
    @('runtime:execution-dry-run', 'security.review-api-security'),
    @('runtime:execution-contract', 'security.review-api-security'),
    @('runtime:validate', '')
)

foreach ($commandSpec in $commands) {
    $command = $commandSpec[0]
    $argument = $commandSpec[1]

    Write-Host ''

    if ([string]::IsNullOrWhiteSpace($argument)) {
        Write-Host ('Running: .\cli\aegis.ps1 {0}' -f $command) -ForegroundColor Yellow
        & powershell -ExecutionPolicy Bypass -File 'cli\aegis.ps1' $command
    }
    else {
        Write-Host ('Running: .\cli\aegis.ps1 {0} {1}' -f $command, $argument) -ForegroundColor Yellow
        & powershell -ExecutionPolicy Bypass -File 'cli\aegis.ps1' $command $argument
    }

    if ($LASTEXITCODE -ne 0) {
        Write-Error ('CLI runtime command failed: {0} {1}' -f $command, $argument)
        exit $LASTEXITCODE
    }
}

Write-Host ''
Write-Host 'CLI runtime command test passed.' -ForegroundColor Green

exit 0
