<#
.SYNOPSIS
Checks that expected Aegis OS CLI files exist.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\testing\test-cli-files.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS - CLI File Test" -ForegroundColor Cyan

$requiredFiles = @(
    "cli\aegis.ps1",
    "cli\COMMANDS.md",
    "cli\CLI_USAGE.md",
    "cli\CLI_REGISTRY_COMMANDS.md",
    "cli\CLI_ASSET_COMMANDS.md",
    "cli\CLI_CONFIG.md",
    "cli\CLI_TESTING.md",
    "cli\CLI_CONFIG_TESTING.md",
    "cli\CLI_METADATA_TESTING.md",
    "cli\CLI_OUTPUT_MODEL.md",
    "cli\CLI_EXIT_CODES.md",
    "cli\CLI_METADATA_COMMANDS.md",
    "cli\CLI_INSTALLATION.md",

    "cli\commands\help.ps1",
    "cli\commands\validate.ps1",
    "cli\commands\doctor.ps1",
    "cli\commands\report.ps1",
    "cli\commands\registry-list.ps1",
    "cli\commands\asset-find.ps1",

    "cli\commands\skill-list.ps1",
    "cli\commands\playbook-list.ps1",
    "cli\commands\pattern-list.ps1",
    "cli\commands\template-list.ps1",
    "cli\commands\domain-list.ps1",
    "cli\commands\tag-list.ps1",
    "cli\commands\docs-list.ps1",
    "cli\commands\release-status.ps1",

    "cli\commands\asset-show.ps1",
    "cli\commands\asset-related.ps1",
    "cli\commands\asset-path.ps1",
    "cli\commands\asset-open.ps1",
    "cli\commands\domain-assets.ps1",
    "cli\commands\tag-assets.ps1",

    "cli\commands\config-show.ps1",
    "cli\commands\config-path.ps1",
    "cli\commands\config-check.ps1",

    "cli\commands\version.ps1",
    "cli\commands\info.ps1",
    "cli\commands\status.ps1"
)

$failures = [System.Collections.Generic.List[object]]::new()

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "OK  $file" -ForegroundColor Green
    }
    else {
        Write-Host "BAD $file" -ForegroundColor Red
        $failures.Add($file)
    }
}

if ($failures.Count -gt 0) {
    Write-Host ""
    Write-Host "Missing CLI files:" -ForegroundColor Red

    foreach ($failure in $failures) {
        Write-Host "- $failure" -ForegroundColor Red
    }

    exit 1
}

Write-Host ""
Write-Host "CLI file test passed." -ForegroundColor Green
exit 0