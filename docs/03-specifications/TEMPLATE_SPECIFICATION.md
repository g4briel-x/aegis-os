# Aegis OS — Template Specification

Version: 0.1  
Status: Core Specification Document

---

# 1. Introduction

A Template is a reusable structure designed to standardize the creation of documents, deliverables and outputs inside Aegis OS.

Templates ensure:

- consistency;
- efficiency;
- quality;
- faster production.

A Template defines the structure.

It does not define expertise or methodology.

---

# 2. Definition

A Template represents:

> A predefined document or artifact structure that guides the creation of consistent professional outputs.

Examples:

- Architecture Document Template
- Technical Specification Template
- Product Requirement Document Template
- Security Assessment Template

---

# 3. Purpose

Templates exist to:

- reduce repetitive work;
- enforce standards;
- improve readability;
- accelerate delivery;
- preserve organizational knowledge.

---

# 4. Relationship With Other Components

## Skills

Skills define expertise.

Templates define output structure.

Example:
Software Architect Skill

    +

Architecture Document Template

    ↓

Professional Architecture Document


---

## Playbooks

Playbooks define processes.

Templates define artifacts produced by processes.

Example:


Architecture Review Playbook

    +

Review Report Template

    ↓

Architecture Review Report


---

# 5. Template Structure

Every Template must follow:


template-name/

├── README.md
├── MANIFEST.md
├── structure.md
├── instructions.md
├── validation.md
├── examples/
└── references/


---

# 6. Required Components

## README.md

Contains:

- template purpose;
- usage scenarios;
- expected outputs.

---

## MANIFEST.md

Contains metadata.

Example:

```yaml
template:
  name: technical-design-document
  version: 1.0.0
  category: engineering
  maturity: stable
structure.md

Defines:

document sections;
hierarchy;
required fields.

Example:

# Introduction

# Requirements

# Design

# Implementation

# Validation

# Conclusion
instructions.md

Explains:

how to use the template;
expected content;
writing guidelines.
validation.md

Defines quality checks.

Example:

[ ] All sections completed

[ ] Information validated

[ ] Assumptions identified

[ ] References included
7. Template Categories
Engineering Templates

Examples:

Technical Specification
API Documentation
Architecture Decision Record
Product Templates

Examples:

Product Requirement Document
User Story
Roadmap
Management Templates

Examples:

Project Plan
Status Report
Risk Assessment
Research Templates

Examples:

Analysis Report
Investigation Document
8. Template Design Principles
Clarity

The structure must be understandable.

Completeness

Required information must be defined.

Flexibility

The template must support variations.

Consistency

All templates should follow common conventions.

9. Template Lifecycle
Creation

    ↓

Review

    ↓

Validation

    ↓

Publication

    ↓

Usage

    ↓

Improvement
10. Quality Requirements

A Template must:

have a defined purpose;
identify its users;
provide instructions;
include validation criteria;
contain examples.
11. Anti-Patterns
Empty Structure

Problem:

Only headings without guidance.

Excessive Complexity

Problem:

Template becomes difficult to use.

Missing Validation

Problem:

Quality cannot be measured.

12. Final Principle

A Template is the standardized interface between expert intelligence and professional deliverables.