# Aegis OS — CLI Registry Commands Bundle

Ce fichier regroupe les commandes CLI spécialisées pour explorer les registries Aegis OS :

- `cli/commands/skill-list.ps1`
- `cli/commands/playbook-list.ps1`
- `cli/commands/pattern-list.ps1`
- `cli/commands/template-list.ps1`
- `cli/commands/domain-list.ps1`
- `cli/commands/tag-list.ps1`
- `cli/commands/release-status.ps1`
- `cli/commands/docs-list.ps1`
- `cli/CLI_REGISTRY_COMMANDS.md`
- `cli/aegis.ps1` update note

---

## FILE: `cli/CLI_REGISTRY_COMMANDS.md`

# Aegis OS — CLI Registry Commands

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This document defines the registry exploration commands for the Aegis OS CLI.

These commands allow maintainers to inspect skills, playbooks, patterns, templates, domains, tags, docs and releases from the terminal.

---

# 2. Commands

```powershell
.\cli\aegis.ps1 skill:list
.\cli\aegis.ps1 playbook:list
.\cli\aegis.ps1 pattern:list
.\cli\aegis.ps1 template:list
.\cli\aegis.ps1 domain:list
.\cli\aegis.ps1 tag:list
.\cli\aegis.ps1 docs:list
.\cli\aegis.ps1 release:status
```

---

# 3. Role

These commands are lightweight readers.

They do not modify files.  
They read registry files and display useful information for humans.

---

# 4. Future Direction

Later versions can support:

```text
JSON output
filter by domain
filter by tag
filter by maturity
show related assets
validate one asset
open asset path
generate docs from registry
```

---

# 5. Final Principle

> CLI registry commands should make Aegis OS assets discoverable without manually opening YAML files.

---

## FILE: `cli/commands/skill-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS skills from the skills registry.

.USAGE
.\cli\aegis.ps1 skill:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\skills\skills.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Skills registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Skills" -ForegroundColor Cyan
Write-Host ""

$content = Get-Content $registryPath
$currentId = ""
$currentName = ""
$currentDomain = ""
$currentPath = ""

foreach ($line in $content) {
    if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
        if (-not [string]::IsNullOrWhiteSpace($currentId)) {
            Write-Host "$currentId" -ForegroundColor Yellow
            Write-Host "  Name:   $currentName"
            Write-Host "  Domain: $currentDomain"
            Write-Host "  Path:   $currentPath"
            Write-Host ""
        }

        $currentId = $Matches[1].Trim()
        $currentName = ""
        $currentDomain = ""
        $currentPath = ""
    }
    elseif ($line -match "^\s*name:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentName = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*domain:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentDomain = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*path:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentPath = $Matches[1].Trim()
    }
}

if (-not [string]::IsNullOrWhiteSpace($currentId)) {
    Write-Host "$currentId" -ForegroundColor Yellow
    Write-Host "  Name:   $currentName"
    Write-Host "  Domain: $currentDomain"
    Write-Host "  Path:   $currentPath"
}

exit 0
```

---

## FILE: `cli/commands/playbook-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS playbooks from the playbooks registry.

.USAGE
.\cli\aegis.ps1 playbook:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\playbooks\playbooks.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Playbooks registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Playbooks" -ForegroundColor Cyan
Write-Host ""

$content = Get-Content $registryPath
$currentId = ""
$currentName = ""
$currentDomain = ""
$currentPath = ""

foreach ($line in $content) {
    if ($line -match "^\s*-\s*id:\s*(.+)\s*$") {
        if (-not [string]::IsNullOrWhiteSpace($currentId)) {
            Write-Host "$currentId" -ForegroundColor Yellow
            Write-Host "  Name:   $currentName"
            Write-Host "  Domain: $currentDomain"
            Write-Host "  Path:   $currentPath"
            Write-Host ""
        }

        $currentId = $Matches[1].Trim()
        $currentName = ""
        $currentDomain = ""
        $currentPath = ""
    }
    elseif ($line -match "^\s*name:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentName = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*domain:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentDomain = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*path:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentPath = $Matches[1].Trim()
    }
}

if (-not [string]::IsNullOrWhiteSpace($currentId)) {
    Write-Host "$currentId" -ForegroundColor Yellow
    Write-Host "  Name:   $currentName"
    Write-Host "  Domain: $currentDomain"
    Write-Host "  Path:   $currentPath"
}

exit 0
```

---

## FILE: `cli/commands/pattern-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS patterns from the patterns registry.

