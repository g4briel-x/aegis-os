<#
.SYNOPSIS
Checks required Aegis OS index and manifest files.

.USAGE
pwsh -ExecutionPolicy Bypass -File scripts\doctor\check-required-indexes.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS - Required Indexes Check" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

$requiredFiles = @(
    "README.md",
    "QUICKSTART.md",
    "PROJECT_STATUS.md",
    "CHANGELOG.md",
    "RELEASE_NOTES_v0.5.md",
    "V0_5_CLOSURE_REPORT.md",
    "V0_5_RELEASE_CHECKLIST.md",
    "MANIFEST.md",
    "docs\INDEX.md",
    "skills\INDEX.md",
    "playbooks\INDEX.md",
    "patterns\INDEX.md",
    "templates\INDEX.md",
    "registry\INDEX.md",
    "reports\README.md",
    "scripts\README.md",
    "cli\COMMANDS.md",
    "cli\CLI_USAGE.md",
    "config\README.md"
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
    Write-Host "Missing required files:" -ForegroundColor Red

    foreach ($failure in $failures) {
        Write-Host "- $failure" -ForegroundColor Red
    }

    exit 1
}

Write-Host ""
Write-Host "Required indexes check passed." -ForegroundColor Green
exit 0