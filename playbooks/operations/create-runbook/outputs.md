## FILE: `playbooks/operations/create-runbook/outputs.md`

# Create Runbook — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Operational Runbook

Purpose:

Provide the complete operational procedure.

Required sections:

```text
Name:
Purpose:
Scope:
Trigger:
Prerequisites:
Procedure:
Verification:
Rollback:
Escalation:
Owner:
```

---

# 2. Trigger Definition

Purpose:

Clarify when to use the runbook.

Required sections:

```text
Trigger:
Source:
Severity:
When to use:
When not to use:
Approval:
```

---

# 3. Procedure Step

Purpose:

Define one executable step.

Required sections:

```text
Step:
Action:
Command or UI path:
Expected result:
Evidence:
Failure handling:
```

---

# 4. Command Reference

Purpose:

List commands safely.

Required sections:

```text
Command:
Purpose:
Environment:
Expected output:
Risk:
Notes:
```

---

# 5. Rollback Section

Purpose:

Define recovery if execution fails.

Required sections:

```text
Rollback trigger:
Owner:
Steps:
Data constraints:
Verification:
Escalation:
```

---

# 6. Escalation Path

Purpose:

Define who to contact.

Required sections:

```text
Condition:
Owner:
Channel:
Response expectation:
Next escalation:
```

---

# 7. Verification Checklist

Purpose:

Prove the runbook succeeded.

Required sections:

```text
Check:
Method:
Expected result:
Evidence:
Status:
```

---

# 8. Final Principle

> Runbook outputs must be operational, not theoretical.
