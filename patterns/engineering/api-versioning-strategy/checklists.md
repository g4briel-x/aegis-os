## FILE: `patterns/engineering/api-versioning-strategy/checklists.md`

# API Versioning Strategy — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] API clients exist
[ ] Clients may be deployed separately
[ ] External integrations exist or are planned
[ ] Breaking changes are possible
[ ] API documentation matters
[ ] Version usage should be tracked
```

---

# 2. Versioning Design Checklist

```text
[ ] Versioning method selected
[ ] Compatibility rules defined
[ ] Breaking change policy defined
[ ] Deprecation process defined
[ ] Migration window defined
[ ] Sunset policy defined
[ ] Owner assigned
```

---

# 3. Breaking Change Checklist

```text
[ ] Affected clients identified
[ ] New version or compatibility path defined
[ ] Migration guide written
[ ] Contract tests added
[ ] Documentation updated
[ ] Communication plan prepared
[ ] Sunset date defined
```

---

# 4. Contract Test Checklist

```text
[ ] Request schema tested
[ ] Response schema tested
[ ] Error schema tested
[ ] Authentication behavior tested
[ ] Authorization behavior tested
[ ] Pagination tested
[ ] Webhook payloads tested if relevant
```

---

# 5. Documentation Checklist

```text
[ ] Current version documented
[ ] Supported versions documented
[ ] Deprecated versions documented
[ ] Changelog updated
[ ] Migration guide linked
[ ] Examples updated
[ ] Sunset dates visible
```

---

# 6. Monitoring Checklist

```text
[ ] Requests by version tracked
[ ] Deprecated endpoint usage tracked
[ ] Errors by version tracked
[ ] Client identifiers tracked when safe
[ ] Migration progress reviewed
[ ] Alerts defined for unexpected legacy usage
```

---

# 7. Final Principle

> API versioning checklists prevent accidental client breakage.
