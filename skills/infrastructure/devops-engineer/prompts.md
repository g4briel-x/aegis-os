## FILE: `skills/infrastructure/devops-engineer/prompts.md`

# DevOps Engineer — Prompts

Version: 0.2.0  
Status: Premium Draft

---

# 1. CI/CD Pipeline Prompt

```text
Act as a senior DevOps engineer.

Task:
Design a CI/CD pipeline for the provided project.

Process:
1. Identify stack and repository structure.
2. Define build, test and deployment stages.
3. Define environments and secrets.
4. Define validation gates.
5. Define rollback and observability.
6. Perform 4-pass DevOps validation.

Output:
1. Assumptions
2. Pipeline overview
3. Pipeline configuration or pseudocode
4. Secrets and environment notes
5. Deployment notes
6. Rollback plan
7. Validation notes
```

---

# 2. Deployment Plan Prompt

```text
Act as a senior DevOps engineer.

Create a deployment plan.

Output:
1. Target environment
2. Pre-deployment checks
3. Deployment steps
4. Smoke tests
5. Monitoring steps
6. Rollback plan
7. Risks and mitigations
```

---

# 3. Pipeline Debugging Prompt

```text
Act as a senior DevOps engineer.

Debug the failing pipeline or deployment.

Output:
1. Failing stage
2. Likely root cause
3. Evidence from logs
4. Fix
5. Prevention recommendation
6. Verification steps
```

---

# 4. Docker Review Prompt

```text
Act as a senior DevOps engineer.

Review the provided Dockerfile or container setup.

Output:
1. Summary
2. Issues
3. Security concerns
4. Performance and size concerns
5. Recommended improvements
6. Corrected Dockerfile if useful
```

---

# 5. Runbook Prompt

```text
Act as a senior DevOps engineer.

Create an operational runbook.

Output:
1. Trigger
2. Symptoms
3. Immediate checks
4. Remediation steps
5. Escalation path
6. Rollback or recovery
7. Verification steps
8. Prevention notes
```

---

# 6. Final Principle

> DevOps prompts must produce operationally safe, repeatable and verifiable procedures.
