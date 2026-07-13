## FILE: `templates/operations/postmortem-template/usage.md`

# Postmortem Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Confirm postmortem is required
2. Assign owner and facilitator
3. Collect timeline and evidence
4. Document customer and business impact
5. Analyze detection and response
6. Identify direct cause and root cause
7. Capture what went well and wrong
8. Define corrective actions
9. Assign owners and due dates
10. Review completion later
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Incident team review
Engineering review
Operations review
Security review if relevant
Support review if customer-visible
Product review if workflow impact exists
Leadership review for major incidents
```

---

# 3. Writing Rules

A Postmortem should:

- be factual;
- avoid blame;
- include timestamps;
- describe real customer impact;
- separate direct cause from root cause;
- include detection and response gaps;
- assign corrective actions;
- avoid vague follow-up tasks.

---

# 4. Corrective Action Rule

Weak:

```text
Improve monitoring.
```

Better:

```text
Add an alert for project submission error rate above 5% for 5 minutes, owned by Operations, due by 2026-07-20.
```

---

# 5. Blameless Rule

Avoid:

```text
The developer forgot to test the migration.
```

Better:

```text
The release process did not require validation of existing records before adding a required column.
```

---

# 6. Final Principle

> Use the Postmortem Template to convert incidents into system improvements.
