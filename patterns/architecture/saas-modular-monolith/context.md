## FILE: `patterns/architecture/saas-modular-monolith/context.md`

# SaaS Modular Monolith — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern is best for SaaS products that need speed and structure at the same time.

Typical contexts:

```text
MVP development
private beta
public beta
early customer pilots
first production release
early growth stage
```

---

# 2. Team Context

Recommended team profile:

```text
1 to 10 engineers
small product team
shared deployment responsibility
limited DevOps capacity
fast iteration requirement
```

---

# 3. Product Context

Useful when:

- feature scope is evolving;
- user roles are still being refined;
- billing may change;
- workflows are still being validated;
- customer feedback can reshape the domain;
- core entities are not fully stable.

---

# 4. Technical Context

Recommended when:

- one runtime is enough;
- one database is manageable;
- one CI/CD pipeline is preferred;
- infrastructure simplicity matters;
- service boundaries are not stable enough for microservices.

---

# 5. Warning Signs

This Pattern may start to stretch when:

- one module slows the entire system;
- teams block each other frequently;
- deployments become risky due to unrelated changes;
- database ownership becomes unclear;
- module boundaries are repeatedly violated;
- one domain needs independent scaling.

---

# 6. Final Principle

> The modular monolith fits contexts where learning is still more important than distributed autonomy.
