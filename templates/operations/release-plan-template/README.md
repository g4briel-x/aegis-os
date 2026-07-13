## FILE: `templates/operations/release-plan-template/README.md`

# Release Plan Template

Version: 0.1.0  
Status: Draft  
Domain: Operations  
Category: Release Management

---

# 1. Purpose

The Release Plan Template provides a reusable structure for planning, approving, deploying, validating and monitoring a SaaS release.

It helps product, engineering, QA, security, operations and support teams align on release scope, risk, dependencies, rollout strategy, validation, rollback, communication and post-release monitoring.

---

# 2. When to Use

Use this Template when:

```text
a production release is being prepared
a feature is customer-facing
a database migration is included
a feature flag rollout is required
security-sensitive changes are included
support must prepare customer-facing notes
rollback or recovery must be defined
release approval must be recorded
```

---

# 3. Output

This Template produces:

```text
Release Plan Document
```

---

# 4. Related Assets

```text
Related skills:
management.technical-project-manager
infrastructure.devops-engineer
engineering.senior-developer
engineering.software-architect
security.security-engineer
product.product-manager-saas

Related playbooks:
operations.prepare-release
infrastructure.deploy-saas-application
engineering.write-test-plan
engineering.review-pull-request
operations.monitor-saas-production
operations.create-runbook

Related patterns:
operations.feature-flag-rollout
operations.production-observability-baseline
engineering.database-migration-safety
operations.incident-severity-model
security.audit-logging-traceability
```

---

# 5. Final Principle

> A release plan is useful when it makes deployment, validation and recovery predictable before production changes happen.
