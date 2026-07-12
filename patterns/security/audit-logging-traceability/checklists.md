## FILE: `patterns/security/audit-logging-traceability/checklists.md`

# Audit Logging Traceability — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Sensitive actions exist
[ ] Admin actions exist
[ ] Tenant data exists
[ ] File access exists
[ ] Permission changes exist
[ ] Incident response needs evidence
[ ] Audit access policy is needed
```

---

# 2. Event Design Checklist

```text
[ ] Event id is generated
[ ] Timestamp is recorded
[ ] Actor is recorded
[ ] Tenant scope is recorded
[ ] Action name is stable
[ ] Resource is recorded
[ ] Result is recorded
[ ] Request id is recorded
```

---

# 3. Action Catalog Checklist

```text
[ ] Authentication events defined
[ ] Role and permission events defined
[ ] Membership events defined
[ ] File access events defined
[ ] Billing events defined if relevant
[ ] Support access events defined
[ ] Security setting events defined
```

---

# 4. Metadata Safety Checklist

```text
[ ] No passwords logged
[ ] No tokens logged
[ ] No secret values logged
[ ] No full sensitive payloads logged
[ ] Metadata is minimal
[ ] Metadata is useful for investigation
```

---

# 5. Access and Retention Checklist

```text
[ ] Audit log readers defined
[ ] Write access restricted
[ ] Retention period defined
[ ] Export rules defined if needed
[ ] Deletion rules defined
[ ] Audit log access reviewed
```

---

# 6. Test Checklist

```text
[ ] Role change creates audit event
[ ] File download creates audit event
[ ] Support access creates audit event
[ ] Security setting change creates audit event
[ ] Audit event includes tenant id
[ ] Audit event excludes secrets
```

---

# 7. Final Principle

> Audit checklists should prove that critical actions leave safe and reliable evidence.
