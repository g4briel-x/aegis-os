<#
.SYNOPSIS
Checks the Aegis OS configuration files.

.DESCRIPTION
Validates required configuration templates and reports optional local
configuration files without treating their absence as an error.

.USAGE
.\cli\aegis.ps1 config:check
#>

$ErrorActionPreference = 'Stop'

$commandRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $commandRoot '..\..')

Set-Location $repoRoot

Write-Host 'Aegis OS - Configuration Check' -ForegroundColor Cyan
Write-Host ''

$requiredFiles = @(
    'config\aegis.config.example.yaml',
    'config\aegis.config.local.example.yaml'
)

$optionalFiles = @(
    'config\aegis.config.local.yaml'
)

$failures = [System.Collections.Generic.List[object]]::new()

Write-Host 'Required configuration files:' -ForegroundColor Yellow

foreach ($file in $requiredFiles) {
    if (-not (Test-Path -Path $file -PathType Leaf)) {
        Write-Host ('MISS {0}' -f $file) -ForegroundColor Red
        $failures.Add($file)
        continue
    }

    $content = Get-Content -Path $file -Raw

    if ([string]::IsNullOrWhiteSpace($content)) {
        Write-Host ('EMPTY {0}' -f $file) -ForegroundColor Red
        $failures.Add($file)
        continue
    }

    Write-Host ('OK   {0}' -f $file) -ForegroundColor Green
}

Write-Host ''
Write-Host 'Optional local configuration:' -ForegroundColor Yellow

foreach ($file in $optionalFiles) {
    if (Test-Path -Path $file -PathType Leaf) {
        Write-Host ('OK   {0}' -f $file) -ForegroundColor Green
    }
    else {
        Write-Host ('SKIP {0} - optional file not created' -f $file) -ForegroundColor DarkYellow
    }
}

if ($failures.Count -gt 0) {
    Write-Host ''
    Write-Host ('Configuration check failed with {0} error(s).' -f $failures.Count) -ForegroundColor Red
    exit 3
}

Write-Host ''
Write-Host 'Configuration check passed.' -ForegroundColor Green

exit 0