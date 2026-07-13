## FILE: `templates/engineering/data-model-template/README.md`

# Data Model Template

Version: 0.1.0  
Status: Draft  
Domain: Engineering  
Category: Data Architecture

---

# 1. Purpose

The Data Model Template provides a reusable structure for documenting SaaS data entities, relationships, fields, ownership, tenant boundaries, constraints, lifecycle states, audit requirements and migration considerations.

It helps product, engineering, database, security and architecture teams align before implementing database tables, API models or domain objects.

---

# 2. When to Use

Use this Template when:

```text
a new SaaS domain model is being designed
a database schema must be created or changed
a PRD introduces new entities
an API contract needs persistent data
tenant ownership must be clarified
permissions depend on resource relationships
migration safety must be reviewed
audit or retention rules matter
```

---

# 3. Output

This Template produces:

```text
Data Model Document
```

---

# 4. Related Assets

```text
Related skills:
engineering.database-engineer
engineering.software-architect
engineering.senior-developer
security.security-engineer
product.business-analyst

Related playbooks:
engineering.design-saas-data-model
engineering.create-api-contract
security.design-auth-rbac
engineering.write-test-plan
operations.prepare-release

Related patterns:
security.tenant-data-isolation
security.rbac-permission-model
security.audit-logging-traceability
engineering.database-migration-safety
architecture.saas-modular-monolith
```

---

# 5. Final Principle

> A data model is useful when it makes ownership, relationships and constraints explicit before code and migrations are written.
