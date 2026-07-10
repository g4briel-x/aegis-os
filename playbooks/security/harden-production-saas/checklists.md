## FILE: `playbooks/security/harden-production-saas/checklists.md`

# Harden Production SaaS — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Production Baseline Checklist

```text
[ ] Production environment identified
[ ] Critical workflows listed
[ ] Sensitive data listed
[ ] Public surfaces listed
[ ] Third-party services listed
[ ] Review owner assigned
[ ] Launch or release decision deadline defined
```

---

# 2. Access Control Checklist

```text
[ ] Authentication reviewed
[ ] Session model reviewed
[ ] Admin roles reviewed
[ ] Least privilege reviewed
[ ] Service accounts reviewed
[ ] Stale access reviewed
[ ] Permission tests reviewed
```

---

# 3. Tenant Isolation Checklist

```text
[ ] Tenant model reviewed
[ ] Tenant-scoped resources listed
[ ] Cross-tenant API tests reviewed
[ ] File access isolation reviewed
[ ] Support access reviewed
[ ] Admin override behavior reviewed
[ ] Isolation gaps documented
```

---

# 4. API and Frontend Checklist

```text
[ ] Public endpoints reviewed
[ ] Authenticated endpoints reviewed
[ ] Rate limits reviewed
[ ] CORS reviewed
[ ] File uploads reviewed
[ ] Sensitive response fields reviewed
[ ] Error messages reviewed
```

---

# 5. Secrets Checklist

```text
[ ] Secrets inventory created
[ ] Secrets not committed
[ ] Secrets not logged
[ ] Environment scope reviewed
[ ] Secret permissions reviewed
[ ] Rotation plan reviewed
[ ] Exposed secrets rotated if needed
```

---

# 6. Monitoring and Recovery Checklist

```text
[ ] Error monitoring available
[ ] Security alerts defined
[ ] Audit logs available
[ ] Backup policy reviewed
[ ] Restore process reviewed
[ ] Rollback process reviewed
[ ] Incident response path reviewed
```

---

# 7. Final Principle

> Hardening checklists make production readiness visible instead of assumed.
