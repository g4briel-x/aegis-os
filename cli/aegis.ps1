## FILE: `cli/aegis.ps1`

```powershell
<#
.SYNOPSIS
Aegis OS CLI entrypoint.

.USAGE
.\cli\aegis.ps1 help
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 report
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 asset:find security
#>

param(
    [Parameter(Position = 0)]
    [string]$Command = "help",

    [Parameter(Position = 1)]
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"

$CliRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $CliRoot "..")
$CommandsRoot = Join-Path $CliRoot "commands"

Set-Location $RepoRoot

function Invoke-AegisCommand {
    param(
        [string]$CommandName,
        [string]$ArgumentValue
    )

    $commandMap = @{
        "help" = "help.ps1"
        "validate" = "validate.ps1"
        "doctor" = "doctor.ps1"
        "report" = "report.ps1"
        "registry:list" = "registry-list.ps1"
        "asset:find" = "asset-find.ps1"
        "skill:list" = "skill-list.ps1"
        "playbook:list" = "playbook-list.ps1"
        "pattern:list" = "pattern-list.ps1"
        "template:list" = "template-list.ps1"
        "domain:list" = "domain-list.ps1"
        "tag:list" = "tag-list.ps1"
        "docs:list" = "docs-list.ps1"
        "release:status" = "release-status.ps1" 
        "asset:show" = "asset-show.ps1"
        "asset:related" = "asset-related.ps1"
        "asset:path" = "asset-path.ps1"
        "asset:open" = "asset-open.ps1"
        "domain:assets" = "domain-assets.ps1"
        "tag:assets" = "tag-assets.ps1"
    }

    if (-not $commandMap.ContainsKey($CommandName)) {
        Write-Host "Unknown command: $CommandName" -ForegroundColor Red
        Write-Host ""
        & powershell -ExecutionPolicy Bypass -File (Join-Path $CommandsRoot "help.ps1")
        exit 1
    }

    $scriptPath = Join-Path $CommandsRoot $commandMap[$CommandName]

    if (-not (Test-Path $scriptPath)) {
        Write-Host "Command script missing: $scriptPath" -ForegroundColor Red
        exit 1
    }

    if ([string]::IsNullOrWhiteSpace($ArgumentValue)) {
        & powershell -ExecutionPolicy Bypass -File $scriptPath
    }
    else {
        & powershell -ExecutionPolicy Bypass -File $scriptPath -Argument $ArgumentValue
    }

    exit $LASTEXITCODE
}

Invoke-AegisCommand -CommandName $Command -ArgumentValue $Argument
```
