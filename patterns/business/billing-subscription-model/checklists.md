## FILE: `patterns/business/billing-subscription-model/checklists.md`

# Billing Subscription Model — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] SaaS product has or will have paid plans
[ ] Plan-based access exists
[ ] Subscription state affects product behavior
[ ] Billing admins are needed
[ ] Invoices or payment records matter
[ ] Failed payment behavior must be defined
```

---

# 2. Plan Checklist

```text
[ ] Plan names are defined
[ ] Target customer per plan is defined
[ ] Price is defined
[ ] Billing interval is defined
[ ] Included features are defined
[ ] Limits are defined
[ ] Upgrade path is defined
```

---

# 3. Entitlement Checklist

```text
[ ] Entitlement matrix exists
[ ] Product access maps to entitlements
[ ] Limits are enforceable
[ ] Entitlement checks are centralized
[ ] Plan names are not scattered in code
[ ] Tests cover paid and unpaid access
```

---

# 4. Subscription State Checklist

```text
[ ] Trialing behavior defined
[ ] Active behavior defined
[ ] Past-due behavior defined
[ ] Payment-failed behavior defined
[ ] Cancel-scheduled behavior defined
[ ] Cancelled behavior defined
[ ] Expired behavior defined
```

---

# 5. Payment Failure Checklist

```text
[ ] Retry schedule defined
[ ] Grace period defined
[ ] Customer notification defined
[ ] Access restriction rule defined
[ ] Billing admin recovery path defined
[ ] Support handling defined
```

---

# 6. Security and Audit Checklist

```text
[ ] Billing permissions defined
[ ] Invoice access restricted
[ ] Payment provider webhooks verified
[ ] Billing changes audited
[ ] Sensitive payment data not stored locally
[ ] Support access controlled
```

---

# 7. Final Principle

> Billing checklists should prove that every subscription state has predictable customer and product behavior.
