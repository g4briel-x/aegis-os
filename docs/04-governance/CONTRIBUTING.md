# Aegis OS — Contributing Guide

Version: 0.1  
Status: Governance Document

---

# 1. Introduction

This document defines the rules and processes for contributing to Aegis OS.

Contributions can include:

- documentation;
- Skills;
- Playbooks;
- Patterns;
- Templates;
- Core components;
- Tools;
- Improvements.

The objective is to maintain a coherent, high-quality ecosystem.

---

# 2. Contribution Philosophy

Aegis OS follows this principle:

> Every contribution must increase the intelligence, reliability or usability of the system.

A contribution should not only add content.

It should add structured value.

---

# 3. Contribution Types

## Documentation Contributions

Examples:

- new specifications;
- improvements;
- corrections;
- examples.

---

## Skill Contributions

Examples:

- new expert modules;
- Skill improvements;
- methodology updates.

---

## Architecture Contributions

Examples:

- core improvements;
- new components;
- integration mechanisms.

---

## Knowledge Contributions

Examples:

- patterns;
- references;
- best practices.

---

# 4. Before Contributing

Before creating new content:

Check:

- Does this capability already exist?
- Is there an existing component that can be improved?
- Does this follow Aegis OS architecture?

Avoid duplication.

---

# 5. Contribution Workflow

The standard workflow:
Identify Need

  ↓

Create Proposal

  ↓

Design Solution

  ↓

Implement

  ↓

Review

  ↓

Validate

  ↓

Merge


---

# 6. Proposal Requirements

Significant contributions should include:

```markdown
# Proposal

## Objective

What problem is solved?

## Motivation

Why is this needed?

## Scope

What is included?

## Impact

What components are affected?

## Validation

How will success be measured?
7. Documentation Standards

All documents must:

use Markdown format;
have clear titles;
define purpose;
explain scope;
include examples when useful;
follow naming conventions.
8. Code Standards

When code is added:

Requirements:

readable;
documented;
tested;
maintainable.

Prefer:

simplicity;
explicit behavior;
modular design.
9. Skill Contribution Rules

New Skills must include:

README.md
MANIFEST.md
identity.md
mission.md
expertise.md
reasoning.md
methodologies.md
decision-framework.md
quality-gates.md
examples/

A Skill without validation cannot become stable.

10. Review Process

Every important contribution should be reviewed for:

Architecture

Does it fit the system?

Quality

Does it meet standards?

Consistency

Does it follow conventions?

Maintainability

Can it evolve?

11. Commit Standards

Commits should be:

focused;
descriptive;
atomic.

Recommended format:

type: description

Examples:

docs: add skill specification

feat: create security engineer skill

fix: correct architecture documentation
12. Version Control

All changes must be:

tracked;
documented;
reversible.

Important changes require version updates.

13. Contribution Principles

Contributors should prioritize:

Quality over quantity

A smaller high-quality contribution is better.

Structure over improvisation

Follow existing architecture.

Reusability over duplication

Create components that can serve multiple contexts.

Long-term value over temporary solutions

Build for evolution.

14. Final Principle

Contributing to Aegis OS means improving a shared intelligence system, not simply adding files.