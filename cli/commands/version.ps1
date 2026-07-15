<#
.SYNOPSIS
Displays the current Aegis OS CLI version.

.DESCRIPTION
Reads the version from the releases registry to avoid version drift.
Quality fix: version was previously hardcoded as '0.5.0' in this file,
risking desynchronization with the actual registry at each release.

.USAGE
.\cli\aegis.ps1 version
#>

$ErrorActionPreference = 'Stop'

$releasesPath = "registry\releases\releases.registry.yaml"

$version = 'unknown'

if (Test-Path $releasesPath) {
    $content = Get-Content $releasesPath -Raw
    # Recherche de la première entrée de version dans le fichier
    if ($content -match '(?m)^\s{4}version:\s*(.+)') {
        $version = $Matches[1].Trim().Trim('"').Trim("'")
    }
}
else {
    # Fallback si le registre n'est pas disponible
    $version = '0.5.0'
    Write-Host "WARN Releases registry not found, using fallback version." -ForegroundColor Yellow
}

Write-Host 'Aegis OS CLI' -ForegroundColor Cyan
Write-Host ('Version: {0}' -f $version) -ForegroundColor Green

exit 0
