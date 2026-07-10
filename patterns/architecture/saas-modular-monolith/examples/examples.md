## FILE: `patterns/architecture/saas-modular-monolith/examples/examples.md`

# SaaS Modular Monolith — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Context

A platform helps creators prepare film, series and documentary projects for financing.

## Recommended Modules

```text
identity
organizations
projects
documents
reviews
investors
billing
notifications
audit
admin
```

## Application

The `projects` module owns:

- project creation;
- project lifecycle;
- submission workflow;
- ownership rules;
- project status transitions.

The `documents` module owns:

- uploaded file metadata;
- document validation;
- document access rules.

The `reviews` module owns:

- reviewer assignments;
- review comments;
- approval decisions.

---

# 2. Example — B2B Workspace SaaS

## Context

A team workspace SaaS supports organizations, members, projects and billing.

## Recommended Modules

```text
identity
workspaces
memberships
projects
tasks
billing
notifications
audit
```

## Application

Keep workspace membership rules inside the `memberships` module and avoid scattering role checks across unrelated modules.

---

# 3. Example — AI SaaS Tool

## Context

A SaaS product uses AI calls to generate reports.

## Recommended Modules

```text
identity
workspaces
documents
ai-jobs
reports
billing
usage
audit
```

## Application

The `ai-jobs` module owns job state and provider calls. The `usage` module tracks cost and limits.

---

# 4. Example — Future Extraction

A `billing` module may later become a service when:

- payment flows are complex;
- billing has independent compliance needs;
- usage metering creates scaling pressure;
- a dedicated team owns revenue infrastructure.

Until then, it remains an internal module with clear boundaries.

---

# 5. Final Principle

> Examples show that the modular monolith adapts to SaaS domains while preserving operational simplicity.