.USAGE
.\cli\aegis.ps1 pattern:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\patterns\patterns.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Patterns registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Patterns" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*-\s*id:\s*(.+)$" | ForEach-Object {
    $id = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $id -ForegroundColor Yellow
}

exit 0
```

---

## FILE: `cli/commands/template-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS templates from the templates registry.

.USAGE
.\cli\aegis.ps1 template:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\templates\templates.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Templates registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Templates" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*-\s*id:\s*(.+)$" | ForEach-Object {
    $id = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $id -ForegroundColor Yellow
}

exit 0
```

---

## FILE: `cli/commands/domain-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS domains from the domains registry.

.USAGE
.\cli\aegis.ps1 domain:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\domains\domains.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Domains registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Domains" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*slug:\s*(.+)$" | ForEach-Object {
    $slug = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $slug -ForegroundColor Yellow
}

exit 0
```

---

## FILE: `cli/commands/tag-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS tags from the tags registry.

.USAGE
.\cli\aegis.ps1 tag:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\tags\tags.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Tags registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Tags" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*name:\s*(.+)$" | ForEach-Object {
    $name = $_.Matches[0].Groups[1].Value.Trim()
    if ($name -ne "Tags Registry") {
        Write-Host $name -ForegroundColor Yellow
    }
}

exit 0
```

---

## FILE: `cli/commands/docs-list.ps1`

```powershell
<#
.SYNOPSIS
Lists Aegis OS docs from the docs registry.

.USAGE
.\cli\aegis.ps1 docs:list
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\docs\docs.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Docs registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Docs" -ForegroundColor Cyan
Write-Host ""

Select-String -Path $registryPath -Pattern "^\s*-\s*id:\s*(.+)$" | ForEach-Object {
    $id = $_.Matches[0].Groups[1].Value.Trim()
    Write-Host $id -ForegroundColor Yellow
}

exit 0
```

---

## FILE: `cli/commands/release-status.ps1`

```powershell
<#
.SYNOPSIS
Shows Aegis OS release status from the releases registry.

.USAGE
.\cli\aegis.ps1 release:status
#>

$ErrorActionPreference = "Stop"

$registryPath = "registry\releases\releases.registry.yaml"

if (-not (Test-Path $registryPath)) {
    Write-Host "Releases registry not found: $registryPath" -ForegroundColor Red
    exit 1
}

Write-Host "Aegis OS Releases" -ForegroundColor Cyan
Write-Host ""

$content = Get-Content $registryPath
$currentId = ""
$currentName = ""
$currentVersion = ""
$currentStatus = ""
$currentMaturity = ""

foreach ($line in $content) {
    if ($line -match "^\s*-\s*id:\s*(release\..+)\s*$") {
        if (-not [string]::IsNullOrWhiteSpace($currentId)) {
            Write-Host "$currentId" -ForegroundColor Yellow
            Write-Host "  Name:     $currentName"
            Write-Host "  Version:  $currentVersion"
            Write-Host "  Status:   $currentStatus"
            Write-Host "  Maturity: $currentMaturity"
            Write-Host ""
        }

        $currentId = $Matches[1].Trim()
        $currentName = ""
        $currentVersion = ""
        $currentStatus = ""
        $currentMaturity = ""
    }
    elseif ($line -match "^\s*name:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentName = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*version:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentVersion = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*status:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentStatus = $Matches[1].Trim()
    }
    elseif ($line -match "^\s*maturity:\s*(.+)\s*$" -and -not [string]::IsNullOrWhiteSpace($currentId)) {
        $currentMaturity = $Matches[1].Trim()
    }
}

if (-not [string]::IsNullOrWhiteSpace($currentId)) {
    Write-Host "$currentId" -ForegroundColor Yellow
    Write-Host "  Name:     $currentName"
    Write-Host "  Version:  $currentVersion"
    Write-Host "  Status:   $currentStatus"
    Write-Host "  Maturity: $currentMaturity"
}

exit 0
```

---

## FILE: `cli/aegis.ps1` — update note

Add these commands to the `$commandMap` inside `cli/aegis.ps1`:

```powershell
"skill:list" = "skill-list.ps1"
"playbook:list" = "playbook-list.ps1"
"pattern:list" = "pattern-list.ps1"
"template:list" = "template-list.ps1"
"domain:list" = "domain-list.ps1"
"tag:list" = "tag-list.ps1"
"docs:list" = "docs-list.ps1"
"release:status" = "release-status.ps1"
```

Also add them to `cli/commands/help.ps1` so they appear in the help output.
