## FILE: `patterns/operations/feature-flag-rollout/solution.md`

# Feature Flag Rollout — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Separate deployment from activation.

Deployment:

```text
Code exists in production.
Feature remains disabled or limited.
```

Activation:

```text
Flag controls who sees or uses the feature.
Rollout expands only after signals are healthy.
```

---

# 2. Flag Definition

Every flag should be documented.

Example:

```yaml
flag:
  id: project_submission_v2
  name: Project Submission V2
  owner: product-manager-saas
  type: release_flag
  default_state: off
  target_audience: beta_creators
  rollout_percentage: 5
  rollback_trigger: error_rate_above_threshold
  expiration_date: 2026-09-30
```

---

# 3. Targeting Rules

Common targeting methods:

```text
specific users
specific organizations
specific workspaces
beta cohort
percentage rollout
region
plan or tier
internal staff
```

Rules should be simple and documented.

---

# 4. Rollout Plan

Recommended rollout structure:

```text
Stage 1: internal users
Stage 2: selected beta users
Stage 3: 5% of eligible users
Stage 4: 25% of eligible users
Stage 5: 50% of eligible users
Stage 6: 100% rollout
Stage 7: cleanup
```

Each stage should define:

```text
entry criteria
monitoring window
success metrics
rollback criteria
decision owner
```

---

# 5. Monitoring Plan

Before rollout, define monitoring signals.

Example:

```text
feature error rate
API latency
conversion rate
activation completion
support tickets
database query time
authorization failures
user feedback
```

---

# 6. Rollback Plan

Rollback should be fast and simple.

Example:

```text
Set flag to off for all users.
Verify old workflow still works.
Monitor error rate for 30 minutes.
Notify support if users were affected.
Create follow-up issue.
```

---

# 7. Test Strategy

Test both flag states:

```text
flag off
flag on
targeted user on
non-targeted user off
rollback path
permission behavior
analytics events
```

---

# 8. Cleanup Strategy

When the rollout is stable:

```text
remove old code path
remove flag checks
remove flag configuration
update tests
update docs
close rollout task
```

---

# 9. Governance

Feature flags should require:

- owner;
- review date;
- expiration date;
- cleanup task;
- risk level;
- rollout decision log.

---

# 10. Final Principle

> Feature flag rollout should be designed as a temporary control system with observable decisions.
