## FILE: `playbooks/infrastructure/fix-failing-ci-pipeline/checklists.md`

# Fix Failing CI Pipeline — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Failure Intake Checklist

```text
[ ] Workflow name captured
[ ] Failed job captured
[ ] Failed step captured
[ ] Branch captured
[ ] Commit captured
[ ] Trigger event captured
[ ] Primary error captured
[ ] Failure category identified
```

---

# 2. Log Review Checklist

```text
[ ] First meaningful error identified
[ ] Final error reviewed
[ ] Stack trace reviewed if present
[ ] Failed command identified
[ ] Missing dependency or command checked
[ ] Permission error checked
[ ] Environment variable error checked
```

---

# 3. Environment Checklist

```text
[ ] Runtime version checked
[ ] Package manager version checked
[ ] Lockfile checked
[ ] Operating system checked
[ ] Working directory checked
[ ] Environment variables checked
[ ] Cache behavior checked
```

---

# 4. Fix Checklist

```text
[ ] Root cause identified
[ ] Minimal safe fix selected
[ ] Fix avoids exposing secrets
[ ] Fix does not bypass required checks
[ ] Side effects considered
[ ] Related documentation updated if needed
```

---

# 5. Verification Checklist

```text
[ ] Failed command rerun locally if possible
[ ] Failed CI job rerun
[ ] Required checks pass
[ ] Downstream jobs reviewed
[ ] Deployment preview checked if relevant
[ ] Merge readiness updated
```

---

# 6. Prevention Checklist

```text
[ ] Runtime versions pinned if needed
[ ] CI configuration clarified
[ ] Required secrets documented without values
[ ] Flaky test tracked if relevant
[ ] Contributor instructions updated if needed
[ ] Prevention owner assigned
```

---

# 7. Final Principle

> CI checklists make build failures easier to fix and harder to repeat.
