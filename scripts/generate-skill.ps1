# ==========================================
# Aegis OS Skill Factory
# Generator Engine v1
# ==========================================

param(
    [string]$SkillDefinition
)

if (-not $SkillDefinition) {
    Write-Host "Usage: .\generate-skill.ps1 <skill.yaml>"
    exit
}

$content = Get-Content $SkillDefinition -Raw

function Get-YamlValue($key) {
    if ($content -match "${key}:\s*(.*)") {
        return $matches[1].Trim()
    }
    return ""
}

$name = Get-YamlValue "name"
$category = Get-YamlValue "category"
$path = Get-YamlValue "path"

if (!$path) {
    Write-Host "Missing skill path"
    exit
}

$skillPath = "skills\$path"

New-Item "$skillPath\examples" -ItemType Directory -Force | Out-Null


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
"@ | Out-File "$skillPath\SKILL.md" -Encoding UTF8


@"
# $name

Professional expert module of Aegis OS.

## Mission

$(Get-YamlValue "mission")

## Usage

Activated by Orchestration Engine.
"@ | Out-File "$skillPath\README.md" -Encoding UTF8


@"
# Expertise

$name

$(Get-YamlValue "expertise")

"@ | Out-File "$skillPath\expertise.md" -Encoding UTF8


@"
# Workflows

Standard workflow:

1. Analyze
2. Investigate
3. Execute
4. Validate
5. Document

"@ | Out-File "$skillPath\workflows.md" -Encoding UTF8


@"
# Checklists

[ ] Requirement understood

[ ] Evidence collected

[ ] Solution validated

[ ] Documentation completed

"@ | Out-File "$skillPath\checklists.md" -Encoding UTF8


@"
# Activation Prompt

Activate $name Skill.

Apply professional methodology.

"@ | Out-File "$skillPath\prompts.md" -Encoding UTF8


@"
# Examples

Practical examples for:

$name

"@ | Out-File "$skillPath\examples\examples.md" -Encoding UTF8


Write-Host "Skill generated:" $name -ForegroundColor Green