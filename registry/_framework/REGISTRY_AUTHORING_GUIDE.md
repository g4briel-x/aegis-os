## FILE: `registry/_framework/REGISTRY_AUTHORING_GUIDE.md`

# Registry Authoring Guide

Version: 0.1.0  
Status: Draft

---

# 1. Authoring Process

Use this sequence:

```text
1. Identify the asset
2. Confirm asset type
3. Assign unique id
4. Define domain and category
5. Add path
6. Add status and maturity
7. Add summary
8. Add tags
9. Add related assets
10. Validate consistency
```

---

# 2. ID Rules

Use this format:

```text
<domain>.<asset-slug>
```

Examples:

```text
engineering.senior-developer
security.review-api-security
business.pricing-strategy-template
```

For framework assets:

```text
framework.registry
framework.templates
framework.skills
```

---

# 3. Summary Rule

A summary should be short and functional.

Weak:

```text
This is a very useful file.
```

Better:

```text
Defines the reusable structure for reviewing SaaS security risks before release.
```

---

# 4. Relationship Rule

Only add relationships that are useful for discovery or orchestration.

Good:

```yaml
related_assets:
  - id: security.rbac-permission-model
    relationship: uses
```

Avoid:

```yaml
related_assets:
  - id: every-other-security-file
    relationship: related_to
```

---

# 5. Review Checklist

```text
[ ] id is unique
[ ] path exists
[ ] type is correct
[ ] domain is correct
[ ] status is accurate
[ ] maturity is accurate
[ ] summary is useful
[ ] tags are relevant
[ ] relationships are not excessive
```

---

# 6. Final Principle

> Registry entries should help Aegis OS choose the right asset at the right time.
