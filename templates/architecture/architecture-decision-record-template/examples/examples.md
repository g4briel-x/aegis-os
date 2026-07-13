## FILE: `templates/architecture/architecture-decision-record-template/examples/examples.md`

# Architecture Decision Record Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Use Modular Monolith for SaaS MVP

## ADR Title

```text
Use Modular Monolith for SaaS MVP
```

## Context

```text
The SaaS MVP must be delivered quickly by a small team. The product domain is still evolving, but the system needs clear boundaries for project management, billing, users, documents and readiness reviews.
```

## Problem

```text
The team needs an architecture that supports fast delivery without creating unnecessary distributed-system complexity.
```

## Options Considered

```text
Option 1: Modular monolith
Option 2: Microservices
Option 3: Serverless functions only
```

## Decision

```text
Use a modular monolith for the MVP.
```

## Reason

```text
A modular monolith keeps deployment simple while allowing the codebase to preserve clear domain boundaries. This supports faster delivery and reduces operational overhead for the early product stage.
```

## Consequences

```text
Positive: simpler deployment, easier debugging, lower operational cost.
Negative: discipline is required to maintain module boundaries.
Neutral: some modules may be extracted later if scale or team structure requires it.
```

---

# 2. Example — Use URI-Based API Versioning

## Decision

```text
Use URI versioning such as /api/v1 for early REST APIs.
```

## Reason

```text
URI versioning is simple, visible, easy to document and suitable for early SaaS APIs with external or separately deployed clients.
```

---

# 3. Example — Use Entitlement Checks Instead of Plan Name Checks

## Decision

```text
Application code should check entitlements rather than hardcoded plan names.
```

## Reason

```text
Entitlements make billing behavior more flexible and reduce plan-name coupling across product code.
```

---

# 4. Final Principle

> Examples show that ADRs should capture the decision logic behind architecture, not only the selected technology.