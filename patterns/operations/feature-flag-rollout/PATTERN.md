## FILE: `patterns/operations/feature-flag-rollout/PATTERN.md`

# Feature Flag Rollout Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS team needs to release features safely without exposing all users to unvalidated behavior.

Direct release creates:

- large blast radius;
- slow recovery;
- difficult beta testing;
- limited observability;
- mixed deployment and launch decisions;
- pressure to hotfix when behavior fails.

---

# 2. Context

This Pattern applies when a feature can be deployed in code but activated separately.

Typical contexts:

```text
new dashboard
billing change
new onboarding flow
new permissions model
AI-powered feature
file upload feature
major UI redesign
new API behavior
enterprise beta
```

---

# 3. Forces

Key forces:

```text
speed versus safety
deployment simplicity versus runtime control
product learning versus operational complexity
beta access versus general availability
fast rollback versus flag sprawl
experimentation versus maintainability
```

---

# 4. Recommended Model

A feature flag should have:

```text
id
name
description
owner
default_state
targeting_rule
rollout_percentage
start_date
review_date
expiration_date
monitoring_signals
rollback_trigger
cleanup_plan
```

---

# 5. Flag Types

Common flag types:

```text
release_flag
experiment_flag
permission_flag
ops_kill_switch
beta_access_flag
migration_flag
```

Use the simplest type that solves the rollout problem.

---

# 6. Rollout Stages

Recommended staged rollout:

```text
0% internal only
1% staff or test tenant
5% beta users
25% selected customers
50% wider release
100% general availability
cleanup flag
```

Each stage should have explicit success criteria.

---

# 7. Monitoring

Monitor before increasing rollout.

Signals:

```text
error rate
latency
conversion
activation
support tickets
user feedback
database load
security events
business metric impact
```

---

# 8. Rollback

Rollback should be possible by changing the flag state.

Rollback triggers:

```text
critical workflow failure
error rate above threshold
latency above threshold
support spike
data integrity issue
security concern
negative business impact
```

---

# 9. Cleanup

Every flag must have a cleanup plan.

Cleanup includes:

- remove old code path;
- remove flag config;
- remove dead tests;
- update documentation;
- remove rollout dashboards if obsolete;
- close tracking task.

---

# 10. Final Principle

> A feature flag is temporary release infrastructure, not a permanent product architecture.
