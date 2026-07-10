## FILE: `skills/engineering/senior-developer/workflows.md`

# Senior Developer — Workflows

Version: 0.2.0  
Status: Premium Draft

---

# 1. Implementation Workflow

Use this workflow when the user asks for new code.

```text
1. Understand the requirement
2. Identify the target stack
3. Define assumptions
4. Design the solution
5. Write the code
6. Run 4-pass verification
7. Correct detected issues
8. Deliver code with usage notes
```

---

# 2. Debugging Workflow

Use this workflow when the user provides an error, bug or unexpected behavior.

```text
1. Read the error or symptom
2. Identify the execution context
3. Locate the likely failure zone
4. Form hypotheses
5. Suggest checks or inspect code
6. Provide a fix
7. Explain the cause
8. Add prevention guidance
```

---

# 3. Code Review Workflow

Use this workflow when reviewing code.

```text
1. Understand intent
2. Review structure
3. Review correctness
4. Review security
5. Review maintainability
6. Review performance where relevant
7. Identify blocking issues
8. Suggest concrete improvements
```

---

# 4. Refactoring Workflow

Use this workflow when improving existing code.

```text
1. Identify current behavior
2. Preserve expected behavior
3. Detect duplication and complexity
4. Improve naming and structure
5. Isolate responsibilities
6. Add or suggest tests
7. Verify output consistency
```

---

# 5. Database Workflow

Use this workflow for database tasks.

```text
1. Understand data entities
2. Identify relationships
3. Define constraints
4. Design schema or query
5. Review indexing and performance
6. Validate data integrity
7. Provide migration or usage notes
```

---

# 6. Architecture Workflow

Use this workflow for architecture decisions.

```text
1. Clarify business and technical goals
2. Identify constraints
3. Define options
4. Compare trade-offs
5. Recommend architecture
6. Document consequences
7. Identify risks and next steps
```

---

# 7. 4-Pass Code Verification Workflow

Every code output must be reviewed using this workflow:

```text
Pass 1 — Syntax and obvious errors
Pass 2 — Logic, edge cases and runtime behavior
Pass 3 — Security, maintainability and architecture fit
Pass 4 — Final output readiness and usage clarity
```

If an issue is found, correct the code and repeat the relevant review pass.

---

# 8. Final Principle

> The workflow is complete only when the solution has been implemented, reviewed and corrected.