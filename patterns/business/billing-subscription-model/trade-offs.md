## FILE: `patterns/business/billing-subscription-model/trade-offs.md`

# Billing Subscription Model — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
revenue clarity
pricing execution
product access consistency
support readiness
billing auditability
enterprise readiness
upgrade and downgrade reliability
```

---

# 2. Costs

This Pattern adds:

```text
billing domain complexity
webhook handling
state synchronization
entitlement testing
support process design
invoice lifecycle management
```

---

# 3. Simple Pricing Trade-Off

Simple plans are easier to sell and implement.

Cost:

```text
less monetization flexibility
harder enterprise customization
less fine-grained usage capture
```

---

# 4. Usage-Based Pricing Trade-Off

Usage-based pricing can align price with value.

Cost:

```text
more metering complexity
more invoice surprises
more support questions
more billing edge cases
```

---

# 5. Trial Trade-Off

Free trials reduce purchase friction.

Risk:

```text
low-quality signups
support burden
trial abuse
delayed revenue
```

Mitigation:

```text
trial limits
activation tracking
billing reminders
clear conversion path
```

---

# 6. Main Risks

Key risks:

```text
entitlement drift
payment webhook duplication
failed payment confusion
inconsistent downgrade behavior
billing admin permission mistakes
missing audit events
hardcoded plan checks
```

---

# 7. Mitigations

Mitigate with:

- entitlement matrix;
- central billing state model;
- idempotent webhook processing;
- billing tests;
- audit logging;
- customer-visible billing status;
- support runbooks.

---

# 8. Final Principle

> Billing trade-offs should be made consciously because they affect revenue, access and trust at the same time.
