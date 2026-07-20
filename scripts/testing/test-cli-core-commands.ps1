<#
.SYNOPSIS
Runs basic Aegis OS CLI core commands.

.DESCRIPTION
Checks that essential CLI commands execute successfully.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\testing\test-cli-core-commands.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS - CLI Core Command Test" -ForegroundColor Cyan

$commands = @(
    @("help", ""),
    @("version", ""),
    @("info", ""),
    @("status", ""),
    @("registry:list", "")
)

foreach ($commandSpec in $commands) {
    $command = $commandSpec[0]
    $argument = $commandSpec[1]

    if ([string]::IsNullOrWhiteSpace($argument)) {
        Write-Host "Running: .\cli\aegis.ps1 $command" -ForegroundColor Yellow

        & pwsh -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command
    }
    else {
        Write-Host "Running: .\cli\aegis.ps1 $command $argument" -ForegroundColor Yellow

        & pwsh -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command $argument
    }

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI core command failed: $command"
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "CLI core command test passed." -ForegroundColor Green
exit 0