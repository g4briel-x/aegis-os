## FILE: `templates/operations/runbook-template/usage.md`

# Runbook Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define the operational procedure
2. Define when the runbook should be used
3. Define required access and prerequisites
4. Add safety checks
5. Write step-by-step actions
6. Define expected results for each step
7. Define validation checks
8. Define rollback or recovery
9. Define escalation rules
10. Add observability and audit requirements
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Operations review
Engineering review
Security review if privileged access is required
Support review if customer communication is involved
Product review if customer workflow is affected
```

---

# 3. Writing Rules

A Runbook should:

- use action-oriented steps;
- avoid vague instructions;
- include stop conditions;
- include validation;
- include escalation;
- include rollback or recovery;
- identify required permissions;
- be safe for production use.

---

# 4. Step Quality Rule

Weak:

```text
Check the system.
```

Better:

```text
Open the production queue dashboard and confirm whether pending jobs exceed 500 for more than 10 minutes.
```

---

# 5. Safety Rule

A Runbook should tell the operator when not to continue.

Example:

```text
Stop and escalate if the database shows active lock waits longer than 60 seconds.
```

---

# 6. Final Principle

> Use the Runbook Template to make operational response calm, safe and consistent.
