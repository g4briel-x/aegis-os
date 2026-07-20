<#
.SYNOPSIS
Runs Aegis OS CLI asset inspection commands.

.DESCRIPTION
Checks that asset-related CLI commands execute successfully.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\testing\test-cli-asset-commands.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS - CLI Asset Command Test" -ForegroundColor Cyan

$commands = @(
    @("asset:find", "security"),
    @("asset:show", "engineering.senior-developer"),
    @("asset:related", "security.security-review-template"),
    @("asset:path", "business.pricing-strategy-template"),
    @("domain:assets", "security"),
    @("tag:assets", "api")
)

foreach ($commandSpec in $commands) {
    $command = $commandSpec[0]
    $argument = $commandSpec[1]

    Write-Host ""
    Write-Host "Running: .\cli\aegis.ps1 $command $argument" -ForegroundColor Yellow

    & pwsh -ExecutionPolicy Bypass -File "cli\aegis.ps1" $command $argument

    if ($LASTEXITCODE -ne 0) {
        Write-Error "CLI asset command failed: $command $argument"
        exit $LASTEXITCODE
    }
}

Write-Host ""
Write-Host "CLI asset command test passed." -ForegroundColor Green
exit 0