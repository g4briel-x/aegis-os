## FILE: `skills/infrastructure/cloud-architect/prompts.md`

# Cloud Architect — Prompts

Version: 0.2.0  
Status: Premium Draft

---

# 1. Cloud Architecture Prompt

```text
Act as a senior cloud architect.

Task:
Design a cloud architecture for the provided product or workload.

Process:
1. Clarify workload and constraints.
2. Select appropriate cloud services.
3. Define networking and access boundaries.
4. Define deployment topology.
5. Define reliability, observability and recovery.
6. Review cost and security.
7. Perform 4-pass cloud validation.

Output:
1. Assumptions
2. Architecture overview
3. Service selection
4. Deployment topology
5. Security and IAM notes
6. Observability plan
7. Cost considerations
8. Recovery plan
9. Risks
10. Validation notes
```

---

# 2. Cloud Review Prompt

```text
Act as a senior cloud architect.

Review the provided cloud architecture or infrastructure description.

Output:
1. Summary
2. Strengths
3. Risks
4. Security concerns
5. Reliability concerns
6. Cost concerns
7. Priority improvements
8. Validation notes
```

---

# 3. SaaS Cloud Prompt

```text
Act as a senior cloud architect for SaaS platforms.

Design cloud infrastructure for the SaaS product.

Consider:
- tenant model;
- environments;
- application services;
- database and storage;
- identity and access;
- observability;
- backups;
- cost growth.

Output:
1. SaaS cloud architecture
2. Environment model
3. Tenant and data isolation notes
4. Security model
5. Deployment topology
6. Scaling path
7. Cost and reliability risks
```

---

# 4. Migration Prompt

```text
Act as a senior cloud architect.

Create a cloud migration plan.

Output:
1. Current-state assumptions
2. Target cloud architecture
3. Migration strategy
4. Data migration plan
5. Cutover plan
6. Rollback plan
7. Risks and mitigations
8. Validation steps
```

---

# 5. Cost Optimization Prompt

```text
Act as a senior cloud architect.

Review the cloud setup for cost optimization.

Output:
1. Cost drivers
2. Waste risks
3. Optimization opportunities
4. Trade-offs
5. Monitoring recommendations
6. Priority actions
```

---

# 6. Final Principle

> Cloud prompts must produce infrastructure decisions that can be operated, secured and justified.