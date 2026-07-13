## FILE: `patterns/INDEX.md`

# Aegis OS — Patterns Index

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This index lists the reusable Patterns available in Aegis OS.

A Pattern is a reusable decision model for solving a recurring product, engineering, architecture, security, operations, design or business problem.

Patterns are different from Playbooks:

```text
Pattern = reusable solution model and trade-offs
Playbook = step-by-step execution procedure
Skill = expert capability
Template = reusable output format
```

---

# 2. Pattern Framework

The Patterns Framework defines how reusable Patterns are created, structured, reviewed and maintained.

```text
patterns/_framework/README.md
patterns/_framework/PATTERN_SPECIFICATION.md
patterns/_framework/PATTERN_DIRECTORY_STRUCTURE.md
patterns/_framework/PATTERN_METADATA_SCHEMA.md
patterns/_framework/PATTERN_AUTHORING_GUIDE.md
patterns/_framework/PATTERN_QUALITY_GATE.md
patterns/_framework/PATTERN_REVIEW_CHECKLIST.md
patterns/_framework/PATTERN_VERSIONING.md
patterns/_framework/PATTERN_TEMPLATE.md
```

Purpose:

```text
Provides standards for authoring reusable solution patterns with context, trade-offs, risks, examples and validation checklists.
```

---

# 3. Architecture Patterns

## 3.1 SaaS Modular Monolith

```text
patterns/architecture/saas-modular-monolith
```

Purpose:

```text
Defines how to build early and mid-stage SaaS products as one deployable application with strong internal module boundaries.
```

Recommended for:

```text
MVPs
early SaaS products
small teams
evolving domains
controlled operational complexity
```

---

# 4. Engineering Patterns

## 4.1 API Error Handling

```text
patterns/engineering/api-error-handling
```

Purpose:

```text
Defines predictable, safe and actionable API error responses with stable error codes, safe messages, request ids and validation details.
```

## 4.2 Background Job Processing

```text
patterns/engineering/background-job-processing
```

Purpose:

```text
Defines safe asynchronous processing with job payloads, tenant context, retries, idempotency, dead-letter handling and observability.
```

## 4.3 Database Migration Safety

```text
patterns/engineering/database-migration-safety
```

Purpose:

```text
Defines safe production database migration practices with compatibility, validation, rollback, recovery and monitoring.
```

## 4.4 API Versioning Strategy

```text
patterns/engineering/api-versioning-strategy
```

Purpose:

```text
Defines how SaaS APIs evolve without breaking clients through versioning, compatibility rules, deprecation, migration guides and contract tests.
```

---

# 5. Security Patterns

## 5.1 RBAC Permission Model

```text
patterns/security/rbac-permission-model
```

Purpose:

```text
Defines roles, permissions, resources, scopes, policies, enforcement points and permission tests for SaaS access control.
```

## 5.2 Tenant Data Isolation

```text
patterns/security/tenant-data-isolation
```

Purpose:

```text
Defines tenant scoping, ownership rules, query constraints, file access and cross-tenant denial testing for multi-tenant SaaS.
```

## 5.3 Audit Logging Traceability

```text
patterns/security/audit-logging-traceability
```

Purpose:

```text
Defines structured audit events for sensitive actions, admin activity, file access, billing changes, permission changes and support access.
```

---

# 6. Product Patterns

## 6.1 SaaS MVP Scope

```text
patterns/product/saas-mvp-scope
```

Purpose:

```text
Defines how to scope a SaaS MVP around one segment, one painful use case, one core workflow and one measurable activation outcome.
```

---

# 7. Design Patterns

## 7.1 SaaS Onboarding Flow

```text
patterns/design/saas-onboarding-flow
```

Purpose:

```text
Defines how to guide new users from signup to first meaningful value through setup, first action, activation and progress feedback.
```

---

# 8. Operations Patterns

## 8.1 Feature Flag Rollout

```text
patterns/operations/feature-flag-rollout
```

Purpose:

```text
Defines safe staged feature activation with targeting, monitoring, rollback, rollout stages and cleanup.
```

## 8.2 Production Observability Baseline

```text
patterns/operations/production-observability-baseline
```

Purpose:

```text
Defines the minimum logs, metrics, dashboards, alerts, request correlation and health checks needed to operate SaaS safely in production.
```

## 8.3 Incident Severity Model

```text
patterns/operations/incident-severity-model
```

Purpose:

```text
Defines incident severity levels, impact criteria, response expectations, escalation rules, communication policy and postmortem requirements.
```

---

# 9. Business Patterns

## 9.1 Billing Subscription Model

```text
patterns/business/billing-subscription-model
```

Purpose:

```text
Defines SaaS plans, prices, subscriptions, entitlements, trials, invoices, upgrades, downgrades, cancellations and failed payment behavior.
```

---

# 10. Standard Pattern Structure

Every premium Pattern should follow this structure:

```text
README.md
PATTERN.md
metadata.yaml
context.md
solution.md
trade-offs.md
checklists.md
examples/examples.md
```

---

# 11. Pattern Completion Status

```yaml
patterns:
  framework: complete

  architecture:
    saas_modular_monolith: complete

  engineering:
    api_error_handling: complete
    background_job_processing: complete
    database_migration_safety: complete
    api_versioning_strategy: complete

  security:
    rbac_permission_model: complete
    tenant_data_isolation: complete
    audit_logging_traceability: complete

  product:
    saas_mvp_scope: complete

  design:
    saas_onboarding_flow: complete

  operations:
    feature_flag_rollout: complete
    production_observability_baseline: complete
    incident_severity_model: complete

  business:
    billing_subscription_model: complete
```

---

# 12. Recommended Usage Order

For a SaaS project, use Patterns in this order:

```text
1. product/saas-mvp-scope
2. architecture/saas-modular-monolith
3. security/rbac-permission-model
4. security/tenant-data-isolation
5. design/saas-onboarding-flow
6. engineering/api-error-handling
7. engineering/api-versioning-strategy
8. engineering/background-job-processing
9. engineering/database-migration-safety
10. business/billing-subscription-model
11. operations/feature-flag-rollout
12. operations/production-observability-baseline
13. operations/incident-severity-model
14. security/audit-logging-traceability
```

---

# 13. Governance Notes

A Pattern should be reviewed when:

```text
the recommended solution changes
a major risk is discovered
a better Pattern replaces it
the technology context changes
a security incident reveals a gap
a Playbook depends on the Pattern
```

---

# 14. Final Principle

> Patterns make expert decisions reusable while preserving the context and trade-offs behind those decisions.