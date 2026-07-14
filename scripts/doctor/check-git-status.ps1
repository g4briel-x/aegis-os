<#
.SYNOPSIS
Checks Git availability and repository status.

.USAGE
powershell -ExecutionPolicy Bypass -File scripts\doctor\check-git-status.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Aegis OS - Git Status Check" -ForegroundColor Cyan

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptRoot "..\..")

Set-Location $repoRoot

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

try {
    $branch = git branch --show-current

    if ([string]::IsNullOrWhiteSpace($branch)) {
        Write-Host "WARN Branch name unavailable or detached HEAD" -ForegroundColor Yellow
    }
    else {
        Write-Host "Branch: $branch" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "WARN Could not read current branch" -ForegroundColor Yellow
}

try {
    $gitStatus = git status --short

    if ([string]::IsNullOrWhiteSpace($gitStatus)) {
        Write-Host "OK  Working tree is clean" -ForegroundColor Green
    }
    else {
        Write-Host "WARN Working tree has changes:" -ForegroundColor Yellow

        foreach ($line in $gitStatus) {
            Write-Host $line -ForegroundColor Yellow
        }
    }
}
catch {
    Write-Host "BAD Could not read Git status" -ForegroundColor Red
    exit 1
}

exit 0