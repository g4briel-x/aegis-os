## FILE: `playbooks/engineering/optimize-database-performance/decision-points.md`

# Optimize Database Performance — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the Database the Bottleneck?

```yaml
decision_point:
  question: Is the observed performance issue caused primarily by database behavior?
  options:
    - yes
    - no
    - unclear
  criteria:
    - slow query duration
    - database CPU or I/O pressure
    - lock waits
    - endpoint time spent in database
    - slow query logs
  recommended_action:
    yes: continue database optimization.
    no: investigate application, network or external service performance.
    unclear: collect traces and timing evidence.
  fallback: compare application timing with database timing.
```

---

# 2. Decision Point — Is an Index the Right Fix?

```yaml
decision_point:
  question: Would adding or changing an index solve the issue safely?
  options:
    - yes
    - no
    - maybe
  criteria:
    - query filter pattern
    - sort pattern
    - join columns
    - table size
    - write overhead
    - existing index coverage
  recommended_action:
    yes: propose index with migration and verification plan.
    no: optimize query or workflow first.
    maybe: test in staging with execution plan comparison.
  fallback: avoid production index changes without evidence.
```

---

# 3. Decision Point — Is Query Rewrite Safer Than Schema Change?

```yaml
decision_point:
  question: Can query rewrite improve performance with lower risk than schema change?
  options:
    - yes
    - no
    - unclear
  criteria:
    - unnecessary joins
    - unbounded result sets
    - N+1 pattern
    - excessive columns
    - aggregation behavior
  recommended_action:
    yes: rewrite query first.
    no: evaluate index or schema change.
    unclear: test both approaches outside production.
  fallback: choose the smallest reversible change.
```

---

# 4. Decision Point — Is Production Change Risk Acceptable?

```yaml
decision_point:
  question: Is it safe to apply the optimization in production?
  options:
    - yes
    - no
    - requires_window
  criteria:
    - table size
    - migration lock risk
    - write traffic
    - rollback path
    - affected workflows
  recommended_action:
    yes: apply with monitoring.
    no: prepare safer migration or defer.
    requires_window: schedule maintenance or use online migration strategy.
  fallback: apply mitigation first, permanent change later.
```

---

# 5. Decision Point — Is Improvement Verified?

```yaml
decision_point:
  question: Did the optimization measurably improve performance without breaking correctness?
  options:
    - yes
    - no
    - partially
  criteria:
    - query duration improved
    - endpoint latency improved
    - tests passed
    - execution plan improved
    - no correctness regression
  recommended_action:
    yes: document and monitor.
    no: revert or try next hypothesis.
    partially: decide whether additional work is needed.
  fallback: keep monitoring until confidence is high.
```

---

# 6. Final Principle

> Database performance decisions must balance speed, correctness, operational safety and long-term maintainability.
