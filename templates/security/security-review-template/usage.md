## FILE: `templates/security/security-review-template/usage.md`

# Security Review Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define review scope
2. Identify roles, resources and data
3. Classify security risk level
4. Review authentication
5. Review authorization
6. Review tenant isolation
7. Review data protection
8. Review APIs and input validation
9. Review audit logging
10. Define threats, findings and security tests
11. Make release decision
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Engineering self-review
Security review
Architecture review if structural impact exists
Operations review if production risk exists
Product review if user experience or customer promise changes
Final release decision
```

---

# 3. Writing Rules

A Security Review should:

- be specific;
- identify protected resources;
- define denied behavior;
- include tenant isolation checks;
- include security test cases;
- document accepted risks;
- end with a release decision.

---

# 4. Finding Rule

Weak:

```text
Permissions need review.
```

Better:

```text
The submit project endpoint checks authentication but does not verify project.submit permission for the workspace. Add server-side permission enforcement before release.
```

---

# 5. Final Principle

> Use the Security Review Template before release, not after a production security incident.
