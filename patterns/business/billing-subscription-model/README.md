## FILE: `patterns/business/billing-subscription-model/README.md`

# Billing Subscription Model Pattern

Version: 0.1.0  
Status: Draft  
Domain: Business  
Category: SaaS Monetization

---

# 1. Purpose

The Billing Subscription Model Pattern defines a reusable model for structuring SaaS pricing, subscriptions, plans, entitlements, invoices, trials, upgrades, downgrades and cancellation behavior.

It helps teams connect business pricing decisions to product access rules, billing operations, customer experience, data model design and revenue tracking.

---

# 2. Problem

SaaS teams often add billing late or treat it as only a payment integration.

Common failures:

```text
pricing plans are unclear
feature access is not mapped to plans
trial rules are inconsistent
upgrades and downgrades are not defined
billing state is not reflected in product access
failed payments are not handled
cancellations create confusion
invoices and subscriptions are not auditable
```

---

# 3. Recommended Solution

Define billing as a product and business system.

A good subscription model should define:

```text
plans
prices
billing interval
trial rules
subscription states
entitlements
usage limits
upgrade rules
downgrade rules
cancellation rules
invoice behavior
payment failure behavior
audit and reporting rules
```

---

# 4. Recommended When

Use this Pattern when:

- a SaaS product needs paid subscriptions;
- pricing tiers are being defined;
- plan-based feature access is required;
- trials, pilots or freemium offers exist;
- billing must integrate with product permissions;
- revenue reporting matters;
- customer lifecycle states must control access.

---

# 5. Avoid When

Avoid overbuilding this Pattern when:

- the product is still pure discovery;
- billing is fully manual for early pilots;
- pricing is not yet validated;
- payment processing is intentionally delayed;
- enterprise contracts are fully custom.

Even then, the future billing assumptions should be documented.

---

# 6. Related Assets

```text
Related skills:
product.product-manager-saas
product.business-analyst
engineering.software-architect
engineering.database-engineer
security.security-engineer

Related playbooks:
product.define-pricing-strategy
product.define-saas-mvp
product.create-prd
business.create-go-to-market-plan
security.design-auth-rbac
engineering.design-saas-data-model

Related patterns:
product.saas-mvp-scope
security.rbac-permission-model
security.audit-logging-traceability
engineering.database-migration-safety
```

---

# 7. Final Principle

> SaaS billing is not just payment collection. It is the contract between price, access, value and customer lifecycle.
