<#
.SYNOPSIS
Validates Aegis registries through the Python runtime.

.ROLE
Delegates advanced registry validation to the Python runtime.
#>

$ErrorActionPreference = 'Stop'

$commandRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $commandRoot '..\..')

Set-Location $repoRoot

$pythonCommand = Get-Command python -ErrorAction SilentlyContinue

if (-not $pythonCommand) {
    Write-Host 'Python was not found in PATH.' -ForegroundColor Red
    exit 3
}

& python -m aegis_runtime --repo-root $repoRoot validate
exit $LASTEXITCODE
