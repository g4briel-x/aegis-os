
<#
.SYNOPSIS
Installs the Aegis OS CLI as a PowerShell function.

.DESCRIPTION
Adds an `aegis` function to the current user's PowerShell profile.
The function routes commands to this repository's cli\aegis.ps1 file.

.USAGE
powershell -ExecutionPolicy Bypass -File install\install-aegis-cli.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — CLI Installer" -ForegroundColor Cyan

$repoRoot = Resolve-Path "."
$cliPath = Join-Path $repoRoot "cli\aegis.ps1"

if (-not (Test-Path $cliPath)) {
    Write-Host "Missing CLI entrypoint: $cliPath" -ForegroundColor Red
    exit 1
}

$profilePath = $PROFILE.CurrentUserCurrentHost
$profileDir = Split-Path -Parent $profilePath

if (-not (Test-Path $profileDir)) {
    New-Item -ItemType Directory -Path $profileDir -Force | Out-Null
}

if (-not (Test-Path $profilePath)) {
    New-Item -ItemType File -Path $profilePath -Force | Out-Null
}

$startMarker = "# >>> AEGIS OS CLI >>>"
$endMarker = "# <<< AEGIS OS CLI <<<"

$profileContent = Get-Content $profilePath -Raw

if ($profileContent -match [regex]::Escape($startMarker)) {
    Write-Host "Existing Aegis CLI profile block found. Updating..." -ForegroundColor Yellow

    $pattern = [regex]::Escape($startMarker) + ".*?" + [regex]::Escape($endMarker)
    $profileContent = [regex]::Replace($profileContent, $pattern, "", "Singleline")
}

$block = @"

$startMarker
function aegis {
    param(
        [Parameter(ValueFromRemainingArguments = `$true)]
        [string[]]`$Args
    )

    & "$cliPath" @Args
}
$endMarker
"@

$newContent = $profileContent.TrimEnd() + "`r`n" + $block + "`r`n"
Set-Content -Path $profilePath -Value $newContent -Encoding UTF8

Write-Host "Aegis CLI installed in PowerShell profile:" -ForegroundColor Green
Write-Host $profilePath -ForegroundColor Yellow
Write-Host ""
Write-Host "Restart PowerShell, then run:" -ForegroundColor Cyan
Write-Host "aegis help" -ForegroundColor Yellow

exit 0
