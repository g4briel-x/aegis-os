# ==========================================
# Aegis OS - Skills Generator
# ==========================================
# Quality fix: $template uses [ordered]@{} instead of @{} to guarantee
# deterministic file creation order across executions.
# PowerShell hashtables do NOT guarantee key iteration order.
# ==========================================

$SkillsRoot = "skills"

$skills = @(
    "engineering/senior-debugger",
    "engineering/software-architect",
    "engineering/senior-developer",
    "engineering/database-engineer",

    "product/product-manager-saas",
    "product/business-analyst",

    "design/ux-ui-designer",

    "infrastructure/devops-engineer",
    "infrastructure/cloud-architect",
    "infrastructure/security-engineer",

    "management/technical-project-manager"
)

# Fix: [ordered]@{} garantit l'ordre d'itération des clés
$template = [ordered]@{
    "README.md" = @"
# Aegis OS Skill

## Overview

Professional expert module of Aegis OS.

## Role

Define the mission and capabilities of this Skill.

## Usage

Activated through Aegis OS Orchestration Engine.
"@

    "SKILL.md" = @"
# Skill Identity

## Name

Aegis OS Expert Skill

## Mission

Define expert mission.

## Responsibilities

- Analyze problems
- Produce solutions
- Validate results

## Principles

- Quality first
- Structured reasoning
- Continuous improvement
"@

    "expertise.md" = @"
# Expertise

## Technical Knowledge

List required expertise.

## Tools

List tools and technologies.

## Experience Level

Senior professional level.
"@

    "workflows.md" = @"
# Workflows

## Standard Process

1. Analyze
2. Plan
3. Execute
4. Validate
5. Document
"@

    "checklists.md" = @"
# Checklists

## Validation

[ ] Requirements understood

[ ] Solution verified

[ ] Risks analyzed

[ ] Documentation completed
"@

    "prompts.md" = @"
# Activation Prompts

## Role Activation

You are an Aegis OS specialist.

Apply professional methodology.
"@
}

foreach ($skill in $skills) {

    $path = Join-Path $SkillsRoot $skill

    New-Item -ItemType Directory -Path (Join-Path $path "examples") -Force | Out-Null

    foreach ($file in $template.Keys) {

        $filePath = Join-Path $path $file

        Set-Content `
            -Path $filePath `
            -Value $template[$file] `
            -Encoding UTF8
    }

    Set-Content `
        -Path (Join-Path $path "examples\examples.md") `
        -Value "# Examples`n`nPractical examples for this Skill." `
        -Encoding UTF8

    Write-Host "Created Skill: $skill" -ForegroundColor Green
}


Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host " Aegis OS Skills Generated "
Write-Host "==================================" -ForegroundColor Cyan
