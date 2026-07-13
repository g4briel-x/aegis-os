## FILE: `templates/product/prd-template/examples/examples.md`

# PRD Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Product / Feature Name

```text
Project Readiness Review
```

## Summary

```text
This feature helps independent producers understand whether their film, series or documentary project package is ready for financing discussions.
```

## Problem Statement

```text
Independent producers often do not know which materials are missing before approaching financiers. This creates delays, poor investor conversations and repeated manual review.
```

## Primary User

```text
Independent film producer
```

## Goals

```text
Allow creators to submit one project package for readiness review.
Show missing materials clearly.
Help creators understand next steps before financing outreach.
```

## Non-Goals

```text
Automated investor matching.
Full financing marketplace.
AI-generated pitch deck creation.
```

## Functional Requirements

```text
FR-001: The system must allow a creator to create a project.
FR-002: The system must show required project materials.
FR-003: The system must allow document upload.
FR-004: The system must prevent submission when required materials are missing.
FR-005: The system must show readiness feedback after review.
```

## Acceptance Criteria

```text
Given a project is missing required documents
When the creator attempts to submit the project
Then the system blocks submission and displays the missing documents.
```

## Success Metric

```text
At least 10 beta creators submit a complete project package during the pilot.
```

---

# 2. Example — SaaS Onboarding Feature

## Feature Name

```text
Guided First Project Setup
```

## Goal

```text
Increase the percentage of new users who create their first project within 10 minutes of signup.
```

## Acceptance Criteria

```text
Given a new user completes signup
When they reach the empty dashboard
Then the primary action prompts them to create the first project.
```

---

# 3. Example — API Feature

## Feature Name

```text
Project Submission API
```

## API Requirement

```text
POST /api/v1/projects/:project_id/submit
```

## Error Requirement

```text
If required documents are missing, the API returns validation_failed with field-level details.
```

---

# 4. Final Principle

> Examples show that PRDs should connect user problem, product scope and implementation readiness.