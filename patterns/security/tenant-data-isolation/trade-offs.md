## FILE: `patterns/security/tenant-data-isolation/trade-offs.md`

# Tenant Data Isolation — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
customer data protection
enterprise readiness
authorization clarity
API safety
testing discipline
auditability
privacy posture
```

---

# 2. Costs

This Pattern adds:

```text
schema design effort
query complexity
test matrix expansion
authorization overhead
support access governance
migration discipline
```

---

# 3. Shared Database Trade-Off

A shared database is operationally simple, but requires strong logical isolation.

Benefits:

```text
simpler deployment
lower infrastructure cost
easier reporting
faster MVP delivery
```

Risks:

```text
query mistakes can expose data
cross-tenant joins can be unsafe
large tenants may affect others
```

---

# 4. Separate Database Trade-Off

Separate databases improve isolation, but add operational complexity.

Useful when:

- compliance requires stronger separation;
- enterprise customers demand isolation;
- tenants have very different scale;
- custom backup and restore is needed.

---

# 5. Admin Access Trade-Off

Support access helps operations, but increases privacy risk.

Mitigation:

```text
approval
time limits
audit logs
reason codes
restricted fields
customer visibility when needed
```

---

# 6. Main Risks

Key risks:

```text
missing tenant filters
unsafe exports
file authorization bypass
search index leakage
background job scope mistakes
support over-access
weak tests
```

---

# 7. Mitigations

Mitigate with:

- tenant-aware repository methods;
- object-level authorization;
- cross-tenant tests;
- audit logs;
- code review checklist;
- security review;
- safe defaults.

---

# 8. Final Principle

> Tenant isolation trades extra design discipline for customer trust and security resilience.
