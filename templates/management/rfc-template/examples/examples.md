## FILE: `templates/management/rfc-template/examples/examples.md`

# RFC Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Feature Flag Rollout RFC

## RFC Title

```text
Adopt Feature Flag Rollout for Customer-Facing Releases
```

## Problem Statement

```text
Customer-facing features are currently activated at deployment time, which makes it difficult to stage rollout, limit exposure, monitor behavior and disable risky features quickly.
```

## Proposal

```text
Introduce a standard feature flag rollout process for all customer-facing features with beta targeting, monitoring, rollback ownership and cleanup requirements.
```

## Goals

```text
Reduce release risk.
Support beta activation.
Improve rollback speed.
```

## Non-Goals

```text
Replace the deployment pipeline.
Create a full experimentation platform immediately.
```

## Recommended Option

```text
Use a simple feature flag layer integrated with release planning and monitoring.
```

## Success Metric

```text
All customer-facing risky features released in the next quarter use a documented rollout plan.
```

---

# 2. Example — API Versioning RFC

## Proposal

```text
Use URI-based API versioning for early public REST APIs.
```

## Reason

```text
URI versioning is explicit, easy to document and simple for external clients during the early SaaS stage.
```

---

# 3. Example — Billing Entitlement RFC

## Proposal

```text
Application code should check entitlement keys instead of raw plan names.
```

## Reason

```text
This reduces coupling between pricing packages and product access logic.
```

---

# 4. Final Principle

> Examples show that RFCs help teams debate the change before implementation pressure begins.
