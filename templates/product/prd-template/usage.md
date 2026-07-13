## FILE: `templates/product/prd-template/usage.md`

# PRD Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define feature name and owner
2. Write the problem statement
3. Define goals and non-goals
4. Identify target users
5. Map use cases and user journey
6. Write functional requirements
7. Write acceptance criteria
8. Add UX, data, API and security requirements
9. Define success metrics
10. Review dependencies, risks and release plan
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Product review
Design review
Engineering review
Security review if relevant
Operations review if release risk exists
Stakeholder approval
```

---

# 3. Writing Rules

The PRD should:

- be specific;
- avoid vague requirements;
- separate goals from solutions;
- make non-goals explicit;
- include testable acceptance criteria;
- define success metrics;
- state open questions clearly.

---

# 4. Requirement Quality Rule

A strong requirement is:

```text
specific
testable
owned
relevant to the user problem
not mixed with unrelated requirements
```

Weak:

```text
The feature should be easy to use.
```

Better:

```text
The user must be able to submit a completed project in fewer than five required steps after all mandatory fields are filled.
```

---

# 5. Acceptance Criteria Rule

Use:

```text
Given / When / Then
```

Example:

```text
Given a project is missing required documents
When the creator attempts to submit it
Then the system prevents submission and displays the missing document list.
```

---

# 6. Final Principle

> Use the PRD Template to align decisions before design and implementation, not to document decisions after the fact.
