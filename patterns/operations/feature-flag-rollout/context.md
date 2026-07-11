## FILE: `patterns/operations/feature-flag-rollout/context.md`

# Feature Flag Rollout — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern is best for SaaS releases where activation risk must be controlled.

Typical scenarios:

```text
new feature launch
beta program
gradual migration
new pricing or billing flow
new permission model
new onboarding path
new AI feature
large frontend redesign
```

---

# 2. Product Context

Use this Pattern when product needs:

- beta access;
- progressive launch;
- customer-specific activation;
- experiment comparison;
- early feedback;
- controlled general availability.

---

# 3. Engineering Context

Use this Pattern when engineering needs:

- safe deployment;
- quick rollback;
- branch reduction;
- production validation;
- migration control;
- kill switch for risky logic.

---

# 4. Operations Context

Use this Pattern when operations needs:

- controlled blast radius;
- measurable rollout stages;
- monitoring before expansion;
- rollback without redeploy;
- incident prevention.

---

# 5. Warning Signs

Feature flag usage is unhealthy when:

- flags are never deleted;
- flag names are unclear;
- multiple flags interact unpredictably;
- tests ignore flag states;
- rollout owners are unknown;
- flags bypass security controls;
- stale flags create dead code.

---

# 6. Final Principle

> A feature flag is only safe when its lifecycle is managed from creation to deletion.
