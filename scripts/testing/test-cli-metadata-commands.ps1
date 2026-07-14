<#
.SYNOPSIS
Runs Aegis OS CLI metadata command tests.

.DESCRIPTION
Checks that version, information and status commands execute successfully.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-metadata-commands.ps1
#>

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot '..\..')

Set-Location $repoRoot

Write-Host 'Aegis OS - CLI Metadata Command Test' -ForegroundColor Cyan

$commands = @(
    'version',
    'info',
    'status'
)

foreach ($command in $commands) {
    Write-Host ''
    Write-Host ('Running: .\cli\aegis.ps1 {0}' -f $command) -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File 'cli\aegis.ps1' $command

    if ($LASTEXITCODE -ne 0) {
        Write-Error ('CLI metadata command failed: {0}' -f $command)
        exit $LASTEXITCODE
    }
}

Write-Host ''
Write-Host 'CLI metadata command test passed.' -ForegroundColor Green

exit 0