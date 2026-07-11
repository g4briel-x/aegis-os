## FILE: `patterns/operations/feature-flag-rollout/checklists.md`

# Feature Flag Rollout — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Feature has meaningful user impact
[ ] Gradual rollout is useful
[ ] Rollback without redeploy is valuable
[ ] Target audience can be identified
[ ] Monitoring signals are available
[ ] Flag owner is assigned
```

---

# 2. Flag Definition Checklist

```text
[ ] Flag id is clear
[ ] Flag type is defined
[ ] Owner is assigned
[ ] Default state is defined
[ ] Targeting rules are defined
[ ] Rollout stages are defined
[ ] Expiration date is defined
```

---

# 3. Testing Checklist

```text
[ ] Flag-off behavior tested
[ ] Flag-on behavior tested
[ ] Targeted access tested
[ ] Non-targeted access tested
[ ] Rollback path tested
[ ] Permission behavior tested
[ ] Analytics events tested if needed
```

---

# 4. Monitoring Checklist

```text
[ ] Error rate monitored
[ ] Latency monitored
[ ] Critical workflow monitored
[ ] Support tickets monitored
[ ] User feedback captured
[ ] Business metric tracked
[ ] Rollout decision window defined
```

---

# 5. Rollback Checklist

```text
[ ] Rollback trigger defined
[ ] Rollback owner assigned
[ ] Flag-off action documented
[ ] Verification checks defined
[ ] Communication path defined
[ ] Follow-up issue process defined
```

---

# 6. Cleanup Checklist

```text
[ ] Cleanup task created
[ ] Expiration date assigned
[ ] Old code path removal planned
[ ] Tests update planned
[ ] Documentation update planned
[ ] Flag deletion owner assigned
```

---

# 7. Final Principle

> Feature flag checklists keep rollout control from becoming rollout chaos.
