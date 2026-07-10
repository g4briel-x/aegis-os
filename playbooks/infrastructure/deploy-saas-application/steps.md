## FILE: `playbooks/infrastructure/deploy-saas-application/steps.md`

# Deploy SaaS Application — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Confirm Deployment Scope and Target

Clarify what will be deployed and where.

Capture:

- release name;
- commit SHA;
- target environment;
- included changes;
- excluded changes;
- deployment owner;
- planned deployment window.

Output:

```text
Deployment scope summary
```

---

# 2. Step 2 — Verify CI and Build Readiness

Confirm that the deployment candidate is valid.

Check:

- required CI checks;
- build status;
- test status;
- lint or typecheck status;
- artifact version;
- deployment preview if available.

Output:

```text
Build readiness summary
```

---

# 3. Step 3 — Review Environment Configuration

Confirm environment configuration is correct.

Review:

- environment variables;
- runtime version;
- deployment region;
- domain settings;
- feature flags;
- service URLs;
- database connection;
- storage configuration.

Output:

```text
Environment configuration summary
```

---

# 4. Step 4 — Review Secrets and Permissions

Confirm that secrets and access controls are available without exposure.

Check:

- required secrets;
- secret names;
- service account permissions;
- deployment token permissions;
- cloud access;
- database permissions;
- secret rotation concerns.

Output:

```text
Secrets and permissions readiness summary
```

---

# 5. Step 5 — Review Migration and Data Impact

Identify whether deployment changes data or schema.

Check:

- database migrations;
- data backfill;
- index changes;
- destructive operations;
- backward compatibility;
- rollback limits;
- backup requirement.

Output:

```text
Migration readiness summary
```

---

# 6. Step 6 — Confirm Rollback Plan

Define how to recover if deployment fails.

Capture:

- rollback trigger;
- rollback owner;
- previous version;
- rollback steps;
- data rollback constraints;
- feature flag fallback;
- verification after rollback.

Output:

```text
Rollback readiness summary
```

---

# 7. Step 7 — Execute Deployment

Run deployment according to the approved process.

Record:

- start time;
- deployment command or platform action;
- deployed version;
- warnings;
- completion status;
- operator.

Output:

```text
Deployment execution log
```

---

# 8. Step 8 — Run Smoke Tests

Verify critical behavior immediately after deployment.

Test:

- application loads;
- login works;
- critical API responds;
- database connection works;
- key workflow completes;
- background jobs or queues are healthy;
- payment or file flows if affected.

Output:

```text
Smoke test result
```

---

# 9. Step 9 — Monitor Critical Signals

Watch the system after deployment.

Monitor:

- error rate;
- latency;
- logs;
- CPU or memory;
- database health;
- queue health;
- user workflow success;
- support reports.

Output:

```text
Post-deployment monitoring result
```

---

# 10. Step 10 — Confirm Success or Trigger Rollback

Make the final deployment decision.

Possible outcomes:

```text
success
monitor_longer
rollback
hotfix_needed
escalate
```

Output:

```text
Deployment confirmation decision
```

---

# 11. Final Principle

> Deployment steps should protect users by validating every critical assumption after release.
