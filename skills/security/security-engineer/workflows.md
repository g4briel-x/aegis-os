## FILE: `skills/security/security-engineer/workflows.md`

# Security Engineer — Workflows

Version: 0.2.0  
Status: Premium Draft

---

# 1. Security Review Workflow

Use this workflow when reviewing a system, feature or implementation.

```text
1. Understand the system purpose
2. Identify protected assets
3. Identify users and actors
4. Identify trust boundaries
5. Review authentication and authorization
6. Review data protection
7. Identify vulnerabilities and abuse cases
8. Recommend mitigations and verification steps
```

---

# 2. Threat Modeling Workflow

Use this workflow when analyzing a system design.

```text
1. Define scope
2. Identify assets
3. Identify actors
4. Identify entry points
5. Identify trust boundaries
6. Enumerate threats
7. Rate impact and likelihood
8. Define mitigations and residual risk
```

---

# 3. Access Control Review Workflow

Use this workflow when reviewing roles and permissions.

```text
1. Identify user roles
2. Identify protected actions
3. Identify protected resources
4. Map permissions to roles
5. Check least privilege
6. Check privilege escalation paths
7. Check audit requirements
8. Recommend corrections
```

---

# 4. Secure Coding Review Workflow

Use this workflow when reviewing code.

```text
1. Understand code purpose
2. Review inputs and validation
3. Review authentication checks
4. Review authorization checks
5. Review error handling
6. Review secrets and sensitive data
7. Review dependency and configuration risks
8. Provide secure corrections
```

---

# 5. Incident Response Workflow

Use this workflow when preparing or responding to a security incident.

```text
1. Classify the incident
2. Identify affected assets
3. Contain exposure
4. Preserve evidence
5. Investigate root cause
6. Eradicate the cause
7. Recover safely
8. Define prevention actions
```

---

# 6. 4-Pass Security Validation Workflow

Every major security output must be reviewed using this workflow:

```text
Pass 1 — Asset, scope and threat boundary review
Pass 2 — Authentication, authorization and data protection review
Pass 3 — Vulnerability, exploitability and mitigation review
Pass 4 — Operational, audit and incident-readiness review
```

---

# 7. Final Principle

> Security workflow is complete only when risk, mitigation and verification are all explicit.