
<#
.SYNOPSIS
Removes the Aegis OS CLI PowerShell function from the user profile.

.USAGE
powershell -ExecutionPolicy Bypass -File install\uninstall-aegis-cli.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — CLI Uninstaller" -ForegroundColor Cyan

$profilePath = $PROFILE.CurrentUserCurrentHost

if (-not (Test-Path $profilePath)) {
    Write-Host "PowerShell profile not found. Nothing to uninstall." -ForegroundColor Yellow
    exit 0
}

$startMarker = "# >>> AEGIS OS CLI >>>"
$endMarker = "# <<< AEGIS OS CLI <<<"

$profileContent = Get-Content $profilePath -Raw

if (-not ($profileContent -match [regex]::Escape($startMarker))) {
    Write-Host "Aegis CLI profile block not found. Nothing to uninstall." -ForegroundColor Yellow
    exit 0
}

$pattern = [regex]::Escape($startMarker) + ".*?" + [regex]::Escape($endMarker)
$newContent = [regex]::Replace($profileContent, $pattern, "", "Singleline").TrimEnd() + "`r`n"

Set-Content -Path $profilePath -Value $newContent -Encoding UTF8

Write-Host "Aegis CLI removed from PowerShell profile." -ForegroundColor Green
Write-Host "Restart PowerShell to complete uninstall." -ForegroundColor Yellow

exit 0