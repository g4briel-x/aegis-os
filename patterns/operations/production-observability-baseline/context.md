## FILE: `patterns/operations/production-observability-baseline/context.md`

# Production Observability Baseline — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS applications that are preparing for or already running in production.

Typical contexts:

```text
first production launch
private beta with real users
paid pilot
public SaaS release
enterprise customer onboarding
reliability hardening
post-incident improvement
```

---

# 2. Product Context

Use this Pattern when the product has workflows that must not silently fail.

Examples:

- signup;
- login;
- project creation;
- document upload;
- payment;
- submission;
- review;
- notification;
- export.

---

# 3. Technical Context

This Pattern applies when the system includes:

```text
frontend
backend API
database
background jobs
file storage
third-party APIs
authentication provider
payment provider
email or notification provider
```

---

# 4. Operational Context

The team needs to know:

- whether production is healthy;
- whether the latest release caused problems;
- whether customers are blocked;
- whether jobs are processing;
- whether dependencies are failing;
- whether recovery worked.

---

# 5. Warning Signs

Observability is weak when:

- customer reports are the first signal of failure;
- logs are plain text and hard to search;
- request ids are missing;
- dashboards do not show customer impact;
- alerts fire too often or not at all;
- background jobs fail silently;
- no one knows which metrics matter.

---

# 6. Final Principle

> Observability context should include systems, users, workflows and operators.
