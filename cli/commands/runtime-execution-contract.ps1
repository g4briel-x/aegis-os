<#
.SYNOPSIS
Builds and validates an execution contract through the Python runtime.

.ROLE
Delegates execution contract generation and validation to the Aegis OS Python runtime.
#>

param(
    [string]$Argument = ''
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host 'Usage: .\cli\aegis.ps1 runtime:execution-contract <asset-id>' -ForegroundColor Yellow
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

& $pythonExe -m aegis_runtime --repo-root $repoRoot execution contract $Argument
exit $LASTEXITCODE