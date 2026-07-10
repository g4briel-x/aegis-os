## FILE: `playbooks/engineering/review-pull-request/steps.md`

# Review Pull Request — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Understand PR Purpose

Start by identifying why the PR exists.

Capture:

- feature, fix or refactor;
- linked issue, PRD or incident;
- expected behavior;
- non-goals;
- release urgency.

Output:

```text
PR purpose summary
```

---

# 2. Step 2 — Confirm Requirement Alignment

Check whether the change matches the requirement.

Review:

- user story;
- acceptance criteria;
- bug reproduction case;
- expected behavior;
- product constraints;
- excluded scope.

Output:

```text
Requirement alignment notes
```

---

# 3. Step 3 — Review Scope and Changed Files

Check whether the PR changes only what it should.

Review:

- changed files;
- new files;
- deleted files;
- configuration changes;
- dependency changes;
- generated files;
- unrelated refactors.

Output:

```text
Scope review findings
```

---

# 4. Step 4 — Review Correctness

Review whether the code behaves correctly.

Check:

- logic correctness;
- edge cases;
- error handling;
- state transitions;
- validation;
- concurrency or async behavior;
- null or missing data;
- failure paths.

Output:

```text
Correctness findings
```

---

# 5. Step 5 — Review Architecture and Maintainability

Check whether the implementation fits the system.

Review:

- separation of concerns;
- naming;
- duplication;
- dependency direction;
- domain boundaries;
- complexity;
- readability;
- future change risk.

Output:

```text
Architecture and maintainability findings
```

---

# 6. Step 6 — Review Security and Data Impact

Check security-sensitive behavior.

Review:

- authentication;
- authorization;
- object ownership;
- tenant isolation;
- sensitive data exposure;
- secrets;
- input validation;
- file access;
- audit logging.

Output:

```text
Security and data findings
```

---

# 7. Step 7 — Review Tests and CI

Check whether the PR is validated.

Review:

- unit tests;
- integration tests;
- API tests;
- UI tests;
- permission tests;
- regression tests;
- CI status;
- flaky or skipped tests.

Output:

```text
Test and CI findings
```

---

# 8. Step 8 — Review Performance and Reliability

Check operational impact.

Review:

- database query efficiency;
- indexes;
- external calls;
- timeouts;
- retries;
- background jobs;
- memory or CPU impact;
- logging and monitoring.

Output:

```text
Performance and reliability findings
```

---

# 9. Step 9 — Review Documentation and Release Notes

Check whether supporting documentation is ready.

Review:

- README updates;
- API docs;
- migration notes;
- environment variable notes;
- release notes;
- rollback notes;
- user-facing documentation.

Output:

```text
Documentation and release findings
```

---

# 10. Step 10 — Record Merge Decision

Decide and document the review outcome.

Possible decisions:

```text
approve
request_changes
comment_only
block_merge
needs_specialist_review
```

Output:

```text
Merge readiness decision
```

---

# 11. Final Principle

> PR review steps should make hidden risk visible before merge.
