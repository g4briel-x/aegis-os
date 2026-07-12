## FILE: `patterns/design/saas-onboarding-flow/README.md`

# SaaS Onboarding Flow Pattern

Version: 0.1.0  
Status: Draft  
Domain: Design  
Category: SaaS UX

---

# 1. Purpose

The SaaS Onboarding Flow Pattern defines a reusable model for guiding new users from signup to first meaningful value.

It helps product, UX and engineering teams design onboarding that reduces confusion, captures essential context, drives activation and avoids unnecessary friction.

---

# 2. Problem

SaaS products often lose users before they experience value.

Common failures:

```text
too many questions before value
unclear first action
empty dashboards
no activation moment
no role-specific guidance
setup feels disconnected from the user's goal
users do not know what to do next
success is not measured
```

---

# 3. Recommended Solution

Design onboarding around the activation path.

A good onboarding flow should define:

```text
target user
signup path
context questions
first workspace or project setup
first task
activation moment
guidance system
progress indicators
fallback support
success metrics
```

---

# 4. Recommended When

Use this Pattern when:

- a SaaS product has new users;
- activation is weak;
- users abandon after signup;
- the first workflow is unclear;
- the product has role-based setup;
- onboarding depends on project, workspace or team creation;
- the MVP needs measurable activation.

---

# 5. Avoid When

Avoid overbuilding onboarding when:

- the product is a short-lived prototype;
- users are manually onboarded by the team;
- the first workflow is already obvious;
- onboarding screens delay value without useful setup;
- the product needs discovery before UX automation.

Even then, the first meaningful user action should be clear.

---

# 6. Related Assets

```text
Related skills:
design.ux-ui-designer-saas
product.product-manager-saas
product.business-analyst
engineering.senior-developer
management.technical-project-manager

Related playbooks:
design.design-saas-ux-flow
product.define-saas-mvp
product.create-prd
product.prepare-saas-launch
business.create-go-to-market-plan

Related patterns:
product.saas-mvp-scope
operations.feature-flag-rollout
operations.production-observability-baseline
```

---

# 7. Final Principle

> SaaS onboarding is successful when the user reaches value faster than they reach confusion.
