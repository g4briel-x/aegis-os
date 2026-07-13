## FILE: `scripts/testing/test-cli-registry-commands.ps1`

```powershell
<#
.SYNOPSIS
Runs CLI registry listing commands.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-registry-commands.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — CLI Registry Command Test" -ForegroundColor Cyan

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
    Write-Host "Running: .\cli\aegis.ps1 $command" -ForegroundColor Yellow

    & powershell -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI registry command failed: $command"
        exit $LASTEXITCODE
    }
}

Write-Host "CLI registry command test passed." -ForegroundColor Green
exit 0
```
