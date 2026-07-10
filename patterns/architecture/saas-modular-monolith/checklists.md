## FILE: `patterns/architecture/saas-modular-monolith/checklists.md`

# SaaS Modular Monolith — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Product is MVP, beta or early growth
[ ] Team wants operational simplicity
[ ] Domain boundaries are still evolving
[ ] Independent scaling is not yet mandatory
[ ] One deployable application is acceptable
[ ] Future extraction may be useful but not urgent
```

---

# 2. Module Design Checklist

```text
[ ] Core modules identified
[ ] Each module has clear responsibility
[ ] Module public interfaces are defined
[ ] Cross-module dependencies are controlled
[ ] Shared layer is limited
[ ] Business logic is not hidden in utilities
[ ] Tests exist per module
```

---

# 3. Data Ownership Checklist

```text
[ ] Tables are mapped to owning modules
[ ] Cross-module relationships are documented
[ ] Migrations are reviewed
[ ] Tenant boundary is clear
[ ] Sensitive data ownership is defined
[ ] Reporting queries do not break ownership assumptions
```

---

# 4. API and Service Boundary Checklist

```text
[ ] API does not expose database internals directly
[ ] Application services enforce business rules
[ ] Authorization checks are placed at boundaries
[ ] Errors are standardized
[ ] Contracts are documented
[ ] Tests cover module behavior
```

---

# 5. Extraction Readiness Checklist

```text
[ ] Candidate modules are documented
[ ] Extraction triggers are defined
[ ] Data dependencies are known
[ ] Module interface is stable
[ ] Operational reason for extraction exists
[ ] Team ownership is possible
```

---

# 6. Final Principle

> The Pattern is healthy when module boundaries are visible in code, data, tests and review.