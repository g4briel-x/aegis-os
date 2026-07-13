## FILE: `patterns/business/billing-subscription-model/examples/examples.md`

# Billing Subscription Model — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Context

A SaaS platform helps creators prepare film, series and documentary projects for financing.

## Plans

```text
Starter: 1 project, basic readiness checklist
Pro: 10 projects, advanced review, document storage
Studio: unlimited projects, team collaboration, investor-room access
Enterprise: custom onboarding, advanced support, custom limits
```

## Entitlements

```text
max_projects
max_storage_gb
advanced_review_enabled
investor_room_enabled
team_collaboration_enabled
priority_support_enabled
```

---

# 2. Example — Subscription States

```text
trialing:
  Pro features available for 14 days

active:
  paid plan access enabled

past_due:
  access remains active for 7-day grace period

payment_failed:
  project editing disabled, billing page available

cancelled:
  read-only access for 30 days, export allowed
```

---

# 3. Example — Downgrade Rule

## Scenario

A workspace with 12 projects wants to downgrade to a plan allowing 5 projects.

## Rule

```text
Downgrade is scheduled for period end.
Workspace owner must archive or export projects until active project count is 5 or less.
```

---

# 4. Example — Webhook Idempotency

## Event

```text
invoice.payment_succeeded
```

## Rule

```text
Process provider event id only once.
If duplicate webhook arrives, return success without applying duplicate state change.
```

---

# 5. Final Principle

> Examples show that billing design must define both commercial rules and product access behavior.
