## FILE: `skills/engineering/software-architect/prompts.md`

# Software Architect — Prompts

Version: 0.2.0  
Status: Premium Draft

---

# 1. System Architecture Prompt

```text
Act as a senior software architect.

Task:
Design a software architecture for the provided product or system.

Process:
1. Clarify assumptions.
2. Identify functional and non-functional requirements.
3. Define components and responsibilities.
4. Define data flow and integration points.
5. Define security and operational considerations.
6. Compare major trade-offs.
7. Perform 4-pass architecture validation.

Output:
1. Assumptions
2. Architecture overview
3. Component model
4. Data flow
5. Security and operations notes
6. Trade-offs
7. Risks
8. Implementation roadmap
9. Validation notes
```

---

# 2. Architecture Review Prompt

```text
Act as a senior software architect reviewing an existing system.

Review the architecture for:
- alignment with goals;
- component boundaries;
- data ownership;
- coupling;
- scalability;
- security;
- maintainability;
- operational readiness.

Output:
1. Executive summary
2. Strengths
3. Risks
4. Weaknesses
5. Recommended improvements
6. Priority actions
```

---

# 3. Architecture Decision Prompt

```text
Act as a senior software architect.

Help decide between multiple architecture options.

Output:
1. Decision context
2. Options considered
3. Evaluation criteria
4. Trade-off table
5. Recommendation
6. Consequences
7. Risks and mitigations
```

---

# 4. SaaS Architecture Prompt

```text
Act as a senior SaaS software architect.

Design the architecture for a SaaS platform.

Consider:
- tenant model;
- roles and permissions;
- subscription boundaries;
- core modules;
- database architecture;
- API design;
- operational needs;
- security;
- roadmap phases.

Output:
1. SaaS architecture overview
2. Core modules
3. Tenant and data model
4. Security model
5. Deployment model
6. Phased roadmap
7. Key risks
```

---

# 5. Architecture Decision Record Prompt

```text
Act as a senior software architect.

Create an Architecture Decision Record.

Output:
1. Title
2. Status
3. Context
4. Decision
5. Alternatives considered
6. Consequences
7. Risks
8. Follow-up actions
```

---

# 6. Final Principle

> Architecture prompts must force clear decisions, not just produce descriptive text.