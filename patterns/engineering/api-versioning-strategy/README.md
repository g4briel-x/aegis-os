## FILE: `patterns/engineering/api-versioning-strategy/README.md`

# API Versioning Strategy Pattern

Version: 0.1.0  
Status: Draft  
Domain: Engineering  
Category: API Design

---

# 1. Purpose

The API Versioning Strategy Pattern defines a reusable model for evolving SaaS APIs without breaking clients unexpectedly.

It helps teams manage backward compatibility, breaking changes, deprecation, client migration, documentation, testing and release communication.

---

# 2. Problem

SaaS APIs evolve as products grow.

Without a versioning strategy, teams create risks such as:

```text
breaking existing clients
undocumented behavior changes
frontend and backend mismatch
mobile clients stuck on old contracts
third-party integrations failing silently
multiple incompatible endpoint behaviors
unclear deprecation timelines
```

---

# 3. Recommended Solution

Define explicit API versioning rules.

A good API versioning strategy should define:

```text
versioning method
backward compatibility rules
breaking change policy
deprecation process
migration window
client communication
contract tests
documentation update process
sunset policy
```

---

# 4. Recommended When

Use this Pattern when:

- the SaaS product exposes APIs;
- external clients or integrations exist;
- frontend and backend are deployed separately;
- API contracts evolve frequently;
- breaking changes are possible;
- mobile clients or third-party clients must be supported;
- enterprise customers depend on stable APIs.

---

# 5. Avoid When

Avoid complex versioning when:

- the API is internal and deployed atomically with all clients;
- no external client depends on stability;
- the product is still a disposable prototype;
- versioning creates more complexity than the API itself.

Even then, breaking changes should be reviewed explicitly.

---

# 6. Related Assets

```text
Related skills:
engineering.software-architect
engineering.senior-developer
engineering.senior-debugger
security.security-engineer
product.product-manager-saas

Related playbooks:
engineering.create-api-contract
engineering.write-test-plan
engineering.review-pull-request
operations.prepare-release
product.prepare-saas-launch

Related patterns:
engineering.api-error-handling
engineering.database-migration-safety
operations.feature-flag-rollout
operations.production-observability-baseline
```

---

# 7. Final Principle

> API versioning should protect client trust while allowing the product to evolve.
