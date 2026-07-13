## FILE: `patterns/business/billing-subscription-model/solution.md`

# Billing Subscription Model — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Define billing as a structured domain.

Core components:

```text
plan catalog
price catalog
subscription state model
entitlement matrix
billing roles
invoice lifecycle
payment failure policy
upgrade and downgrade policy
webhook handling
audit logging
```

---

# 2. Plan Catalog

Create a plan catalog.

Example:

```text
Free
Starter
Pro
Business
Enterprise
```

Each plan should define:

```text
target customer
included features
limits
support level
billing interval
price
upgrade path
```

---

# 3. Entitlement Matrix

Map plans to product access.

Example:

```text
Feature | Free | Starter | Pro | Business
Projects | 1 | 5 | 25 | Unlimited
Storage | 1 GB | 10 GB | 100 GB | Custom
Team members | 1 | 3 | 10 | Custom
Advanced reviews | No | No | Yes | Yes
API access | No | No | Limited | Yes
```

Use an entitlement service or policy layer to avoid scattered plan checks.

---

# 4. Subscription State Model

Define how product access behaves by state.

Example:

```text
trialing: full trial access
active: paid plan access
past_due: grace period access
payment_failed: limited access or billing-only access
cancel_scheduled: active until period end
cancelled: read-only or no access according to policy
expired: no paid feature access
```

---

# 5. Billing Roles

Define who can manage billing.

Common roles:

```text
workspace_owner
billing_admin
platform_admin
support_admin
```

Billing actions should be permission-controlled and audited.

---

# 6. Webhook Handling

Payment provider webhooks should be:

```text
verified
idempotent
logged
retriable
mapped to internal subscription state
monitored
```

Examples:

```text
invoice.payment_succeeded
invoice.payment_failed
customer.subscription.updated
customer.subscription.deleted
checkout.session.completed
```

---

# 7. Upgrade and Downgrade Flow

Upgrade flow:

```text
select plan
confirm price
process payment or provider checkout
update subscription
apply entitlements
create audit event
show confirmation
```

Downgrade flow:

```text
check current usage
warn about lost access
choose effective date
apply downgrade rules
create audit event
notify billing admin
```

---

# 8. Cancellation Flow

Cancellation should define:

```text
immediate or period-end cancellation
data retention
export option
reactivation path
access after cancellation
feedback capture
```

Avoid dark patterns that block clear cancellation.

---

# 9. Final Principle

> The solution should separate payment processing, subscription state and product entitlement checks.
