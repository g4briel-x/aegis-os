## FILE: `templates/engineering/data-model-template/examples/examples.md`

# Data Model Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Project Readiness Data Model

## Model Name

```text
Project Readiness Data Model
```

## Business Context

```text
The SaaS helps independent producers prepare film, series or documentary projects for financing review.
```

## Main Entities

```text
Workspace
User
Project
ProjectDocument
ReadinessChecklist
ReadinessReview
AuditEvent
```

## Project Entity

```text
Table: projects
Primary key: id
Tenant key: workspace_id
Owner: workspace
Lifecycle states: draft, submitted, reviewed, archived
```

## Project Fields

```text
id | uuid | required | generated | Project identifier | no
workspace_id | uuid | required | none | Tenant boundary | no
title | text | required | none | Project title | no
project_type | text | required | none | film, series or documentary | no
status | text | required | draft | Project lifecycle status | no
created_by | uuid | required | none | Creator user id | no
submitted_at | timestamp | optional | null | Submission time | no
```

## Tenant Boundary

```text
Every project belongs to one workspace_id. Users can read or modify projects only inside their active workspace.
```

## Permission Rules

```text
create: project.create
read: project.read
update: project.update
submit: project.submit
archive: project.archive
```

## Audit Events

```text
project.created
project.submitted
project.reviewed
project.archived
```

---

# 2. Example — Relationship Model

```text
Workspace has many Projects.
Project has many ProjectDocuments.
Project has one active ReadinessChecklist.
Project can have many ReadinessReviews.
User creates Project.
```

---

# 3. Example — Migration Note

```text
If readiness_score is added later, add it as nullable first, backfill in batches, validate submitted projects, then enforce requirement only in a later release if needed.
```

---

# 4. Final Principle

> Examples show that a data model must describe domain meaning, technical storage and security boundaries together.
