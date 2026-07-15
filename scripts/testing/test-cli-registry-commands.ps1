<#
.SYNOPSIS
Runs Aegis OS CLI registry listing commands.

.DESCRIPTION
Checks that registry-related CLI commands execute successfully.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-registry-commands.ps1
#>

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
Write-Host "Aegis OS - CLI Registry Command Test" -ForegroundColor Cyan

$commands = @(
    "skill:list",
    "playbook:list",
    "pattern:list",
    "template:list",
    "domain:list",
    "tag:list",
    "docs:list",
    "release:status"
)

foreach ($command in $commands) {
    Write-Host ""
    Write-Host "Running: .\cli\aegis.ps1 $command" -ForegroundColor Yellow

    & $PSExe -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI registry command failed: $command"
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "CLI registry command test passed." -ForegroundColor Green
exit 0