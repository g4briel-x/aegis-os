# ==========================================
# Aegis OS - Generate Shared Knowledge Base
# ==========================================

$SharedPath = "shared"

# Création des dossiers
$folders = @(
    "$SharedPath",
    "$SharedPath/software-engineering",
    "$SharedPath/security",
    "$SharedPath/operations"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
}

# Fonction création fichier Markdown
function Create-MarkdownFile {
    param(
        [string]$Path,
        [string]$Content
    )

    Set-Content -Path $Path -Value $Content -Encoding UTF8
    Write-Host "Created: $Path" -ForegroundColor Green
}

# ==========================================
# Engineering Principles
# ==========================================

Create-MarkdownFile `
"shared/engineering-principles.md" `
@"
# Aegis OS Engineering Principles

## Purpose

Principles shared by every Aegis OS Skill.

## Core Rules

- Understand before building.
- Prefer simplicity over unnecessary complexity.
- Design for maintainability.
- Validate before delivery.
- Document important decisions.

## Engineering Mindset

Every solution must consider:

- reliability
- security
- scalability
- maintainability
- user value
"@

# ==========================================
# Quality Standards
# ==========================================

Create-MarkdownFile `
"shared/quality-standards.md" `
@"
# Aegis OS Quality Standards

## Quality Definition

A quality output is:

- correct
- understandable
- maintainable
- tested
- documented

## Validation

Every important production passes:

1. Technical review
2. Security review
3. Consistency review
4. Final validation
"@

# ==========================================
# Clean Code
# ==========================================

Create-MarkdownFile `
"shared/software-engineering/clean-code.md" `
@"
# Clean Code Principles

## Rules

- Names must express intent.
- Functions should have one responsibility.
- Avoid unnecessary complexity.
- Keep code readable.

## Objective

Code must be understood by humans first.
"@

# ==========================================
# SOLID
# ==========================================

Create-MarkdownFile `
"shared/software-engineering/solid.md" `
@"
# SOLID Principles

## S - Single Responsibility

A component has one reason to change.

## O - Open Closed

Open for extension, closed for modification.

## L - Liskov Substitution

Derived types must respect contracts.

## I - Interface Segregation

Avoid forcing unnecessary dependencies.

## D - Dependency Inversion

Depend on abstractions.
"@

# ==========================================
# Clean Architecture
# ==========================================

Create-MarkdownFile `
"shared/software-engineering/clean-architecture.md" `
@"
# Clean Architecture

## Layers

Entities

↓

Use Cases

↓

Interface Adapters

↓

Frameworks

## Goal

Separate business rules from technical details.
"@

# ==========================================
# DDD
# ==========================================

Create-MarkdownFile `
"shared/software-engineering/ddd.md" `
@"
# Domain Driven Design

## Concepts

- Domain
- Entity
- Value Object
- Aggregate
- Repository
- Domain Service

## Goal

Align software design with business reality.
"@

# ==========================================
# Testing
# ==========================================

Create-MarkdownFile `
"shared/software-engineering/testing.md" `
@"
# Software Testing

## Levels

- Unit tests
- Integration tests
- End-to-end tests

## Objective

Prevent regression and guarantee confidence.
"@

# ==========================================
# OWASP
# ==========================================

Create-MarkdownFile `
"shared/security/owasp.md" `
@"
# OWASP Security Principles

## Security Rules

- Validate inputs.
- Protect sensitive data.
- Apply least privilege.
- Manage authentication securely.

## Objective

Build secure systems by default.
"@

# ==========================================
# Observability
# ==========================================

Create-MarkdownFile `
"shared/operations/observability.md" `
@"
# Observability Principles

## Three Pillars

- Logs
- Metrics
- Traces

## Objective

Understand system behavior in production.
"@

# ==========================================
# Performance
# ==========================================

Create-MarkdownFile `
"shared/performance.md" `
@"
# Performance Engineering

## Principles

Measure before optimizing.

Consider:

- latency
- throughput
- resource usage
- scalability
"@

# ==========================================
# Glossary
# ==========================================

Create-MarkdownFile `
"shared/glossary.md" `
@"
# Aegis OS Glossary

Common engineering terminology.

- Skill: specialized expert module.
- Core: fundamental operating rules.
- Playbook: operational procedure.
- Pattern: reusable solution.
"@


Write-Host ""
Write-Host "==================================" -ForegroundColor Cyan
Write-Host " Shared knowledge base generated "
Write-Host "==================================" -ForegroundColor Cyan