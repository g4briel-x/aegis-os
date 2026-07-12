## FILE: `patterns/engineering/database-migration-safety/README.md`

# Database Migration Safety Pattern

Version: 0.1.0  
Status: Draft  
Domain: Engineering  
Category: Database Operations

---

# 1. Purpose

The Database Migration Safety Pattern defines a reusable model for designing, reviewing, deploying and validating database migrations safely in SaaS applications.

It helps teams reduce production risk when changing schemas, indexes, constraints, seed data, tenant data, permissions, billing data or other persistent records.

---

# 2. Problem

Database migrations can break production even when application code is correct.

Common failures:

```text
destructive migration without backup
long-running migration locks production tables
missing rollback plan
application and schema versions are incompatible
data backfill fails halfway
migration is not tested on realistic data volume
tenant data is modified incorrectly
indexes are created unsafely
constraints are added before data is cleaned
```

---

# 3. Recommended Solution

Treat every production migration as a controlled change.

A safe migration should define:

```text
migration purpose
risk level
schema change
data change
backward compatibility
deployment order
backup requirement
rollback or recovery path
validation queries
monitoring signals
owner and approval
```

---

# 4. Recommended When

Use this Pattern when:

- a production database schema changes;
- data backfill or correction is needed;
- indexes or constraints are added;
- tenant-scoped data is modified;
- billing, permissions or audit tables change;
- release safety matters;
- rollback and recovery must be planned.

---

# 5. Avoid When

Avoid overloading this Pattern for:

- local-only experimental changes;
- disposable test databases;
- generated migrations that will never reach production;
- one-off analysis queries with no persistent change.

Even then, destructive SQL should still be reviewed carefully.

---

# 6. Related Assets

```text
Related skills:
engineering.database-engineer
engineering.software-architect
engineering.senior-developer
infrastructure.devops-engineer
security.security-engineer

Related playbooks:
engineering.design-saas-data-model
operations.prepare-release
infrastructure.deploy-saas-application
engineering.write-test-plan
engineering.review-pull-request
operations.create-runbook

Related patterns:
security.tenant-data-isolation
operations.production-observability-baseline
engineering.background-job-processing
```

---

# 7. Final Principle

> A database migration is safe when failure modes are understood before production execution.
