## FILE: `skills/infrastructure/cloud-architect/workflows.md`

# Cloud Architect — Workflows

Version: 0.2.0  
Status: Premium Draft

---

# 1. Cloud Architecture Design Workflow

Use this workflow when designing new cloud infrastructure.

```text
1. Understand product and workload goals
2. Identify cloud provider and constraints
3. Define environments
4. Select compute, storage and database services
5. Define networking and access boundaries
6. Define deployment topology
7. Define observability and recovery
8. Validate cost, security and reliability
```

---

# 2. SaaS Infrastructure Workflow

Use this workflow when designing SaaS cloud architecture.

```text
1. Define tenant model
2. Define user and access model
3. Define application services
4. Define database and storage model
5. Define isolation and security boundaries
6. Define scaling path
7. Define monitoring and support needs
8. Define cost and growth assumptions
```

---

# 3. Cloud Review Workflow

Use this workflow when reviewing an existing cloud setup.

```text
1. Understand current infrastructure
2. Identify workload requirements
3. Review network exposure
4. Review IAM and secrets
5. Review reliability and backups
6. Review observability
7. Review cost risks
8. Recommend prioritized improvements
```

---

# 4. Migration Workflow

Use this workflow for moving a system to the cloud.

```text
1. Assess current system
2. Define migration goals
3. Identify dependencies
4. Select migration strategy
5. Plan data migration
6. Define cutover and rollback
7. Validate performance and security
8. Document migration risks
```

---

# 5. Disaster Recovery Workflow

Use this workflow when defining recovery plans.

```text
1. Identify critical services
2. Define recovery objectives
3. Define backup strategy
4. Define failover strategy
5. Define restore procedure
6. Define verification steps
7. Define incident communication
8. Review regularly
```

---

# 6. 4-Pass Cloud Validation Workflow

Every cloud architecture output must be reviewed using this workflow:

```text
Pass 1 — Requirement, workload and environment alignment
Pass 2 — Architecture, networking and dependency review
Pass 3 — Security, identity and compliance review
Pass 4 — Cost, reliability, observability and recovery readiness review
```

---

# 7. Final Principle

> Cloud design is complete only when deployment, security, operations, cost and recovery are all addressed.