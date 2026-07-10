## FILE: `playbooks/security/harden-production-saas/outputs.md`

# Harden Production SaaS — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Production Hardening Report

Purpose:

Summarize production security readiness.

Required sections:

```text
Application:
Environment:
Review scope:
Overall readiness:
Blockers:
High risks:
Accepted risks:
Decision:
```

---

# 2. Access Control Finding

Purpose:

Document identity or permission issues.

Required sections:

```text
Finding:
Affected role:
Affected resource:
Risk:
Evidence:
Recommendation:
Priority:
```

---

# 3. Tenant Isolation Finding

Purpose:

Document customer boundary risks.

Required sections:

```text
Resource:
Boundary:
Issue:
Impact:
Evidence:
Required fix:
```

---

# 4. Secrets and Configuration Finding

Purpose:

Document configuration security gaps.

Required sections:

```text
Secret or setting:
Environment:
Issue:
Exposure risk:
Recommended action:
Owner:
```

---

# 5. API Exposure Finding

Purpose:

Document public or API attack surface risks.

Required sections:

```text
Endpoint or surface:
Issue:
Risk:
Required protection:
Verification:
```

---

# 6. Remediation Plan

Purpose:

Prioritize hardening actions.

Required sections:

```text
Action:
Priority:
Owner:
Due date:
Verification method:
Status:
```

---

# 7. Readiness Decision

Purpose:

Record launch or production status.

Required sections:

```text
Decision:
Reason:
Blockers:
Accepted risks:
Required approvals:
Monitoring requirements:
```

---

# 8. Final Principle

> Hardening outputs must clearly distinguish blockers, accepted risks and verified controls.

---