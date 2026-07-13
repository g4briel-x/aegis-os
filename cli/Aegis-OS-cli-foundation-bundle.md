# Aegis OS — CLI Foundation Bundle

Ce fichier regroupe les premiers fichiers de la couche CLI Aegis OS :

- `cli/README.md`
- `cli/CLI_USAGE.md`
- `cli/aegis.ps1`
- `cli/commands/README.md`
- `cli/commands/help.ps1`
- `cli/commands/validate.ps1`
- `cli/commands/doctor.ps1`
- `cli/commands/report.ps1`
- `cli/commands/registry-list.ps1`
- `cli/commands/asset-find.ps1`

---

## FILE: `cli/README.md`

# Aegis OS — CLI Foundation

Version: 0.1.0  
Status: Draft  
Domain: CLI  
Category: Developer Tooling

---

# 1. Purpose

The Aegis OS CLI Foundation provides the first local command interface for interacting with the repository.

The CLI is a PowerShell-based entrypoint that wraps validation, doctor, report and registry inspection scripts.

---

# 2. Why CLI Exists

Before Aegis OS becomes a runtime system or marketplace, it needs a local command layer.

The CLI allows maintainers to run commands such as:

```powershell
.\cli\aegis.ps1 help
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 report
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 asset:find security
```

---

# 3. CLI Responsibilities

The CLI should:

```text
provide one entrypoint for common commands
wrap validation scripts
wrap doctor scripts
wrap report scripts
read registry files
find assets by keyword
prepare future automation
```

---

# 4. CLI Non-Goals

The first CLI does not:

```text
execute AI agents
install marketplace packages
modify registry files automatically
generate production code
replace Git
replace GitHub Actions
```

---

# 5. Final Principle

> The CLI turns repository operations into repeatable commands.

---

## FILE: `cli/CLI_USAGE.md`

# Aegis OS — CLI Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Main Command

Run from the repository root:

```powershell
.\cli\aegis.ps1 help
```

---

# 2. Available Commands

```powershell
.\cli\aegis.ps1 help
.\cli\aegis.ps1 validate
.\cli\aegis.ps1 doctor
.\cli\aegis.ps1 report
.\cli\aegis.ps1 registry:list
.\cli\aegis.ps1 asset:find security
```

---

# 3. Command Roles

## `help`

```text
Shows available CLI commands.
```

## `validate`

```text
Runs Aegis OS validation checks.
```

## `doctor`

```text
Runs repository health checks, validation and report generation.
```

## `report`

```text
Generates human-readable registry reports.
```

## `registry:list`

```text
Lists available registry YAML files.
```

## `asset:find`

```text
Searches registry files for a keyword such as security, api, pricing or ux.
```

---

# 4. Recommended Local Workflow

```powershell
.\cli\aegis.ps1 doctor
git status
git add .
git commit -m "..."
git push
```

---

# 5. Final Principle

> A CLI should reduce repeated manual commands without hiding what it does.

---

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

---

## FILE: `cli/commands/README.md`

# Aegis OS — CLI Commands

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains PowerShell command wrappers used by `cli/aegis.ps1`.

---

# 2. Commands

```text
help.ps1
validate.ps1
doctor.ps1
report.ps1
registry-list.ps1
asset-find.ps1
```

---

# 3. Rule

Command scripts should be thin wrappers.

Business logic should remain in:

```text
scripts/validation
scripts/reports
scripts/doctor
registry
```

---

# 4. Final Principle

> CLI commands should orchestrate existing scripts instead of duplicating their logic.

---

## FILE: `cli/commands/help.ps1`

```powershell
<#
.SYNOPSIS
Shows Aegis OS CLI help.
#>

Write-Host "Aegis OS CLI" -ForegroundColor Cyan
Write-Host ""
Write-Host "Usage:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 <command> [argument]"
Write-Host ""
Write-Host "Commands:" -ForegroundColor Yellow
Write-Host "  help                 Show this help message"
Write-Host "  validate             Run validation checks"
Write-Host "  doctor               Run repository health checks"
Write-Host "  report               Generate registry reports"
Write-Host "  registry:list        List registry YAML files"
Write-Host "  asset:find <keyword> Search registry files by keyword"
Write-Host ""
Write-Host "Examples:" -ForegroundColor Yellow
Write-Host "  .\cli\aegis.ps1 validate"
Write-Host "  .\cli\aegis.ps1 doctor"
Write-Host "  .\cli\aegis.ps1 asset:find security"
exit 0
```

---

## FILE: `cli/commands/validate.ps1`

```powershell
<#
.SYNOPSIS
Runs Aegis OS validation.
#>

$ErrorActionPreference = "Stop"

$scriptPath = "scripts\validation\validate-all.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Validation script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE
```

---

## FILE: `cli/commands/doctor.ps1`

```powershell
<#
.SYNOPSIS
Runs Aegis OS doctor.
#>

$ErrorActionPreference = "Stop"

$scriptPath = "scripts\doctor\aegis-doctor.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Doctor script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE
```

---

## FILE: `cli/commands/report.ps1`

```powershell
<#
.SYNOPSIS
Generates Aegis OS registry reports.
#>

$ErrorActionPreference = "Stop"

$scriptPath = "scripts\reports\generate-all-reports.ps1"

if (-not (Test-Path $scriptPath)) {
    Write-Host "Report script not found: $scriptPath" -ForegroundColor Red
    exit 1
}

& powershell -ExecutionPolicy Bypass -File $scriptPath
exit $LASTEXITCODE
```

---

## FILE: `cli/commands/registry-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS registry YAML files.
#>

$ErrorActionPreference = "Stop"

$registryRoot = "registry"

if (-not (Test-Path $registryRoot)) {
    Write-Host "Registry folder not found." -ForegroundColor Red
    exit 1
}

$files = Get-ChildItem -Path $registryRoot -Recurse -File -Include *.yaml, *.yml

if ($files.Count -eq 0) {
    Write-Host "No registry YAML files found." -ForegroundColor Yellow
    exit 0
}

Write-Host "Aegis OS Registries" -ForegroundColor Cyan
Write-Host ""

foreach ($file in $files | Sort-Object FullName) {
    Write-Host (Resolve-Path $file.FullName -Relative)
}

exit 0
```

---

## FILE: `cli/commands/asset-find.ps1`

```powershell
<#
.SYNOPSIS
Searches Aegis OS registry files by keyword.

.USAGE
.\cli\aegis.ps1 asset:find security
#>

param(
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:find <keyword>" -ForegroundColor Yellow
    exit 1
}

$registryRoot = "registry"

if (-not (Test-Path $registryRoot)) {
    Write-Host "Registry folder not found." -ForegroundColor Red
    exit 1
}

$files = Get-ChildItem -Path $registryRoot -Recurse -File -Include *.yaml, *.yml
$matches = @()

foreach ($file in $files) {
    $content = Get-Content $file.FullName
    $lineNumber = 0

    foreach ($line in $content) {
        $lineNumber++

        if ($line -match [regex]::Escape($Argument)) {
            $matches += [PSCustomObject]@{
                File = Resolve-Path $file.FullName -Relative
                Line = $lineNumber
                Text = $line.Trim()
            }
        }
    }
}

if ($matches.Count -eq 0) {
    Write-Host "No matches found for: $Argument" -ForegroundColor Yellow
    exit 0
}

Write-Host "Matches for '$Argument':" -ForegroundColor Cyan
Write-Host ""

foreach ($match in $matches) {
    Write-Host "$($match.File):$($match.Line)  $($match.Text)"
}

exit 0
```
