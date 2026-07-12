## FILE: `patterns/engineering/database-migration-safety/trade-offs.md`

# Database Migration Safety — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

This Pattern improves:

```text
production safety
data integrity
release confidence
rollback readiness
customer trust
database maintainability
operational visibility
```

---

# 2. Costs

This Pattern adds:

```text
planning effort
review time
extra deployment steps
temporary compatibility code
dual-write complexity
validation query maintenance
cleanup work
```

---

# 3. Speed Trade-Off

Fast migrations can be tempting but risky.

Mitigation:

```text
classify risk
split large changes
use expand-and-contract
test on realistic data
validate before and after
```

---

# 4. Rollback Trade-Off

Some migrations cannot be truly rolled back.

Examples:

```text
data deletion
lossy transformation
large irreversible rewrite
external side effect
```

Mitigation:

```text
backup before destructive change
prefer forward fix
delay destructive cleanup
use feature flags
keep old columns temporarily
```

---

# 5. Performance Trade-Off

Indexes and constraints can improve correctness and speed but may lock or slow production during creation.

Mitigation:

```text
use online index creation where available
schedule low-traffic windows
monitor locks
split constraint validation
clean data before enforcing constraints
```

---

# 6. Main Risks

Key risks:

```text
data loss
downtime
table locks
failed backfill
tenant leakage
broken application compatibility
stale code paths
missing cleanup
```

---

# 7. Mitigations

Mitigate with:

- migration review;
- backup plan;
- expand-and-contract;
- batched backfills;
- validation queries;
- monitoring;
- rollback or recovery plan;
- post-migration cleanup.

---

# 8. Final Principle

> Migration trade-offs should be accepted explicitly, never discovered during production failure.
