## FILE: `templates/operations/release-plan-template/usage.md`

# Release Plan Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define release name, version and owner
2. Confirm release scope and excluded changes
3. Assess customer, business and operational impact
4. Identify risks and dependencies
5. Confirm test readiness
6. Define deployment steps
7. Define validation checks
8. Define rollback or recovery plan
9. Define monitoring and communication plan
10. Collect approvals before release
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Product review
Engineering review
QA review
Security review if relevant
Operations review
Support review if customer-facing
Final release approval
```

---

# 3. Writing Rules

A Release Plan should:

- be specific;
- identify owners;
- avoid vague validation;
- include rollback triggers;
- include monitoring signals;
- document accepted risks;
- include communication needs;
- record approvals.

---

# 4. Validation Rule

Weak:

```text
Check production.
```

Better:

```text
Confirm login, project creation, document upload and project submission succeed in production using a test workspace.
```

---

# 5. Rollback Rule

A rollback plan should define:

```text
trigger
owner
method
expected duration
validation after rollback
customer communication if needed
```

---

# 6. Final Principle

> Use the Release Plan Template before production deployment, not after risk appears.
