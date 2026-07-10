## FILE: `playbooks/security/respond-to-security-incident/outputs.md`

# Respond to Security Incident — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Incident Classification

Purpose:

Define the type and severity of the incident.

Required sections:

```text
Incident type:
Status:
Severity:
Affected system:
Initial evidence:
Owner:
```

---

# 2. Impact Assessment

Purpose:

Identify what may be affected.

Required sections:

```text
Affected users:
Affected data:
Affected systems:
Credential impact:
Business impact:
Unknowns:
```

---

# 3. Evidence Record

Purpose:

Preserve what is known and when.

Required sections:

```text
Timestamp:
Source:
Evidence:
Location:
Access restriction:
Notes:
```

---

# 4. Containment Plan

Purpose:

Define immediate actions to reduce exposure.

Required sections:

```text
Action:
Reason:
Owner:
Risk:
Status:
Verification:
```

---

# 5. Investigation Summary

Purpose:

Explain likely cause and supporting evidence.

Required sections:

```text
Likely root cause:
Evidence:
Affected path:
Confidence:
Open questions:
```

---

# 6. Recovery Plan

Purpose:

Restore secure operation.

Required sections:

```text
Recovery action:
Owner:
Verification:
Risk:
Status:
```

---

# 7. Prevention Actions

Purpose:

Reduce recurrence.

Required sections:

```text
Action:
Owner:
Priority:
Due date:
Expected prevention effect:
```

---

# 8. Post-Incident Review

Purpose:

Document lessons and follow-up.

Required sections:

```text
Timeline:
Root cause:
Impact:
Response summary:
Lessons learned:
Follow-up actions:
```

---

# 9. Final Principle

> Security incident outputs must create traceability from signal to containment, recovery and prevention.
