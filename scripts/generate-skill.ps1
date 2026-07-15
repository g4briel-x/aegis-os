# ==========================================
# Aegis OS Skill Factory
# Generator Engine v1
# ==========================================
# Bug fixes:
#   - Get-YamlValue now uses anchored regex (^key:) to avoid matching
#     partial key names like "display_name" when searching for "name".
#   - exit without code replaced by exit 1 so CI/CD detects failures.
# ==========================================

param(
    [string]$SkillDefinition
)

$ErrorActionPreference = "Stop"

if (-not $SkillDefinition) {
    Write-Host "Usage: .\generate-skill.ps1 <skill.yaml>" -ForegroundColor Yellow
    exit 1   # Fix: exit 1 (erreur), pas exit 0 (succès)
}

if (-not (Test-Path $SkillDefinition)) {
    Write-Host "Skill definition file not found: $SkillDefinition" -ForegroundColor Red
    exit 1
}

$content = Get-Content $SkillDefinition -Raw

# Fix: regex ancré en début de ligne ((?m) = multiline) pour éviter de matcher
# "display_name:", "short_name:", etc. quand on cherche "name:"
function Get-YamlValue($key) {
    if ($content -match "(?m)^${key}:\s*(.+)") {
        return $Matches[1].Trim()
    }
    return ""
}

$name     = Get-YamlValue "name"
$category = Get-YamlValue "category"
$path     = Get-YamlValue "path"

if ([string]::IsNullOrWhiteSpace($path)) {
    Write-Host "Missing 'path' field in skill definition: $SkillDefinition" -ForegroundColor Red
    exit 1   # Fix: exit 1
}

if ([string]::IsNullOrWhiteSpace($name)) {
    Write-Host "Missing 'name' field in skill definition: $SkillDefinition" -ForegroundColor Red
    exit 1
}

$skillPath = Join-Path "skills" $path

New-Item (Join-Path $skillPath "examples") -ItemType Directory -Force | Out-Null


@"
# $name

## Category

$category

## Mission

$(Get-YamlValue "mission")

## Role

$(Get-YamlValue "role")

## Responsibilities

$(Get-YamlValue "responsibilities")

## Principles

- Quality first
- Evidence based reasoning
- Continuous improvement
"@ | Out-File (Join-Path $skillPath "SKILL.md") -Encoding UTF8


@"
# $name

Professional expert module of Aegis OS.

## Mission

$(Get-YamlValue "mission")

## Usage

Activated by Orchestration Engine.
"@ | Out-File (Join-Path $skillPath "README.md") -Encoding UTF8


@"
# Expertise

$name

$(Get-YamlValue "expertise")

"@ | Out-File (Join-Path $skillPath "expertise.md") -Encoding UTF8


@"
# Workflows

Standard workflow:

1. Analyze
2. Investigate
3. Execute
4. Validate
5. Document

"@ | Out-File (Join-Path $skillPath "workflows.md") -Encoding UTF8


@"
# Checklists

[ ] Requirement understood

[ ] Evidence collected

[ ] Solution validated

[ ] Documentation completed

"@ | Out-File (Join-Path $skillPath "checklists.md") -Encoding UTF8


@"
# Activation Prompt

Activate $name Skill.

Apply professional methodology.

"@ | Out-File (Join-Path $skillPath "prompts.md") -Encoding UTF8


@"
# Examples

Practical examples for:

$name

"@ | Out-File (Join-Path $skillPath "examples\examples.md") -Encoding UTF8


Write-Host "Skill generated: $name" -ForegroundColor Green
exit 0
