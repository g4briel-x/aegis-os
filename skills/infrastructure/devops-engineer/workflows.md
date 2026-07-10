## FILE: `skills/infrastructure/devops-engineer/workflows.md`

# DevOps Engineer — Workflows

Version: 0.2.0  
Status: Premium Draft

---

# 1. CI/CD Design Workflow

Use this workflow when designing a pipeline.

```text
1. Identify repository and stack
2. Identify build requirements
3. Define test stages
4. Define artifact or package strategy
5. Define deployment environments
6. Define approvals and gates
7. Define notifications
8. Validate rollback and observability
```

---

# 2. Deployment Workflow

Use this workflow when preparing a deployment.

```text
1. Confirm target environment
2. Validate configuration
3. Confirm secrets availability
4. Build or fetch artifact
5. Deploy
6. Run smoke tests
7. Monitor health
8. Confirm rollback path
```

---

# 3. Pipeline Debugging Workflow

Use this workflow when CI/CD fails.

```text
1. Read failure logs
2. Identify failing stage
3. Identify dependency or environment change
4. Form likely root cause
5. Provide fix
6. Add prevention guard if possible
7. Validate with rerun or local reproduction
```

---

# 4. Observability Workflow

Use this workflow when defining monitoring.

```text
1. Identify critical services
2. Define health checks
3. Define key metrics
4. Define logs needed for diagnosis
5. Define alert thresholds
6. Define dashboards
7. Define incident response links
```

---

# 5. Runbook Workflow

Use this workflow when creating operational runbooks.

```text
1. Define trigger
2. Define symptoms
3. Define immediate checks
4. Define remediation steps
5. Define escalation path
6. Define rollback or recovery
7. Define verification steps
8. Document prevention notes
```

---

# 6. 4-Pass DevOps Validation Workflow

Every DevOps output must be reviewed using this workflow:

```text
Pass 1 — Requirement, environment and dependency review
Pass 2 — Automation, repeatability and deployment safety review
Pass 3 — Security, secrets and access control review
Pass 4 — Observability, rollback and operational readiness review
```

---

# 7. Final Principle

> DevOps workflow is complete only when the system can be deployed, observed and recovered safely.