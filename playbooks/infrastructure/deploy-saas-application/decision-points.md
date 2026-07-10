## FILE: `playbooks/infrastructure/deploy-saas-application/decision-points.md`

# Deploy SaaS Application — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Build Deployable?

```yaml
decision_point:
  question: Have required checks passed for the deployment candidate?
  options:
    - yes
    - no
    - exception_requested
  criteria:
    - CI checks
    - tests
    - build artifact
    - code review
    - release approval
  recommended_action:
    yes: continue deployment preparation.
    no: block deployment.
    exception_requested: require explicit owner approval and risk note.
  fallback: delay deployment until required checks pass.
```

---

# 2. Decision Point — Are Secrets and Configuration Ready?

```yaml
decision_point:
  question: Are all required secrets and environment variables available for the target environment?
  options:
    - yes
    - no
    - unclear
  criteria:
    - required secret names
    - environment variables
    - service URLs
    - deployment permissions
    - runtime configuration
  recommended_action:
    yes: continue.
    no: block deployment until fixed.
    unclear: verify configuration before deployment.
  fallback: deploy only to staging or postpone.
```

---

# 3. Decision Point — Is Migration Risk Acceptable?

```yaml
decision_point:
  question: Is the migration or data impact safe enough to proceed?
  options:
    - yes
    - no
    - requires_review
  criteria:
    - migration reversibility
    - destructive change
    - backup status
    - data compatibility
    - customer impact
  recommended_action:
    yes: proceed with migration plan.
    no: block deployment.
    requires_review: involve Database Engineer or Software Architect Skill.
  fallback: split migration from application deployment.
```

---

# 4. Decision Point — Did Smoke Tests Pass?

```yaml
decision_point:
  question: Did critical smoke tests pass after deployment?
  options:
    - yes
    - no
    - partially
  criteria:
    - app load
    - login
    - critical API
    - critical workflow
    - affected feature
  recommended_action:
    yes: continue monitoring.
    no: trigger rollback or hotfix decision.
    partially: assess user impact and monitor closely.
  fallback: rollback if critical workflow is broken.
```

---

# 5. Decision Point — Should Rollback Be Triggered?

```yaml
decision_point:
  question: Should the deployment be rolled back?
  options:
    - rollback
    - monitor
    - hotfix
    - escalate
  criteria:
    - error rate
    - user impact
    - data risk
    - security risk
    - failed smoke tests
    - rollback feasibility
  recommended_action:
    rollback: execute rollback plan.
    monitor: continue observation within defined window.
    hotfix: apply only if safe and faster than rollback.
    escalate: involve owners if risk is high.
  fallback: prioritize user impact reduction.
```

---

# 6. Final Principle

> Deployment decisions should favor recovery and user safety over pride in the release.
