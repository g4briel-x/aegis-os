<#
.SYNOPSIS
Displays the current Aegis OS CLI version.

.USAGE
.\cli\aegis.ps1 version
#>

$ErrorActionPreference = 'Stop'

$version = '0.5.0'

Write-Host 'Aegis OS CLI' -ForegroundColor Cyan
Write-Host ('Version: {0}' -f $version) -ForegroundColor Green

exit 0