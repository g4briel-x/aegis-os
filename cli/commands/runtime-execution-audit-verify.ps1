<#
.SYNOPSIS
Verifies the integrity of an execution audit journal.

.ROLE
Delegates structural and cryptographic execution audit
verification to the Aegis OS Python runtime.

.USAGE
.\cli\aegis.ps1 runtime:execution-audit-verify <id>
.\cli\aegis.ps1 runtime:execution-audit-verify <id> json
#>

param(
    [Parameter(Position = 0)]
    [string]$Identifier = '',

    [Parameter(
        Position = 1,
        ValueFromRemainingArguments = $true
    )]
    [string[]]$Options = @()
)

$ErrorActionPreference = 'Stop'

function Show-Usage {
    Write-Host `
        'Usage: .\cli\aegis.ps1 runtime:execution-audit-verify <session-id-or-workspace-id> [json]' `
        -ForegroundColor Yellow
}

if ([string]::IsNullOrWhiteSpace($Identifier)) {
    Show-Usage
    exit 2
}

$jsonOutput = $false

foreach ($optionValue in $Options) {
    if ([string]::IsNullOrWhiteSpace($optionValue)) {
        continue
    }

    $option = $optionValue.Trim()

    if ($option -ieq 'json') {
        if ($jsonOutput) {
            Write-Host `
                'The json option was supplied more than once.' `
                -ForegroundColor Red

            exit 2
        }

        $jsonOutput = $true
        continue
    }

    Write-Host `
        "Unsupported audit verification option: $option" `
        -ForegroundColor Red

    Show-Usage
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
    [string]$repoRoot
)

if ($jsonOutput) {
    $runtimeArguments += '--json'
}

$runtimeArguments += @(
    'execution'
    'audit-verify'
    $Identifier
)

& $pythonExe @runtimeArguments

exit $LASTEXITCODE