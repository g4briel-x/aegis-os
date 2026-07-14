
<#
.SYNOPSIS
Checks whether the Aegis OS CLI profile function is installed.

.USAGE
powershell -ExecutionPolicy Bypass -File install\check-aegis-cli.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — CLI Install Check" -ForegroundColor Cyan

$profilePath = $PROFILE.CurrentUserCurrentHost
$startMarker = "# >>> AEGIS OS CLI >>>"

if (-not (Test-Path $profilePath)) {
    Write-Host "PowerShell profile does not exist:" -ForegroundColor Red
    Write-Host $profilePath -ForegroundColor Yellow
    exit 1
}

$profileContent = Get-Content $profilePath -Raw

if ($profileContent -match [regex]::Escape($startMarker)) {
    Write-Host "Aegis CLI profile block is installed." -ForegroundColor Green
    Write-Host $profilePath -ForegroundColor Yellow
}
else {
    Write-Host "Aegis CLI profile block is not installed." -ForegroundColor Yellow
    Write-Host "Run:" -ForegroundColor Cyan
    Write-Host "powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "After restarting PowerShell, test with:" -ForegroundColor Cyan
Write-Host "aegis help" -ForegroundColor Yellow

exit 0
