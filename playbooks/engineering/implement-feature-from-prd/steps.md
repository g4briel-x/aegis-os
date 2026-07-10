## FILE: `playbooks/engineering/implement-feature-from-prd/steps.md`

# Implement Feature From PRD — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Review PRD and Acceptance Criteria

Read the PRD before implementation planning.

Check:

- problem statement;
- goals and non-goals;
- user stories;
- functional requirements;
- non-functional requirements;
- acceptance criteria;
- metrics;
- risks and open questions.

Output:

```text
PRD implementation readiness summary
```

---

# 2. Step 2 — Identify Affected System Areas

Map the feature to system areas.

Review:

- frontend screens;
- backend services;
- APIs;
- database tables;
- authentication;
- authorization;
- notifications;
- files or storage;
- background jobs;
- configuration;
- documentation.

Output:

```text
Affected component list
```

---

# 3. Step 3 — Define Technical Approach

Define how the feature will be built.

Capture:

- implementation pattern;
- architecture alignment;
- reuse opportunities;
- new components;
- refactoring needs;
- trade-offs;
- assumptions.

Output:

```text
Technical approach summary
```

---

# 4. Step 4 — Break Work Into Technical Tasks

Convert requirements into executable tasks.

Task types may include:

- schema updates;
- API creation or update;
- service logic;
- frontend components;
- form validation;
- permission checks;
- tests;
- documentation;
- deployment configuration.

Output:

```text
Technical task breakdown
```

---

# 5. Step 5 — Define Data Changes

Identify data model and persistence impact.

Check:

- new entities;
- new fields;
- migrations;
- constraints;
- indexes;
- data validation;
- ownership model;
- tenant scoping;
- audit needs.

Output:

```text
Data change summary
```

---

# 6. Step 6 — Define API Changes

Identify endpoint and contract changes.

Capture:

- endpoint;
- method;
- request schema;
- response schema;
- authentication;
- authorization;
- validation;
- error handling;
- versioning impact.

Output:

```text
API change summary
```

---

# 7. Step 7 — Define UI and UX Changes

Map requirements to screens and states.

Review:

- screen changes;
- user actions;
- loading states;
- empty states;
- error states;
- success states;
- permission states;
- accessibility considerations.

Output:

```text
UI implementation summary
```

---

# 8. Step 8 — Review Security and Permissions

Check security-sensitive behavior.

Review:

- authentication requirements;
- role permissions;
- object-level authorization;
- tenant boundaries;
- sensitive data exposure;
- file access;
- audit logging;
- abuse risk.

Output:

```text
Security implementation notes
```

---

# 9. Step 9 — Define Tests and Validation

Convert acceptance criteria into verification.

Test coverage may include:

- unit tests;
- integration tests;
- API tests;
- UI tests;
- permission tests;
- regression tests;
- manual QA checklist.

Output:

```text
Test and validation plan
```

---

# 10. Step 10 — Prepare Pull Request and Release Handoff

Prepare the change for review and release.

Include:

- PR summary;
- changed areas;
- test evidence;
- screenshots if UI changed;
- risk notes;
- migration notes;
- rollback notes;
- documentation updates.

Output:

```text
Pull request and release handoff notes
```

---

# 11. Final Principle

> Implementation steps should preserve traceability from requirement to code to test.
