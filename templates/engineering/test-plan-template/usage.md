## FILE: `templates/engineering/test-plan-template/usage.md`

# Test Plan Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Identify the change being tested
2. Link PRD, API contract or design references
3. Define test scope and non-scope
4. Define test objectives
5. Select test strategy
6. Prepare test environment and data
7. Write functional, API, security and edge cases
8. Map acceptance criteria to tests
9. Define automation and manual coverage
10. Confirm entry and exit criteria
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Engineering review
QA review
Product review
Security review if sensitive
Operations review if release risk exists
```

---

# 3. Writing Rules

A Test Plan should:

- map to requirements;
- include negative cases;
- include security cases when access control matters;
- define test data;
- identify manual and automated tests;
- define clear exit criteria.

---

# 4. Test Case Rule

Use clear Given / When / Then format.

Example:

```text
Given a project is missing required documents
When the creator attempts to submit the project
Then submission is blocked and the missing documents are listed.
```

---

# 5. Final Principle

> Use the Test Plan Template to reduce release uncertainty before testing starts.
