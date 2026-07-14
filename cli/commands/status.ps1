<#
.SYNOPSIS
Runs a lightweight Aegis OS repository status check.

.USAGE
.\cli\aegis.ps1 status
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Status" -ForegroundColor Cyan
Write-Host ""

$checks = @(
    @{ Name = "CLI entrypoint"; Path = "cli\aegis.ps1" },
    @{ Name = "Config example"; Path = "config\aegis.config.example.yaml" },
    @{ Name = "Skills registry"; Path = "registry\skills\skills.registry.yaml" },
    @{ Name = "Playbooks registry"; Path = "registry\playbooks\playbooks.registry.yaml" },
    @{ Name = "Patterns registry"; Path = "registry\patterns\patterns.registry.yaml" },
    @{ Name = "Templates registry"; Path = "registry\templates\templates.registry.yaml" },
    @{ Name = "Validation script"; Path = "scripts\validation\validate-all.ps1" },
    @{ Name = "Doctor script"; Path = "scripts\doctor\aegis-doctor.ps1" },
    @{ Name = "Smoke test script"; Path = "scripts\testing\test-cli-smoke.ps1" }
)

$failures = @()

foreach ($check in $checks) {
    if (Test-Path $check.Path) {
        Write-Host "OK   $($check.Name): $($check.Path)" -ForegroundColor Green
    }
    else {
        Write-Host "MISS $($check.Name): $($check.Path)" -ForegroundColor Yellow
        $failures += $check
    }
}

Write-Host ""

try {
    $branch = git branch --show-current
    Write-Host "Git branch: $branch" -ForegroundColor Cyan

    $status = git status --short

    if ([string]::IsNullOrWhiteSpace($status)) {
        Write-Host "Git working tree: clean" -ForegroundColor Green
    }
    else {
        Write-Host "Git working tree: has changes" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "Git status: unavailable" -ForegroundColor Yellow
}

Write-Host ""

if ($failures.Count -gt 0) {
    Write-Host "Status completed with missing files." -ForegroundColor Yellow
    exit 3
}

Write-Host "Status check passed." -ForegroundColor Green
exit 0