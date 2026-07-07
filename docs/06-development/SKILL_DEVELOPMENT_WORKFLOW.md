# Aegis OS — 06-development Bundle

Ce fichier regroupe les documents du dossier `docs/06-development/`.

---

## FILE: `docs/06-development/SKILL_DEVELOPMENT_WORKFLOW.md`

# Aegis OS — Skill Development Workflow

Version: 0.1  
Status: Development Workflow Document

---

# 1. Introduction

This document defines the standard workflow for designing, building, validating and evolving a Skill inside Aegis OS.

A Skill is a structured expert capability. It must be engineered, not improvised.

---

# 2. Workflow Philosophy

Aegis OS follows this principle:

> A Skill must be developed like a professional software component: scoped, documented, reviewed, validated and versioned.

The workflow ensures that each Skill is:

- useful;
- coherent;
- maintainable;
- reusable;
- professionally structured.

---

# 3. Skill Development Lifecycle

```text
Need Identification

    ↓

Skill Proposal

    ↓

Skill Design

    ↓

Content Production

    ↓

Validation

    ↓

Publication

    ↓

Continuous Improvement

4. Phase 1 — Need Identification
Objective

Identify why the Skill is needed.

Questions:

What domain does it cover?
What problems does it solve?
Why is an existing Skill insufficient?
What value will it add to Aegis OS?

Required output:

problem statement;
expected users;
target domain;
success criteria.
5. Phase 2 — Skill Proposal
Objective

Define the Skill before writing content.

Proposal should include:

# Skill Proposal

## Name

## Domain

## Mission

## Scope

## Expected Deliverables

## Dependencies

## Risks

## Validation Plan
6. Phase 3 — Skill Design
Objective

Define the internal architecture of the Skill.

Each Skill should follow the official specification:

skill-name/

├── README.md
├── MANIFEST.md
├── identity.md
├── mission.md
├── expertise.md
├── reasoning.md
├── methodologies.md
├── decision-framework.md
├── quality-gates.md
├── anti-patterns.md
├── collaboration.md
├── deliverables.md
├── prompts.md
├── playbooks/
├── checklists/
├── examples/
└── references/
7. Phase 4 — Content Production
Objective

Create the actual expert content.

Content must define:

professional identity;
expert mission;
methods;
decision logic;
quality rules;
collaboration model;
expected outputs.

Production principles:

no placeholders;
no vague generic text;
professional tone;
actionable guidance.
8. Phase 5 — Validation
Objective

Verify the Skill before publication.

Validation checks:

[ ] Structure complete
[ ] Mission clearly defined
[ ] Expertise documented
[ ] Reasoning model documented
[ ] Quality gates included
[ ] Anti-patterns documented
[ ] Examples provided
[ ] Dependencies declared

Validation levels:

structural review;
technical review;
architectural review;
ecosystem review.
9. Phase 6 — Publication
Objective

Make the Skill available in the ecosystem.

Publication requires:

metadata completed;
version defined;
changelog entry;
references updated.

Example metadata:

skill:
  name: software-architect
  version: 1.0.0
  maturity: stable
  category: engineering
10. Phase 7 — Continuous Improvement
Objective

Keep the Skill relevant over time.

Improvement triggers:

user feedback;
new technologies;
quality review;
ecosystem evolution;
repeated execution issues.

Improvement loop:

Usage

 ↓

Observation

 ↓

Feedback

 ↓

Correction / Improvement

 ↓

Validation

 ↓

New Version
11. Skill Quality Rules

A Skill must be:

Focused

One clear professional role.

Senior

Reflect experienced-level thinking.

Explainable

Reasoning must be understandable.

Reusable

Usable across multiple scenarios.

Maintainable

Easy to update over time.

12. Common Failure Modes

Avoid:

generic descriptions without operational value;
duplicated domain coverage;
unclear scope;
undocumented dependencies;
no validation process;
no examples.
13. Skill Development Checklist
[ ] Need identified
[ ] Proposal written
[ ] Structure created
[ ] Content produced
[ ] Validation completed
[ ] Metadata defined
[ ] Version assigned
[ ] Publication completed
14. Final Principle

A Skill becomes valuable only when it combines expertise, structure, validation and long-term maintainability.