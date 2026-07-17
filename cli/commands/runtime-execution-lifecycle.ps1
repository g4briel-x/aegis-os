<#
.SYNOPSIS
Applies a terminal lifecycle action to an execution session.

.ROLE
Delegates execution lifecycle management to the
Aegis OS Python runtime.
#>

param(
    [Parameter(Position = 0)]
    [string]$Identifier = '',

    [Parameter(Position = 1)]
    [ValidateSet('complete', 'fail', 'cancel')]
    [string]$Action = '',

    [Parameter(Position = 2)]
    [string]$Reason = '',

    [Parameter(Position = 3)]
    [string]$Actor = 'aegis-runtime'
)

$ErrorActionPreference = 'Stop'

if (
    [string]::IsNullOrWhiteSpace($Identifier) -or
    [string]::IsNullOrWhiteSpace($Action)
) {
    Write-Host `
        'Usage: .\cli\aegis.ps1 runtime:execution-lifecycle <session-id-or-workspace-id> <complete|fail|cancel> [reason] [actor]' `
        -ForegroundColor Yellow

    exit 2
}

$commandRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $commandRoot '..\..')

Set-Location $repoRoot

$venvPython = Join-Path `
    $repoRoot `
    '.venv\Scripts\python.exe'

if (Test-Path $venvPython) {
    $pythonExe = $venvPython
}
else {
    $pythonCommand = Get-Command `
        python `
        -ErrorAction SilentlyContinue

    if (-not $pythonCommand) {
        Write-Host `
            'Python was not found in PATH.' `
            -ForegroundColor Red

        exit 3
    }

    $pythonExe = $pythonCommand.Source
}

$runtimeArguments = @(
    '-m'
    'aegis_runtime'
    '--repo-root'
    $repoRoot
    'execution'
    'lifecycle'
    $Identifier
    $Action
)

if (-not [string]::IsNullOrWhiteSpace($Reason)) {
    $runtimeArguments += @(
        '--reason'
        $Reason
    )
}

if (-not [string]::IsNullOrWhiteSpace($Actor)) {
    $runtimeArguments += @(
        '--actor'
        $Actor
    )
}

& $pythonExe @runtimeArguments

exit $LASTEXITCODE