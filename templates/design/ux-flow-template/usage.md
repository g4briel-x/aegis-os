## FILE: `templates/design/ux-flow-template/usage.md`

# UX Flow Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define the user and goal
2. Define entry and exit points
3. Map the main happy path
4. Define screens and required elements
5. Define empty, loading, success and error states
6. Define permissions and data behavior
7. Add analytics and side effects
8. Add edge cases
9. Add acceptance criteria
10. Review with product, design, engineering and QA
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Product review
UX/UI review
Engineering review
Security review if access or sensitive data matters
QA review
Final approval
```

---

# 3. Writing Rules

A UX Flow should:

- focus on one workflow;
- describe user action and system response;
- include states;
- include error behavior;
- define permissions;
- include analytics;
- be specific enough for design and QA.

---

# 4. Flow Rule

Weak:

```text
User creates a project.
```

Better:

```text
Given a new user is on the empty dashboard, when they click Create Project, the system opens the project setup screen with required title and project type fields.
```

---

# 5. Final Principle

> Use the UX Flow Template before creating high-fidelity screens so the structure is correct first.
