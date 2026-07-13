## FILE: `scripts/testing/test-cli-config-commands.ps1`

```powershell
<#
.SYNOPSIS
Runs CLI configuration commands.

.DESCRIPTION
Checks that Aegis OS CLI configuration commands are wired correctly.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-config-commands.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — CLI Configuration Command Test" -ForegroundColor Cyan

$commands = @(
    "config:path",
    "config:check",
    "config:show"
)

foreach ($command in $commands) {
    Write-Host "Running: .\cli\aegis.ps1 $command" -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI configuration command failed: $command"
        exit $LASTEXITCODE
    }
}

Write-Host "CLI configuration command test passed." -ForegroundColor Green
exit 0
```