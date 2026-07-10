## FILE: `playbooks/engineering/write-test-plan/steps.md`

# Write Test Plan — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Review Requirements and Acceptance Criteria

Start by understanding what must be validated.

Review:

- product goal;
- user stories;
- functional requirements;
- non-functional requirements;
- acceptance criteria;
- constraints;
- open questions.

Output:

```text
Requirement review summary
```

---

# 2. Step 2 — Define Test Scope and Non-Scope

Clarify what the plan will and will not cover.

Capture:

- included features;
- included workflows;
- affected components;
- excluded areas;
- assumptions;
- test boundaries.

Output:

```text
Test scope definition
```

---

# 3. Step 3 — Identify Risk Areas

Identify what could fail and matter most.

Risk areas may include:

- critical workflow failure;
- data loss;
- incorrect permissions;
- broken API contract;
- invalid validation rules;
- performance degradation;
- regression of existing behavior;
- security exposure.

Output:

```text
Testing risk list
```

---

# 4. Step 4 — Define Test Strategy

Define how testing will be performed.

Consider:

- manual QA;
- unit tests;
- integration tests;
- API tests;
- UI tests;
- end-to-end tests;
- security tests;
- regression tests;
- smoke tests.

Output:

```text
Test strategy
```

---

# 5. Step 5 — Write Functional Test Cases

Create tests for expected behavior.

For each test case, define:

- scenario;
- precondition;
- steps;
- expected result;
- priority;
- evidence required.

Output:

```text
Functional test cases
```

---

# 6. Step 6 — Write Edge and Failure Test Cases

Create tests for non-happy paths.

Examples:

- missing required fields;
- invalid input;
- expired session;
- duplicate submission;
- network error;
- unavailable dependency;
- empty state;
- permission denied.

Output:

```text
Edge and failure test cases
```

---

# 7. Step 7 — Write Permission and Security Test Cases

Create tests for access control and sensitive behavior.

Review:

- role access;
- object ownership;
- tenant isolation;
- admin-only actions;
- sensitive data exposure;
- file access;
- audit events.

Output:

```text
Permission and security test cases
```

---

# 8. Step 8 — Define Regression Coverage

Identify existing behavior that must not break.

Capture:

- related workflows;
- previous bugs;
- shared components;
- API contracts;
- database behavior;
- release-critical paths.

Output:

```text
Regression coverage list
```

---

# 9. Step 9 — Define Test Data and Environment Needs

Identify required data and environment setup.

Capture:

- users and roles;
- test accounts;
- sample records;
- files;
- payments or mock services;
- seeded data;
- environment variables;
- staging requirements.

Output:

```text
Test data and environment requirements
```

---

# 10. Step 10 — Produce Release Validation Checklist

Create the final checklist for merge or release approval.

Include:

- critical tests;
- required evidence;
- owners;
- status;
- blockers;
- final decision.

Output:

```text
Release validation checklist
```

---

# 11. Final Principle

> Test planning should make quality measurable before release pressure begins.