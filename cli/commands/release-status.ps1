
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
