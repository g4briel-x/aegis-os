<#
.SYNOPSIS
Shows one Aegis asset through the Python runtime.

.ROLE
Uses the Python runtime resolver to display an asset by ID.
#>

param(
    [string]$Argument = ''
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host 'Usage: .\cli\aegis.ps1 runtime:asset-show <asset-id>' -ForegroundColor Yellow
    exit 2
}

$commandRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $commandRoot '..\..')

Set-Location $repoRoot

$venvPython = Join-Path $repoRoot '.venv\Scripts\python.exe'

if (Test-Path $venvPython) {
    $pythonExe = $venvPython
}
else {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue

    if (-not $pythonCommand) {
        Write-Host 'Python was not found in PATH.' -ForegroundColor Red
        exit 3
    }

    $pythonExe = $pythonCommand.Source
}

& $pythonExe -m aegis_runtime --repo-root $repoRoot asset show $Argument
exit $LASTEXITCODE
