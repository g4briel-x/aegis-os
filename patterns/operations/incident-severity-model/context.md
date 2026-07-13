## FILE: `patterns/operations/incident-severity-model/context.md`

# Incident Severity Model — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS applications with real production usage and customer impact.

Typical contexts:

```text
private beta with paying users
public SaaS production
enterprise pilot
customer-facing platform
critical workflow platform
multi-tenant application
```

---

# 2. Product Context

Use this Pattern when the product has workflows such as:

- signup;
- login;
- billing;
- project creation;
- file upload;
- submission;
- review;
- reporting;
- notifications;
- data export.

---

# 3. Operational Context

The team needs consistent rules for:

```text
alert triage
incident declaration
escalation
customer communication
executive notification
postmortem creation
reliability review
```

---

# 4. Security Context

Security-related incidents may require higher severity.

Examples:

```text
cross-tenant data exposure
unauthorized admin access
active exploit
credential leakage
audit log tampering
personal data exposure
```

Security severity should consider exposure, exploitability, scope and regulatory risk.

---

# 5. Business Context

Business impact may increase severity when incidents affect:

```text
revenue collection
enterprise customer commitments
launch events
contractual SLAs
public reputation
legal obligations
```

---

# 6. Warning Signs

Severity handling is weak when:

- every incident is called critical;
- no one knows who leads the incident;
- security events are treated as normal bugs;
- support hears about incidents from customers first;
- communication is delayed by uncertainty;
- postmortems are skipped for repeated issues.

---

# 7. Final Principle

> Incident severity context must include users, systems, business and security impact together.
