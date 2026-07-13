## FILE: `scripts/testing/test-cli-metadata-commands.ps1`

```powershell
<#
.SYNOPSIS
Runs CLI metadata commands.

.DESCRIPTION
Checks that Aegis OS CLI metadata commands are wired correctly.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-metadata-commands.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — CLI Metadata Command Test" -ForegroundColor Cyan

$commands = @(
    "version",
    "info",
    "status"
)

foreach ($command in $commands) {
    Write-Host "Running: .\cli\aegis.ps1 $command" -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI metadata command failed: $command"
        exit $LASTEXITCODE
    }
}

Write-Host "CLI metadata command test passed." -ForegroundColor Green
exit 0
```