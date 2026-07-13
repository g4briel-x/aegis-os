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
