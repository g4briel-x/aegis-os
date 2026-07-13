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
