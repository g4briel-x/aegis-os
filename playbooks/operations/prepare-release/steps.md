## FILE: `playbooks/operations/prepare-release/steps.md`

# Prepare Release — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Confirm Release Scope

Define exactly what is included in the release.

Capture:

- release name;
- release objective;
- included features;
- included fixes;
- excluded items;
- affected services;
- target environment.

Output:

```text
Release scope summary
```

---

# 2. Step 2 — Confirm Acceptance Criteria

Verify that the release has clear completion expectations.

Check:

- product acceptance criteria;
- engineering definition of done;
- QA criteria;
- security criteria;
- operational readiness criteria.

Output:

```text
Acceptance readiness summary
```

---

# 3. Step 3 — Review Code and Tests

Confirm the technical implementation is ready.

Review:

- pull request status;
- code review status;
- unit test results;
- integration test results;
- end-to-end test results;
- lint or static analysis results;
- unresolved defects.

Output:

```text
Code and test readiness summary
```

---

# 4. Step 4 — Review Data and Compatibility Impact

Identify whether the release affects data, schemas, APIs or compatibility.

Check:

- database migrations;
- backward compatibility;
- API version changes;
- data transformations;
- migration rollback;
- customer data risk.

Output:

```text
Data and compatibility impact summary
```

---

# 5. Step 5 — Review Security Impact

Confirm security-sensitive changes are reviewed.

Check:

- authentication changes;
- authorization changes;
- secrets or credentials;
- payment or billing logic;
- sensitive data exposure;
- new public endpoints;
- dependency vulnerabilities.

Output:

```text
Security readiness summary
```

---

# 6. Step 6 — Confirm Deployment Plan

Define how the release will be deployed.

Capture:

- deployment owner;
- deployment steps;
- target environment;
- deployment time;
- required approvals;
- feature flags;
- smoke tests;
- expected deployment duration.

Output:

```text
Deployment plan
```

---

# 7. Step 7 — Confirm Rollback Plan

Define how to safely reverse or mitigate the release.

Capture:

- rollback trigger;
- rollback steps;
- rollback owner;
- data rollback constraints;
- feature disablement option;
- expected rollback duration.

Output:

```text
Rollback plan
```

---

# 8. Step 8 — Prepare Communication

Define who needs to know about the release.

Prepare:

- internal release note;
- stakeholder update;
- customer-facing note if needed;
- support briefing;
- known issues;
- escalation contacts.

Output:

```text
Communication plan
```

---

# 9. Step 9 — Define Post-Release Monitoring

Define what to watch after deployment.

Monitor:

- error rate;
- latency;
- logs;
- critical user flows;
- business metrics;
- support tickets;
- payment or auth behavior if affected.

Output:

```text
Post-release monitoring plan
```

---

# 10. Step 10 — Record Go / No-Go Decision

Make the release decision based on evidence.

Record:

- decision;
- approver;
- conditions;
- unresolved risks;
- next action.

Output:

```text
Go / no-go decision record
```

---

# 11. Final Principle

> Release preparation is the discipline of making risk visible before production feels it.