## FILE: `patterns/operations/feature-flag-rollout/trade-offs.md`

# Feature Flag Rollout — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
deployment safety
rollback speed
beta control
experimentation
production learning
blast radius reduction
release confidence
```

---

# 2. Costs

This Pattern adds:

```text
conditional code
test matrix complexity
flag management overhead
cleanup responsibility
possible inconsistent user experience
monitoring requirements
```

---

# 3. Product Trade-Offs

Feature flags allow controlled launches, but can fragment user experience.

Mitigation:

```text
define cohorts clearly
avoid confusing mixed states
communicate beta status
track user feedback by cohort
```

---

# 4. Engineering Trade-Offs

Feature flags reduce release risk but increase code complexity.

Mitigation:

```text
keep flags short-lived
test both paths
remove old paths quickly
avoid nested flag logic
```

---

# 5. Security Trade-Offs

Flags must not bypass authorization.

Bad:

```text
if flag_enabled:
  allow_admin_action
```

Good:

```text
if flag_enabled and user_has_permission:
  allow_action
```

---

# 6. Operational Trade-Offs

Flags make rollback faster, but only if operators know how to use them.

Mitigation:

```text
document rollback action
define owner
include flag in release plan
monitor after changes
```

---

# 7. Final Principle

> The value of a feature flag disappears when the flag becomes unmanaged complexity.
