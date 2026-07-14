
<#
.SYNOPSIS
Checks Git availability and repository status.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\doctor\check-git-status.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS — Git Status Check" -ForegroundColor Cyan

try {
    $gitVersion = git --version
    Write-Host "OK  $gitVersion" -ForegroundColor Green
}
catch {
    Write-Host "BAD Git is not available." -ForegroundColor Red
    exit 1
}

try {
    $insideRepo = git rev-parse --is-inside-work-tree
}
catch {
    Write-Host "BAD Current folder is not a Git repository." -ForegroundColor Red
    exit 1
}

if ($insideRepo -ne "true") {
    Write-Host "BAD Current folder is not inside a Git working tree." -ForegroundColor Red
    exit 1
}

Write-Host "OK  Inside Git repository" -ForegroundColor Green

$branch = git branch --show-current
Write-Host "Branch: $branch" -ForegroundColor Yellow

$status = git status --short

if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "OK  Working tree is clean" -ForegroundColor Green
}
else {
    Write-Host "WARN Working tree has changes:" -ForegroundColor Yellow
    $status | ForEach-Object { Write-Host $_ -ForegroundColor Yellow }
}

exit 0

