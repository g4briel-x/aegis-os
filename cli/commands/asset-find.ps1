<#
.SYNOPSIS
Searches Aegis OS registry files by keyword.

.DESCRIPTION
Searches all YAML registry files and displays matching lines.

.USAGE
.\cli\aegis.ps1 asset:find security
#>

param(
    [string]$Argument = ""
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Argument)) {
    Write-Host "Usage: .\cli\aegis.ps1 asset:find <keyword>" -ForegroundColor Yellow
    exit 2
}

$registryRoot = "registry"

if (-not (Test-Path $registryRoot)) {
    Write-Host "Registry folder not found: $registryRoot" -ForegroundColor Red
    exit 3
}

$files = @(
    Get-ChildItem -Path $registryRoot -Recurse -File |
    Where-Object {
        $_.Extension -in @(".yaml", ".yml")
    }
)

if ($files.Count -eq 0) {
    Write-Host "No registry YAML files found." -ForegroundColor Yellow
    exit 0
}

$results = @()
$escapedArgument = [regex]::Escape($Argument)

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName
    $lineNumber = 0

    foreach ($line in $content) {
        $lineNumber++

        if ($line -match $escapedArgument) {
            $relativePath = Resolve-Path -Path $file.FullName -Relative
            $relativePath = $relativePath -replace '^\.[\\/]', ''

            $results += [PSCustomObject]@{
                File = $relativePath
                Line = $lineNumber
                Text = $line.Trim()
            }
        }
    }
}

if ($results.Count -eq 0) {
    Write-Host "No matches found for: $Argument" -ForegroundColor Yellow
    exit 0
}

Write-Host "Matches for '$Argument':" -ForegroundColor Cyan
Write-Host ""

foreach ($result in $results) {
    Write-Host "$($result.File):$($result.Line)  $($result.Text)"
}

Write-Host ""
Write-Host "Total matches: $($results.Count)" -ForegroundColor Green

exit 0