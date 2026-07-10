## FILE: `skills/security/security-engineer/checklists.md`

# Security Engineer — Checklists

Version: 0.2.0  
Status: Premium Draft

---

# 1. Security Review Checklist

```text
[ ] Scope defined
[ ] Protected assets identified
[ ] Actors identified
[ ] Trust boundaries documented
[ ] Authentication reviewed
[ ] Authorization reviewed
[ ] Sensitive data reviewed
[ ] Abuse cases considered
[ ] Mitigations defined
```

---

# 2. Authentication Checklist

```text
[ ] Login flow reviewed
[ ] Session or token handling reviewed
[ ] Password or credential handling reviewed
[ ] Account recovery considered
[ ] Brute force protection considered
[ ] Logout and expiry considered
[ ] Sensitive errors avoided
```

---

# 3. Authorization Checklist

```text
[ ] Roles identified
[ ] Permissions mapped
[ ] Server-side enforcement confirmed
[ ] Privilege escalation risk reviewed
[ ] Tenant boundaries considered
[ ] Admin actions protected
[ ] Audit logging considered
```

---

# 4. API Security Checklist

```text
[ ] Request validation defined
[ ] Authentication required where needed
[ ] Authorization checked per resource
[ ] Rate limiting considered
[ ] Error responses do not leak sensitive data
[ ] Input size limits considered
[ ] Sensitive endpoints identified
```

---

# 5. Secrets Checklist

```text
[ ] No secrets hardcoded
[ ] Secrets excluded from repository
[ ] Secrets stored securely
[ ] Secrets scoped to least privilege
[ ] Rotation considered
[ ] Logs do not expose secrets
[ ] Revocation path defined
```

---

# 6. 4-Pass Validation Checklist

```text
[ ] Pass 1 completed — assets, scope and boundaries
[ ] Pass 2 completed — authentication, authorization and data protection
[ ] Pass 3 completed — vulnerabilities and mitigations
[ ] Pass 4 completed — operations, audit and incident readiness
[ ] Weaknesses corrected or documented
```

---

# 7. Final Principle

> Security checklists prevent critical risks from being missed during fast delivery.