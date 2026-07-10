## FILE: `playbooks/security/review-api-security/README.md`

# Review API Security Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Security  
Category: API Security Review

---

# 1. Purpose

The Review API Security Playbook provides a structured procedure for reviewing API endpoints, contracts and integrations for security risks.

It helps identify weaknesses in authentication, authorization, input validation, data exposure, abuse protection, error handling and operational visibility.

---

# 2. Trigger

Use this Playbook when:

- a new API endpoint is being designed;
- an existing API needs security review;
- an API handles sensitive data;
- a public or partner-facing API is being exposed;
- authentication or authorization is being changed;
- an API incident or abuse risk is suspected;
- a release requires security validation.

---

# 3. Scope

This Playbook covers:

- API asset identification;
- authentication review;
- authorization review;
- input validation review;
- data exposure review;
- rate limit and abuse review;
- error handling review;
- logging and audit review;
- mitigation planning.

This Playbook does not replace a full penetration test, but it provides a strong structured security review procedure.

---

# 4. Related Skills

```text
security.security-engineer
engineering.software-architect
engineering.senior-developer
engineering.senior-debugger
infrastructure.devops-engineer
```

---

# 5. Final Principle

> API security must verify who can do what, with which data, under which limits, and with what evidence.