<#
.SYNOPSIS
Runs Aegis OS CLI runtime command tests.

.DESCRIPTION
Checks that PowerShell CLI commands correctly delegate to the Python runtime.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\testing\test-cli-runtime-commands.ps1
#>

$ErrorActionPreference = 'Stop'

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot '..\..')

Set-Location $repoRoot

Write-Host `
    'Aegis OS - CLI Runtime Command Test' `
    -ForegroundColor Cyan

$commands = @(
    @('runtime:status', ''),
    @('runtime:registry-list', ''),
    @('runtime:asset-find', 'security'),
    @(
        'runtime:asset-show',
        'security.review-api-security'
    ),
    @(
        'runtime:execution-plan',
        'security.review-api-security'
    ),
    @(
        'runtime:execution-dry-run',
        'security.review-api-security'
    ),
    @(
        'runtime:execution-contract',
        'security.review-api-security'
    ),
    @(
        'runtime:execution-context',
        'security.review-api-security'
    ),
    @(
        'runtime:execution-session',
        'security.review-api-security'
    ),
    @('runtime:validate', '')
)

foreach ($commandSpec in $commands) {
    $command = $commandSpec[0]
    $argument = $commandSpec[1]

    Write-Host ''

    if ([string]::IsNullOrWhiteSpace($argument)) {
        Write-Host (
            'Running: .\cli\aegis.ps1 {0}' `
                -f $command
        ) -ForegroundColor Yellow

        & powershell `
            -ExecutionPolicy Bypass `
            -File 'cli\aegis.ps1' `
            $command
    }
    else {
        Write-Host (
            'Running: .\cli\aegis.ps1 {0} {1}' `
                -f $command, $argument
        ) -ForegroundColor Yellow

        & powershell `
            -ExecutionPolicy Bypass `
            -File 'cli\aegis.ps1' `
            $command `
            $argument
    }

    if ($LASTEXITCODE -ne 0) {
        Write-Error (
            'CLI runtime command failed: {0} {1}' `
                -f $command, $argument
        )

        exit $LASTEXITCODE
    }
}

$workspaceRoot = Join-Path `
    $repoRoot `
    '.aegis\workspaces'

if (-not (Test-Path $workspaceRoot)) {
    Write-Error `
        'No persisted execution workspace was created.'

    exit 1
}

$latestWorkspace = Get-ChildItem `
    $workspaceRoot `
    -Directory |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if (-not $latestWorkspace) {
    Write-Error `
        'No persisted execution workspace was found.'

    exit 1
}

Write-Host ''
Write-Host (
    'Running: .\cli\aegis.ps1 ' `
    + 'runtime:execution-orchestrate {0}' `
    -f $latestWorkspace.Name
) -ForegroundColor Yellow

$orchestrationOutput = & powershell `
    -ExecutionPolicy Bypass `
    -File 'cli\aegis.ps1' `
    'runtime:execution-orchestrate' `
    $latestWorkspace.Name 2>&1

$orchestrationExitCode = $LASTEXITCODE

$orchestrationOutput | ForEach-Object {
    Write-Host $_
}

if ($orchestrationExitCode -ne 0) {
    Write-Error (
        'CLI runtime command failed: ' `
        + 'runtime:execution-orchestrate {0}' `
        -f $latestWorkspace.Name
    )

    exit $orchestrationExitCode
}

$orchestrationText = (
    $orchestrationOutput -join `
        [Environment]::NewLine
)

if (
    $orchestrationText -notmatch
    'Orchestration:\s+passed'
) {
    Write-Error `
        'Execution orchestration did not report success.'

    exit 1
}

if (
    $orchestrationText -notmatch
    'State:\s+dry-run-ready'
) {
    Write-Error `
        'Execution orchestration did not reach the dry-run-ready state.'

    exit 1
}

Write-Host ''
Write-Host (
    'Running: .\cli\aegis.ps1 ' `
    + 'runtime:execution-lifecycle {0} complete' `
    -f $latestWorkspace.Name
) -ForegroundColor Yellow

$lifecycleReason = 'CLI runtime lifecycle completed.'
$lifecycleActor = 'test:cli-runtime'

$lifecycleOutput = & powershell `
    -ExecutionPolicy Bypass `
    -File 'cli\aegis.ps1' `
    'runtime:execution-lifecycle' `
    $latestWorkspace.Name `
    'complete' `
    $lifecycleReason `
    $lifecycleActor 2>&1

$lifecycleExitCode = $LASTEXITCODE

$lifecycleOutput | ForEach-Object {
    Write-Host $_
}

if ($lifecycleExitCode -ne 0) {
    Write-Error (
        'CLI runtime command failed: ' `
        + 'runtime:execution-lifecycle {0} complete' `
        -f $latestWorkspace.Name
    )

    exit $lifecycleExitCode
}

$lifecycleText = (
    $lifecycleOutput -join `
        [Environment]::NewLine
)

if (
    $lifecycleText -notmatch
    'Lifecycle:\s+passed'
) {
    Write-Error `
        'Execution lifecycle did not report success.'

    exit 1
}

if (
    $lifecycleText -notmatch
    'Action:\s+complete'
) {
    Write-Error `
        'Execution lifecycle did not report the complete action.'

    exit 1
}

if (
    $lifecycleText -notmatch
    'State:\s+completed'
) {
    Write-Error `
        'Execution lifecycle did not reach the completed state.'

    exit 1
}

if (
    $lifecycleText -notmatch
    'Actor:\s+test:cli-runtime'
) {
    Write-Error `
        'Execution lifecycle did not preserve the supplied actor.'

    exit 1
}

Write-Host ''
Write-Host (
    'Running: .\cli\aegis.ps1 runtime:session-show {0}' `
        -f $latestWorkspace.Name
) -ForegroundColor Yellow

$sessionShowOutput = & powershell `
    -ExecutionPolicy Bypass `
    -File 'cli\aegis.ps1' `
    'runtime:session-show' `
    $latestWorkspace.Name 2>&1

$sessionShowExitCode = $LASTEXITCODE

$sessionShowOutput | ForEach-Object {
    Write-Host $_
}

if ($sessionShowExitCode -ne 0) {
    Write-Error (
        'CLI runtime command failed: runtime:session-show {0}' `
            -f $latestWorkspace.Name
    )

    exit $sessionShowExitCode
}

$sessionShowText = (
    $sessionShowOutput -join `
        [Environment]::NewLine
)

if (
    $sessionShowText -notmatch
    'State:\s+completed'
) {
    Write-Error `
        'Persisted execution session did not retain the completed state.'

    exit 1
}

Write-Host ''
Write-Host `
    'CLI runtime command test passed.' `
    -ForegroundColor Green

exit 0