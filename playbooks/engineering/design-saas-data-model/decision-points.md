## FILE: `playbooks/engineering/design-saas-data-model/decision-points.md`

# Design SaaS Data Model — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is This a Separate Entity?

```yaml
decision_point:
  question: Should this concept become its own entity/table?
  options:
    - yes
    - no
    - maybe
  criteria:
    - has independent lifecycle
    - has relationships
    - has permissions
    - needs querying or reporting
    - has many fields
  recommended_action:
    yes: model as entity.
    no: model as field or embedded value.
    maybe: document uncertainty and review query needs.
  fallback: start simple but avoid blocking future extraction.
```

---

# 2. Decision Point — Is Multi-Tenancy Required?

```yaml
decision_point:
  question: Does this data belong inside a tenant, workspace or organization boundary?
  options:
    - yes
    - no
    - unclear
  criteria:
    - B2B customer separation
    - organization accounts
    - workspace membership
    - customer-specific records
    - role-based access
  recommended_action:
    yes: add tenant or workspace boundary.
    no: document global data behavior.
    unclear: treat as tenant-scoped until product confirms otherwise.
  fallback: involve Software Architect and Security Engineer Skills.
```

---

# 3. Decision Point — Should the Relationship Be Many-to-Many?

```yaml
decision_point:
  question: Does the relationship require many records on both sides?
  options:
    - yes
    - no
    - unclear
  criteria:
    - multiple users per project
    - multiple tags per item
    - multiple roles per user
    - history or metadata on relationship
  recommended_action:
    yes: create join entity if needed.
    no: use simpler foreign key.
    unclear: review actual workflow and future needs.
  fallback: choose the simplest relationship that supports current MVP.
```

---

# 4. Decision Point — Does Data Require Audit History?

```yaml
decision_point:
  question: Should changes to this data be audited or versioned?
  options:
    - yes
    - no
    - unclear
  criteria:
    - sensitive data
    - financial data
    - permission changes
    - approval workflow
    - compliance requirement
    - dispute risk
  recommended_action:
    yes: add audit event or history model.
    no: document no audit requirement.
    unclear: audit critical changes until reviewed.
  fallback: record created_at, updated_at and actor fields at minimum.
```

---

# 5. Decision Point — Is Deletion Soft or Hard?

```yaml
decision_point:
  question: Should records be soft-deleted, archived or permanently deleted?
  options:
    - soft_delete
    - hard_delete
    - archive
    - unclear
  criteria:
    - recovery need
    - audit need
    - legal retention
    - user privacy
    - relationship integrity
  recommended_action:
    soft_delete: use when recovery and audit matter.
    hard_delete: use only when safe and compliant.
    archive: use when record should remain but become inactive.
    unclear: document retention question before implementation.
  fallback: avoid destructive deletion for business-critical data.
```

---

# 6. Final Principle

> Data model decisions should be explicit because hidden assumptions become expensive migrations later.