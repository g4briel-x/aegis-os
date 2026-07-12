## FILE: `patterns/security/tenant-data-isolation/checklists.md`

# Tenant Data Isolation — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Multiple customers share the system
[ ] Private tenant data exists
[ ] Users belong to organizations or workspaces
[ ] API endpoints expose tenant data
[ ] Files or documents are tenant-scoped
[ ] Background jobs process tenant data
```

---

# 2. Data Model Checklist

```text
[ ] Primary tenant entity defined
[ ] Tenant-scoped tables identified
[ ] Ownership fields included
[ ] Membership model defined
[ ] Cross-tenant relationships reviewed
[ ] Sensitive data ownership documented
[ ] Deletion and retention reviewed
```

---

# 3. Query Checklist

```text
[ ] Protected queries include tenant scope
[ ] Generic unsafe lookups avoided
[ ] Search queries include tenant filters
[ ] Exports include tenant scope
[ ] Reports avoid cross-tenant leakage
[ ] Query helpers are reviewed
```

---

# 4. API Checklist

```text
[ ] Endpoint requires authentication
[ ] Tenant membership is checked
[ ] Permission is checked
[ ] Resource ownership is checked
[ ] Denied access is safe
[ ] Response excludes unauthorized fields
```

---

# 5. File Access Checklist

```text
[ ] File metadata includes tenant scope
[ ] Downloads check authorization
[ ] Uploads attach correct tenant
[ ] Signed URLs are scoped and short-lived
[ ] Sensitive downloads are audited
[ ] Storage path is not the only protection
```

---

# 6. Test Checklist

```text
[ ] Cross-tenant read denied
[ ] Cross-tenant write denied
[ ] Cross-tenant file download denied
[ ] Wrong workspace search result denied
[ ] Background job scope mismatch rejected
[ ] Support access audited
```

---

# 7. Final Principle

> Tenant isolation checklists should prove that customer boundaries hold under normal and hostile paths.