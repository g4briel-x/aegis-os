## FILE: `templates/operations/incident-report-template/usage.md`

# Incident Report Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Create report when incident is declared
2. Assign owner and incident commander
3. Record current status and severity
4. Document customer impact
5. Document affected systems
6. Start timeline immediately
7. Record actions as they happen
8. Add communication status
9. Track next steps and owners
10. Complete resolution section after recovery
```

---

# 2. Recommended Update Cadence

```text
SEV1: update every 15-30 minutes
SEV2: update every 30-60 minutes
SEV3: update as material changes occur
SEV4: normal issue tracking is usually enough
```

---

# 3. Writing Rules

An Incident Report should:

- state facts clearly;
- avoid speculation;
- distinguish confirmed impact from suspected impact;
- include timestamps;
- include owners;
- include next update time;
- be updated as the incident evolves.

---

# 4. Impact Rule

Weak:

```text
The system is broken.
```

Better:

```text
Creators cannot submit completed project packages. Draft editing and login remain available.
```

---

# 5. Final Principle

> Use the Incident Report Template to keep response aligned while the incident is still moving.
