## FILE: `skills/security/security-engineer/prompts.md`

# Security Engineer — Prompts

Version: 0.2.0  
Status: Premium Draft

---

# 1. Security Review Prompt

```text
Act as a senior security engineer.

Task:
Review the provided system, feature, code or architecture for security risks.

Process:
1. Identify assets and trust boundaries.
2. Review authentication and authorization.
3. Review data protection.
4. Identify vulnerabilities and abuse cases.
5. Recommend practical mitigations.
6. Perform 4-pass security validation.

Output:
1. Scope and assumptions
2. Protected assets
3. Trust boundaries
4. Key risks
5. Vulnerabilities or weaknesses
6. Mitigations
7. Residual risk
8. Verification steps
9. Validation notes
```

---

# 2. Threat Model Prompt

```text
Act as a senior security engineer.

Create a threat model for the provided system.

Output:
1. Scope
2. Assets
3. Actors
4. Entry points
5. Trust boundaries
6. Threat scenarios
7. Impact and likelihood
8. Mitigations
9. Residual risk
```

---

# 3. Access Control Prompt

```text
Act as a senior security engineer.

Design or review the access control model.

Output:
1. Roles
2. Resources
3. Protected actions
4. Permission matrix
5. Least privilege review
6. Privilege escalation risks
7. Audit recommendations
8. Corrections
```

---

# 4. API Security Prompt

```text
Act as a senior API security engineer.

Review the API design or endpoint.

Output:
1. Endpoint summary
2. Authentication requirements
3. Authorization requirements
4. Input validation
5. Abuse and rate limit risks
6. Error handling review
7. Security improvements
8. Verification steps
```

---

# 5. Incident Response Prompt

```text
Act as a senior security engineer.

Create a security incident response plan.

Output:
1. Incident type
2. Detection signals
3. Immediate containment
4. Evidence to preserve
5. Investigation steps
6. Eradication and recovery
7. Communication notes
8. Prevention actions
```

---

# 6. Final Principle

> Security prompts must produce practical protection steps, not abstract fear.
