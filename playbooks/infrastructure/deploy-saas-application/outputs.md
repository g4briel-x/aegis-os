## FILE: `playbooks/infrastructure/deploy-saas-application/outputs.md`

# Deploy SaaS Application — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Deployment Readiness Summary

Purpose:

Summarize whether deployment can proceed.

Required sections:

```text
Release:
Target environment:
Commit:
CI status:
Approvals:
Blocking issues:
Decision:
```

---

# 2. Environment Checklist Result

Purpose:

Document environment readiness.

Required sections:

```text
Environment:
Configuration status:
Secrets status:
Permission status:
Open issues:
```

---

# 3. Deployment Execution Log

Purpose:

Record what happened during deployment.

Required sections:

```text
Start time:
End time:
Operator:
Version deployed:
Commands or platform actions:
Warnings:
Status:
```

---

# 4. Smoke Test Result

Purpose:

Confirm critical behavior after deployment.

Required sections:

```text
Test:
Expected result:
Actual result:
Status:
Evidence:
```

---

# 5. Monitoring Result

Purpose:

Confirm production health after deployment.

Required sections:

```text
Signal:
Threshold:
Observed value:
Status:
Monitoring window:
```

---

# 6. Rollback Decision

Purpose:

Record whether rollback was needed.

Required sections:

```text
Decision:
Reason:
Trigger:
Owner:
Action taken:
Verification:
```

---

# 7. Post-Deployment Confirmation

Purpose:

Communicate final deployment status.

Required sections:

```text
Deployment status:
User impact:
Known issues:
Follow-up actions:
Communication sent:
```

---

# 8. Final Principle

> Deployment outputs create traceability from release intention to verified runtime behavior.