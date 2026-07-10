## FILE: `playbooks/engineering/review-pull-request/checklists.md`

# Review Pull Request — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. PR Context Checklist

```text
[ ] PR purpose is clear
[ ] Linked requirement or issue exists
[ ] Expected behavior is described
[ ] Scope is focused
[ ] Non-goals are clear
[ ] Reviewer has enough context
```

---

# 2. Correctness Checklist

```text
[ ] Main logic reviewed
[ ] Edge cases reviewed
[ ] Error handling reviewed
[ ] Input validation reviewed
[ ] State transitions reviewed
[ ] Failure paths reviewed
[ ] Regression risk considered
```

---

# 3. Architecture Checklist

```text
[ ] Code is readable
[ ] Naming is clear
[ ] Responsibilities are separated
[ ] Duplication is acceptable or reduced
[ ] Dependencies are appropriate
[ ] Complexity is justified
[ ] Existing patterns are respected
```

---

# 4. Security Checklist

```text
[ ] Authentication impact reviewed
[ ] Authorization impact reviewed
[ ] Object ownership reviewed
[ ] Tenant isolation reviewed if relevant
[ ] Sensitive data exposure reviewed
[ ] Secrets not exposed
[ ] Audit logging considered
```

---

# 5. Test Checklist

```text
[ ] Unit tests reviewed
[ ] Integration tests reviewed if relevant
[ ] API tests reviewed if relevant
[ ] UI tests reviewed if relevant
[ ] Permission tests reviewed if relevant
[ ] CI is passing or failure is explained
[ ] Manual validation documented if needed
```

---

# 6. Release Checklist

```text
[ ] Migration notes included if needed
[ ] Environment variable changes documented
[ ] Deployment impact reviewed
[ ] Rollback notes included if needed
[ ] Documentation updated if needed
[ ] Monitoring impact considered
```

---

# 7. Final Principle

> PR checklists prevent review from becoming a quick glance at code instead of a quality gate.
