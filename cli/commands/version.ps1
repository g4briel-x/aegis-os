## FILE: `cli/commands/version.ps1`

```powershell
<#
.SYNOPSIS
Shows the Aegis OS CLI version.

.USAGE
.\cli\aegis.ps1 version
#>

$ErrorActionPreference = "Stop"

$configPath = "config\aegis.config.example.yaml"
$version = "0.1.0"

if (Test-Path $configPath) {
    $versionLine = Select-String -Path $configPath -Pattern "^\s*version:\s*(.+)\s*$" | Select-Object -First 1

    if ($versionLine) {
        $version = $versionLine.Matches[0].Groups[1].Value.Trim().Trim('"').Trim("'")
    }
}

Write-Host "Aegis OS CLI" -ForegroundColor Cyan
Write-Host "Version: $version" -ForegroundColor Yellow

exit 0
```
