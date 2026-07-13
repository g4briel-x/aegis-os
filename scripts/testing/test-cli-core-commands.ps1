## FILE: `scripts/testing/test-cli-core-commands.ps1`

```powershell
<#
.SYNOPSIS
Runs basic CLI core commands.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-core-commands.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — CLI Core Command Test" -ForegroundColor Cyan

$commands = @(
    @("help", ""),
    @("registry:list", "")
)

foreach ($commandSpec in $commands) {
    $command = $commandSpec[0]
    $argument = $commandSpec[1]

    Write-Host "Running: .\cli\aegis.ps1 $command $argument" -ForegroundColor Yellow

    if ([string]::IsNullOrWhiteSpace($argument)) {
        & powershell -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command
    }
    else {
        & powershell -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command $argument
    }

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI command failed: $command"
        exit $LASTEXITCODE
    }
}

Write-Host "CLI core command test passed." -ForegroundColor Green
exit 0
```