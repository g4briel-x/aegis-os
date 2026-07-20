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

$results = [System.Collections.Generic.List[object]]::new()

# Select-String is a compiled cmdlet and is significantly faster than
# reading each file with Get-Content and testing every line with -match
# in a PowerShell-level loop, especially as the registry grows.
$matches = $files | Select-String -Pattern $Argument -SimpleMatch

foreach ($match in $matches) {
    $relativePath = Resolve-Path -Path $match.Path -Relative
    $relativePath = $relativePath -replace '^\.[\\/]', ''

    $results.Add([PSCustomObject]@{
        File = $relativePath
        Line = $match.LineNumber
        Text = $match.Line.Trim()
    })
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