## FILE: `playbooks/security/design-auth-rbac/checklists.md`

# Design Auth RBAC — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Authentication Checklist

```text
[ ] Login method defined
[ ] Identity provider selected or assumed
[ ] Session or token model defined
[ ] User lifecycle defined
[ ] Invitation flow reviewed
[ ] MFA need reviewed
[ ] Password reset or recovery reviewed
```

---

# 2. Role Checklist

```text
[ ] Roles listed
[ ] Role purpose defined
[ ] Role scope defined
[ ] Role assignment rule defined
[ ] Role escalation risk reviewed
[ ] Admin roles minimized
[ ] Default role defined
```

---

# 3. Permission Checklist

```text
[ ] Protected resources listed
[ ] Actions defined
[ ] Role-permission matrix created
[ ] Denied actions documented
[ ] Conditional permissions documented
[ ] Sensitive actions reviewed
[ ] Least privilege applied
```

---

# 4. Tenant Isolation Checklist

```text
[ ] Tenant boundary defined
[ ] Tenant-scoped resources listed
[ ] Global resources listed
[ ] Cross-tenant restrictions defined
[ ] Shared resource rules defined
[ ] Support access reviewed
[ ] Object-level checks defined
```

---

# 5. API Authorization Checklist

```text
[ ] Each endpoint mapped to auth rule
[ ] Required role documented
[ ] Required permission documented
[ ] Ownership check documented
[ ] Tenant check documented
[ ] Denied cases documented
[ ] Audit need documented
```

---

# 6. Test Checklist

```text
[ ] Allowed access tests defined
[ ] Denied access tests defined
[ ] Cross-tenant tests defined
[ ] Unauthenticated tests defined
[ ] Admin-only tests defined
[ ] Role assignment tests defined
[ ] Sensitive data exposure tests defined
```

---

# 7. Final Principle

> RBAC checklists prevent security design from relying on vague role names instead of enforceable rules.
