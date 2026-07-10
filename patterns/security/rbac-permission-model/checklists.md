## FILE: `patterns/security/rbac-permission-model/checklists.md`

# RBAC Permission Model — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Multiple roles exist
[ ] Protected resources exist
[ ] User ownership matters
[ ] Tenant or workspace boundary exists
[ ] API endpoints need authorization
[ ] Sensitive data or files exist
[ ] Denied access must be tested
```

---

# 2. Role Checklist

```text
[ ] Role names are clear
[ ] Role purpose is defined
[ ] Role scope is defined
[ ] Role assignment rule is defined
[ ] Admin roles are minimized
[ ] Support access is handled separately
[ ] Role risk is documented
```

---

# 3. Permission Checklist

```text
[ ] Permissions are action-based
[ ] Broad permissions are justified
[ ] Sensitive permissions are identified
[ ] Permission names are consistent
[ ] Permission catalog is documented
[ ] Permission matrix exists
[ ] Denied behavior is documented
```

---

# 4. Tenant and Ownership Checklist

```text
[ ] Tenant boundary is defined
[ ] Resource ownership is defined
[ ] Cross-tenant access is denied
[ ] Shared resource behavior is explicit
[ ] File access follows resource ownership
[ ] Admin override behavior is audited
[ ] Support access is time-bound or approved
```

---

# 5. Enforcement Checklist

```text
[ ] Authentication is enforced
[ ] API authorization is enforced
[ ] Application service checks exist
[ ] Tenant-scoped queries are used
[ ] Frontend is not the only enforcement
[ ] Background jobs respect permissions where relevant
[ ] Sensitive actions create audit events
```

---

# 6. Test Checklist

```text
[ ] Allowed access tests exist
[ ] Wrong role tests exist
[ ] Wrong tenant tests exist
[ ] Wrong owner tests exist
[ ] Unauthenticated tests exist
[ ] Admin-only tests exist
[ ] Sensitive data exposure tests exist
```

---

# 7. Final Principle

> RBAC checklists should prove both access and denial.
