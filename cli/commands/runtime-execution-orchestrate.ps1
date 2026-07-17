<#
.SYNOPSIS
Orchestrates one persisted Aegis OS execution session.

.ROLE
Delegates persistent execution session orchestration to the
Aegis OS Python runtime.
#>

param(
    [string]$Argument = ''
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host `
        'Usage: .\cli\aegis.ps1 runtime:execution-orchestrate <session-id-or-workspace-id>' `
        -ForegroundColor Yellow

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
        Write-Host `
            'Python was not found in PATH.' `
            -ForegroundColor Red

        exit 3
    }

    $pythonExe = $pythonCommand.Source
}

& $pythonExe -m aegis_runtime `
    --repo-root $repoRoot `
    execution orchestrate `
    $Argument

exit $LASTEXITCODE