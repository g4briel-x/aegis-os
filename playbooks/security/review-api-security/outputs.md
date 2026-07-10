## FILE: `playbooks/security/review-api-security/outputs.md`

# Review API Security — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. API Security Review

Purpose:

Summarize the security posture of the API under review.

Required sections:

```text
API scope:
Protected assets:
Authentication review:
Authorization review:
Validation review:
Data exposure review:
Abuse controls:
Logging and audit:
```

---

# 2. Authorization Matrix

Purpose:

Clarify which roles can perform which actions.

Required sections:

```text
Role:
Resource:
Action:
Allowed:
Condition:
Notes:
```

---

# 3. Risk List

Purpose:

List API security issues found during review.

Required sections:

```text
Risk:
Endpoint:
Severity:
Impact:
Likelihood:
Evidence:
```

---

# 4. Mitigation Plan

Purpose:

Define practical corrections.

Required sections:

```text
Issue:
Mitigation:
Owner:
Priority:
Verification:
Residual risk:
```

---

# 5. Verification Checklist

Purpose:

Confirm that security controls are implemented correctly.

Required sections:

```text
Control:
Test:
Expected result:
Status:
Evidence:
```

---

# 6. Final Principle

> API security outputs must be specific enough for engineers to fix and reviewers to verify.
