## FILE: `playbooks/infrastructure/fix-failing-ci-pipeline/decision-points.md`

# Fix Failing CI Pipeline — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Failure Deterministic?

```yaml
decision_point:
  question: Does the same CI failure occur consistently?
  options:
    - yes
    - no
    - unknown
  criteria:
    - repeated failed runs
    - same failed step
    - same error message
    - same test failure
  recommended_action:
    yes: proceed with root cause analysis.
    no: investigate flaky test, runner instability or timing issue.
    unknown: rerun once and compare logs.
  fallback: treat as flaky until evidence proves deterministic failure.
```

---

# 2. Decision Point — Does It Fail Locally?

```yaml
decision_point:
  question: Can the failure be reproduced locally with the same command?
  options:
    - yes
    - no
    - not_tested
  criteria:
    - same command
    - same runtime version
    - same package manager
    - same environment assumptions
  recommended_action:
    yes: debug locally first.
    no: compare CI and local environments.
    not_tested: run the failed command locally if safe.
  fallback: use CI logs as source of truth.
```

---

# 3. Decision Point — Is a Secret or Permission Involved?

```yaml
decision_point:
  question: Does the failed step depend on secrets, tokens, permissions or protected environments?
  options:
    - yes
    - no
    - unclear
  criteria:
    - environment variable error
    - authentication error
    - deployment permission error
    - access denied
    - missing secret
  recommended_action:
    yes: review secret and permission configuration without exposing values.
    no: continue standard CI debugging.
    unclear: inspect workflow and failed step requirements.
  fallback: involve DevOps or Security Engineer Skill.
```

---

# 4. Decision Point — Is the Failure Blocking Release?

```yaml
decision_point:
  question: Is this CI failure blocking a production release or urgent hotfix?
  options:
    - yes
    - no
    - unknown
  criteria:
    - release branch
    - hotfix branch
    - production deployment
    - stakeholder urgency
  recommended_action:
    yes: prioritize safe mitigation and escalation.
    no: proceed with normal correction.
    unknown: clarify release impact.
  fallback: treat as release-blocking until owner confirms otherwise.
```

---

# 5. Decision Point — Is the Pipeline Ready Again?

```yaml
decision_point:
  question: Has the pipeline recovered enough to merge or release?
  options:
    - yes
    - no
    - partially
  criteria:
    - failed job now passes
    - downstream jobs pass
    - required checks pass
    - no hidden skipped checks
  recommended_action:
    yes: record recovery and continue merge or release process.
    no: continue investigation.
    partially: document remaining failing checks and risk.
  fallback: block merge until required checks pass.
```

---

# 6. Final Principle

> CI decision points keep the team from bypassing failures without understanding risk.