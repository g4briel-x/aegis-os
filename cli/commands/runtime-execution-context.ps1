<#
.SYNOPSIS
Builds a resolved execution context through the Python runtime.

.ROLE
Delegates execution context building and input resolution to the
Aegis OS Python runtime.
#>

param(
    [string]$Argument = ''
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host 'Usage: .\cli\aegis.ps1 runtime:execution-context <asset-id>' -ForegroundColor Yellow
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

& $pythonExe -m aegis_runtime `
    --repo-root $repoRoot `
    execution context `
    $Argument

exit $LASTEXITCODE