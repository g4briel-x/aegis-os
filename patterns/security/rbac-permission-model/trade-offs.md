## FILE: `patterns/security/rbac-permission-model/trade-offs.md`

# RBAC Permission Model — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
security clarity
least privilege
tenant isolation
testability
auditability
API consistency
admin governance
enterprise readiness
```

---

# 2. Costs

This Pattern adds:

```text
design overhead
permission matrix maintenance
more test cases
policy review effort
implementation complexity
possible friction for fast prototypes
```

---

# 3. RBAC Versus ABAC

RBAC is better when:

- roles are stable;
- permissions map well to responsibilities;
- customers understand role names;
- the product needs simplicity.

Attribute-based access control may be better when:

- rules depend on many conditions;
- dynamic policy logic is required;
- user attributes drive access;
- complex enterprise policies are needed.

A hybrid model is often useful:

```text
RBAC for role permissions
ownership checks for resources
tenant checks for isolation
conditions for lifecycle state
```

---

# 4. Main Risks

Key risks:

```text
role explosion
permissions too broad
admin overreach
cross-tenant query mistakes
frontend-only enforcement
incomplete denied-access tests
support access without audit
```

---

# 5. Mitigations

Mitigate with:

- least privilege defaults;
- permission matrix review;
- centralized policy definitions;
- tenant-scoped query helpers;
- mandatory permission tests;
- audit logs for sensitive actions;
- periodic access review.

---

# 6. Final Principle

> RBAC reduces risk only when roles remain understandable and permissions remain enforceable.
