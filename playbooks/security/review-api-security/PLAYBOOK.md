## FILE: `playbooks/security/review-api-security/PLAYBOOK.md`

# Review API Security — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured security review of an API endpoint, API group or API integration.

---

# 2. Trigger

An API is being created, changed, exposed, audited or suspected of creating security risk.

---

# 3. Inputs

Useful inputs include:

- API endpoint list;
- HTTP methods;
- request schema;
- response schema;
- authentication mechanism;
- authorization rules;
- user roles;
- data model;
- error responses;
- rate limiting rules;
- logs or audit requirements;
- deployment context.

---

# 4. Outputs

Expected outputs include:

- API security review;
- risk list;
- authorization matrix;
- validation findings;
- data exposure findings;
- abuse and rate limit findings;
- mitigation plan;
- verification checklist.

---

# 5. Execution Summary

```text
1. Define API review scope
2. Identify assets and sensitive data
3. Review authentication
4. Review authorization
5. Review input validation
6. Review output and data exposure
7. Review abuse controls and rate limits
8. Review errors, logging and audit
9. Prioritize risks
10. Define mitigations and verification steps
```

---

# 6. Completion Criteria

The Playbook is complete when:

- API scope is documented;
- protected resources are identified;
- authentication and authorization are reviewed;
- input and output risks are documented;
- security risks are prioritized;
- mitigations are defined;
- verification steps are clear.

---

# 7. Escalation or Fallback

Escalate when:

- sensitive data exposure is possible;
- authorization is unclear;
- authentication is missing or weak;
- tenant boundaries are not enforced;
- public exposure is high-risk;
- payment, identity or financial data is involved;
- exploitation evidence exists.

---

# 8. Final Principle

> An API is secure only when access, data, behavior and observability are all intentionally controlled.