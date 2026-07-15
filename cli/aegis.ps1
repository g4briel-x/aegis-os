<#
.SYNOPSIS
Aegis OS CLI entrypoint.

.DESCRIPTION
Central command router for Aegis OS local repository operations.
.USAGE
.\cli\aegis.ps1 help
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 report
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 asset:find security
.\cli\aegis.ps1 asset:show engineering.senior-developer
.\cli\aegis.ps1 asset:related security.security-review-template
.\cli\aegis.ps1 asset:path business.pricing-strategy-template
.\cli\aegis.ps1 asset:open design.ux-flow-template
.\cli\aegis.ps1 skill:list
.\cli\aegis.ps1 playbook:list
.\cli\aegis.ps1 pattern:list
.\cli\aegis.ps1 template:list
.\cli\aegis.ps1 domain:list
.\cli\aegis.ps1 domain:assets security
.\cli\aegis.ps1 tag:list
.\cli\aegis.ps1 tag:assets api
.\cli\aegis.ps1 docs:list
.\cli\aegis.ps1 release:status
#>

param(
    [Parameter(Position = 0)]
    [string]$Command = "Help",
    
    [Parameter(Position = 1)]
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"


# Resolve the exact PowerShell host currently running this script
# (pwsh on PowerShell 7+/cross-platform, powershell.exe on Windows PowerShell 5.1)
# instead of hardcoding a binary name that may not exist on this machine.
$PSExe = (Get-Process -Id $PID).Path
$CliRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $CliRoot "..")
$CommandsRoot = Join-Path $CliRoot "commands"

Set-Location $RepoRoot

$commandMap = @{
    "help" = "help.ps1"

    "validate" = "validate.ps1"
    "doctor" = "doctor.ps1"
    "report" = "report.ps1"

    "registry:list" = "registry-list.ps1"

    "skill:list" = "skill-list.ps1"
    "playbook:list" = "playbook-list.ps1"
    "pattern:list" = "pattern-list.ps1"
    "template:list" = "template-list.ps1"
    "domain:list" = "domain-list.ps1"
    "tag:list" = "tag-list.ps1"
    "docs:list" = "docs-list.ps1"
    "release:status" = "release-status.ps1"

    "asset:find" = "asset-find.ps1"
    "asset:show" = "asset-show.ps1"
    "asset:related" = "asset-related.ps1"
    "asset:path" = "asset-path.ps1"
    "asset:open" = "asset-open.ps1"

    "domain:assets" = "domain-assets.ps1"
    "tag:assets" = "tag-assets.ps1"

    "runtime:status" = "runtime-status.ps1"
    "runtime:validate" = "runtime-validate.ps1"
    "runtime:registry-list" = "runtime-registry-list.ps1"
    "runtime:asset-show" = "runtime-asset-show.ps1"
    "runtime:asset-find" = "runtime-asset-find.ps1"
    "runtime:execution-plan" = "runtime-execution-plan.ps1"
    "runtime:execution-dry-run" = "runtime-execution-dry-run.ps1"

    "config:show" = "config-show.ps1"
    "config:path" = "config-path.ps1"
    "config:check" = "config-check.ps1"

    "version" = "version.ps1"
    "info" = "info.ps1"
    "status" = "status.ps1"

}

function Show-UnknownCommand {
    param(
        [string]$CommandName
    )

    Write-Host "Unknown command: $CommandName" -ForegroundColor Red
    Write-Host ""
    & $PSExe -ExecutionPolicy Bypass -File (Join-Path $CommandsRoot "help.ps1")
}

function Invoke-AegisCommand {
    param(
        [string]$CommandName,
        [string]$ArgumentValue
    )

    if (-not $commandMap.ContainsKey($CommandName)) {
        Show-UnknownCommand -CommandName $CommandName
        exit 1
    }

    $scriptName = $commandMap[$CommandName]
    $scriptPath = Join-Path $CommandsRoot $scriptName

    if (-not (Test-Path $scriptPath)) {
        Write-Host "Command script missing: $scriptPath" -ForegroundColor Red
        exit 1
    }

    if ([string]::IsNullOrWhiteSpace($ArgumentValue)) {
        & $PSExe -ExecutionPolicy Bypass -File $scriptPath
    }
    else {
        & $PSExe -ExecutionPolicy Bypass -File $scriptPath -Argument $ArgumentValue
    }

    exit $LASTEXITCODE
}

Invoke-AegisCommand -CommandName $Command -ArgumentValue $Argument
