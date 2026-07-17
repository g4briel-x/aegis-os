<#
.SYNOPSIS
Displays the validated audit history of an execution session.

.ROLE
Delegates read-only execution audit history inspection
to the Aegis OS Python runtime.

.USAGE
.\cli\aegis.ps1 runtime:execution-audit-history <id>
.\cli\aegis.ps1 runtime:execution-audit-history <id> type=session-completed
.\cli\aegis.ps1 runtime:execution-audit-history <id> actor=operator:test
.\cli\aegis.ps1 runtime:execution-audit-history <id> limit=2 reverse
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
        'Usage: .\cli\aegis.ps1 runtime:execution-audit-history <session-id-or-workspace-id> [type=<event-type>] [actor=<actor>] [limit=<number>] [reverse]' `
        -ForegroundColor Yellow
}

if ([string]::IsNullOrWhiteSpace($Identifier)) {
    Show-Usage
    exit 2
}

$allowedEventTypes = @(
    'session-loaded'
    'orchestration-started'
    'state-transition'
    'plan-created'
    'dry-run-prepared'
    'session-completed'
    'session-failed'
    'session-cancelled'
)

$eventType = ''
$actor = ''
$limit = $null
$reverse = $false

foreach ($optionValue in $Options) {
    if ([string]::IsNullOrWhiteSpace($optionValue)) {
        continue
    }

    $option = $optionValue.Trim()

    if ($option -ieq 'reverse') {
        if ($reverse) {
            Write-Host `
                'The reverse option was supplied more than once.' `
                -ForegroundColor Red

            exit 2
        }

        $reverse = $true
        continue
    }

    if ($option.StartsWith('type=')) {
        if (-not [string]::IsNullOrWhiteSpace($eventType)) {
            Write-Host `
                'The event type filter was supplied more than once.' `
                -ForegroundColor Red

            exit 2
        }

        $eventType = $option.Substring(5).Trim()

        if ([string]::IsNullOrWhiteSpace($eventType)) {
            Write-Host `
                'The audit event type cannot be empty.' `
                -ForegroundColor Red

            exit 2
        }

        if ($allowedEventTypes -notcontains $eventType) {
            Write-Host `
                "Unsupported audit event type: $eventType" `
                -ForegroundColor Red

            $allowedValues = $allowedEventTypes -join ', '

            Write-Host `
                "Allowed values: $allowedValues" `
                -ForegroundColor Yellow

            exit 2
        }

        continue
    }

    if ($option.StartsWith('actor=')) {
        if (-not [string]::IsNullOrWhiteSpace($actor)) {
            Write-Host `
                'The actor filter was supplied more than once.' `
                -ForegroundColor Red

            exit 2
        }

        $actor = $option.Substring(6).Trim()

        if ([string]::IsNullOrWhiteSpace($actor)) {
            Write-Host `
                'The actor filter cannot be empty.' `
                -ForegroundColor Red

            exit 2
        }

        continue
    }

    if ($option.StartsWith('limit=')) {
        if ($null -ne $limit) {
            Write-Host `
                'The event limit was supplied more than once.' `
                -ForegroundColor Red

            exit 2
        }

        $limitText = $option.Substring(6).Trim()
        $parsedLimit = 0

        $isValidLimit = [int]::TryParse(
            $limitText,
            [ref]$parsedLimit
        )

        if (-not $isValidLimit -or $parsedLimit -le 0) {
            Write-Host `
                'The audit event limit must be a positive integer.' `
                -ForegroundColor Red

            exit 2
        }

        $limit = $parsedLimit
        continue
    }

    Write-Host `
        "Unsupported audit history option: $option" `
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
    'execution'
    'audit-history'
    $Identifier
)

if (-not [string]::IsNullOrWhiteSpace($eventType)) {
    $runtimeArguments += @(
        '--event-type'
        $eventType
    )
}

if (-not [string]::IsNullOrWhiteSpace($actor)) {
    $runtimeArguments += @(
        '--actor'
        $actor
    )
}

if ($null -ne $limit) {
    $runtimeArguments += @(
        '--limit'
        [string]$limit
    )
}

if ($reverse) {
    $runtimeArguments += '--reverse'
}

& $pythonExe @runtimeArguments

exit $LASTEXITCODE