## FILE: `patterns/business/billing-subscription-model/context.md`

# Billing Subscription Model — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS products moving from free usage, pilots or manual sales toward repeatable subscription revenue.

Typical contexts:

```text
MVP pricing
paid pilot
self-serve subscription
B2B workspace billing
usage-based AI SaaS
team-based SaaS
enterprise tier planning
```

---

# 2. Product Context

Use this Pattern when the product has:

- plans;
- trials;
- paid tiers;
- workspace billing;
- feature gates;
- storage or usage limits;
- billing admins;
- cancellation flows.

---

# 3. Business Context

The Pattern is useful when the team needs to define:

```text
free plan
starter plan
pro plan
business plan
enterprise plan
monthly billing
annual billing
discounts
paid pilots
custom contracts
```

---

# 4. Technical Context

The Pattern may require:

- payment provider integration;
- subscription table;
- plan table;
- entitlement service;
- invoice sync;
- webhook processing;
- billing audit logs;
- background jobs for retries or sync.

---

# 5. Security Context

Billing affects sensitive areas:

```text
payment metadata
billing admin permissions
invoice access
customer identity
workspace access
subscription state changes
audit logs
```

Payment card data should usually remain inside the payment provider, not the SaaS application.

---

# 6. Warning Signs

Billing design is weak when:

- plan names are hardcoded across the app;
- feature access is checked inconsistently;
- failed payments are ignored;
- invoices are not linked to customer accounts;
- users can access paid features after cancellation accidentally;
- downgrades create impossible states;
- billing changes are not audited.

---

# 7. Final Principle

> Billing context should connect commercial promise, product access and operational reality.
