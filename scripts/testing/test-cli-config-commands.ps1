<#
.SYNOPSIS
Runs Aegis OS CLI configuration command tests.

.DESCRIPTION
Checks that the configuration-related CLI commands execute successfully.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\testing\test-cli-config-commands.ps1
#>

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot '..\..')

Set-Location $repoRoot

Write-Host 'Aegis OS - CLI Configuration Command Test' -ForegroundColor Cyan

$commands = @(
    'config:show',
    'config:path',
    'config:check'
)

foreach ($command in $commands) {
    Write-Host ''
    Write-Host "Running: .\cli\aegis.ps1 $command" -ForegroundColor Yellow

    & pwsh -ExecutionPolicy Bypass -File 'cli\aegis.ps1' $command

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI configuration command failed: $command"
        exit $LASTEXITCODE
    }
}

Write-Host ''
Write-Host 'CLI configuration command test passed.' -ForegroundColor Green

exit 0