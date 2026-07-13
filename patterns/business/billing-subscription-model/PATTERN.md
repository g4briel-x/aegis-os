## FILE: `patterns/business/billing-subscription-model/PATTERN.md`

# Billing Subscription Model Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS product needs to charge customers in a way that is clear, reliable and connected to the product experience.

Billing problems appear when:

- plans are not linked to features;
- subscriptions are not linked to workspaces or organizations;
- trial expiration is unclear;
- failed payments do not change access predictably;
- upgrades and downgrades have no policy;
- invoices are hard to reconcile;
- support cannot explain billing state;
- analytics cannot connect revenue to usage.

---

# 2. Context

This Pattern applies to SaaS products with:

```text
subscription plans
workspace or organization accounts
paid pilots
free trials
usage limits
feature tiers
billing admins
invoices
payment provider integration
revenue reporting
```

It is especially useful for B2B SaaS, vertical SaaS, creator platforms, AI SaaS and collaboration products.

---

# 3. Forces

Key forces:

```text
pricing simplicity versus monetization flexibility
self-serve billing versus sales-led contracts
feature access versus customer trust
trial generosity versus revenue discipline
payment failure handling versus customer continuity
custom enterprise pricing versus product consistency
```

---

# 4. Recommended Model

Use a subscription model with:

```text
Customer
Account or tenant
Plan
Price
Subscription
Subscription item
Entitlement
Usage limit
Invoice
Payment status
Billing event
```

Example:

```text
Workspace subscribes to Pro plan.
Pro plan allows 10 active projects, 50 GB storage and advanced review workflows.
Billing admin can manage subscription.
Members can use features based on workspace entitlements.
```

---

# 5. Subscription States

Define subscription lifecycle states.

Recommended states:

```text
trialing
active
past_due
payment_failed
paused
cancel_scheduled
cancelled
expired
manual_review
```

Each state should define product access behavior.

---

# 6. Entitlements

Entitlements define what a customer can access.

Examples:

```text
max_projects
max_team_members
storage_limit_gb
advanced_reviews_enabled
investor_room_enabled
priority_support_enabled
api_access_enabled
custom_branding_enabled
```

Product code should check entitlements, not raw plan names whenever possible.

---

# 7. Upgrade and Downgrade Rules

Define what happens when customers change plans.

Upgrade rules:

```text
access increases immediately
billing prorates if applicable
new limits apply immediately
audit event is created
```

Downgrade rules:

```text
effective immediately or at period end
blocked if current usage exceeds lower limit
grace period if needed
customer warning required
feature access reduced predictably
```

---

# 8. Payment Failure Rules

Define failed payment handling.

Example flow:

```text
payment fails
subscription becomes past_due
customer is notified
grace period starts
retry schedule runs
access remains active or limited according to policy
after grace period, access is restricted
billing admin can update payment method
```

---

# 9. Final Principle

> Billing behavior should be explicit enough that product, finance, support and engineering all describe it the same way.
