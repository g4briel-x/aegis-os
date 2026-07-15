<#
.SYNOPSIS
Displays the Aegis Python runtime status.

.ROLE
Delegates repository discovery and registry inventory to the Python runtime.
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

& python -m aegis_runtime --repo-root $repoRoot status
exit $LASTEXITCODE
