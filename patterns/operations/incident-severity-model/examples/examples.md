## FILE: `patterns/operations/incident-severity-model/examples/examples.md`

# Incident Severity Model — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS Submission Failure

## Incident

Creators cannot submit project packages for financing review.

## Classification

```text
SEV2 if many users are affected and workaround exists.
SEV1 if submission is completely unavailable during launch or paid pilot with no workaround.
```

## Response

```text
assign technical lead
notify support
monitor submission endpoint
communicate customer impact if visible
create postmortem if SEV1 or prolonged SEV2
```

---

# 2. Example — Cross-Tenant Data Exposure

## Incident

A user can access another workspace's project document.

## Classification

```text
SEV1 or SEV0 depending on exposure scope and legal risk.
```

## Response

```text
start security incident process
disable affected access path
preserve audit logs
identify affected tenants
notify leadership and legal if required
prepare customer communication
postmortem required
```

---

# 3. Example — Notification Delay

## Incident

Review assignment notification emails are delayed by 45 minutes.

## Classification

```text
SEV3 if workflow can continue manually.
SEV2 if delay blocks critical customer operations.
```

---

# 4. Example — Payment Provider Outage

## Incident

Payment provider is unavailable.

## Classification

```text
SEV2 if new purchases fail but current customers can work.
SEV1 if billing failure blocks core access for active customers.
```

---

# 5. Final Principle

> Examples show that severity depends on impact, not only on the technical component that failed.