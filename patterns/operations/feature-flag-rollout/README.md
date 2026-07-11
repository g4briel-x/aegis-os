## FILE: `patterns/operations/feature-flag-rollout/README.md`

# Feature Flag Rollout Pattern

Version: 0.1.0  
Status: Draft  
Domain: Operations  
Category: Release Management

---

# 1. Purpose

The Feature Flag Rollout Pattern defines a reusable model for releasing SaaS features gradually, safely and observably.

It helps teams separate deployment from activation, reduce launch risk, test with limited users, monitor impact and roll back behavior without redeploying code.

---

# 2. Problem

SaaS teams often deploy features directly to all users.

This creates risks:

```text
large blast radius
difficult rollback
no controlled beta
no progressive validation
customer impact if feature fails
harder production debugging
```

---

# 3. Recommended Solution

Use feature flags to control feature activation.

A safe rollout should define:

```text
flag name
owner
target audience
default state
rollout percentage
activation conditions
monitoring signals
rollback trigger
expiration date
cleanup task
```

---

# 4. Recommended When

Use this Pattern when:

- a feature has meaningful user impact;
- the feature affects revenue, permissions, data or onboarding;
- gradual rollout is safer than full release;
- beta users should test first;
- rollback must be fast;
- A/B testing or experimentation is needed;
- production behavior needs controlled activation.

---

# 5. Avoid When

Avoid feature flags when:

- the change is trivial and low-risk;
- the flag will never be removed;
- the team has no ownership for cleanup;
- the flag controls security-critical behavior in an unsafe way;
- flag complexity becomes harder than the release itself.

---

# 6. Related Assets

```text
Related skills:
infrastructure.devops-engineer
engineering.senior-developer
engineering.software-architect
security.security-engineer
product.product-manager-saas

Related playbooks:
operations.prepare-release
infrastructure.deploy-saas-application
operations.monitor-saas-production
product.prepare-saas-launch
engineering.write-test-plan
```

---

# 7. Final Principle

> Feature flags should reduce release risk, not create permanent hidden complexity.
