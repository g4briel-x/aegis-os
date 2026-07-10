## FILE: `skills/security/security-engineer/examples/examples.md`

# Security Engineer — Examples

Version: 0.2.0  
Status: Premium Draft

---

# 1. Example — SaaS Access Control

## User Request

Design access control for a SaaS platform with admins, creators, producers and investors.

## Expected Skill Behavior

The Skill should:

- define roles;
- define protected resources;
- create a permission matrix;
- consider tenant boundaries;
- protect admin actions;
- define audit needs.

## Expected Output Structure

```text
Assumptions
Roles
Resources
Permission matrix
Risks
Mitigations
Audit notes
Validation notes
```

---

# 2. Example — API Security Review

## User Request

Review an API endpoint that updates a user's billing information.

## Expected Skill Behavior

The Skill should:

- require authentication;
- enforce authorization;
- validate input;
- protect sensitive data;
- avoid leaking errors;
- recommend audit logging.

---

# 3. Example — Secrets Handling

## User Request

Where should I store API keys for deployment?

## Expected Skill Behavior

The Skill should:

- reject hardcoding secrets;
- recommend environment or secret manager usage;
- define rotation and least privilege;
- warn against logging secrets.

---

# 4. Example — Threat Model

## User Request

Create a threat model for an AI-powered expert assistant with tools and memory.

## Expected Skill Behavior

The Skill should:

- identify assets such as memory, tools and credentials;
- define trust boundaries;
- identify prompt injection and unauthorized tool use risks;
- propose mitigations and validation.

---

# 5. Example — Security Incident

## User Request

A token may have been leaked in logs. What should we do?

## Expected Skill Behavior

The Skill should:

- recommend immediate revocation;
- identify exposure scope;
- preserve evidence;
- rotate credentials;
- search for misuse;
- add prevention controls.

---

# 6. Final Principle

> Examples prove that the Skill can turn security concerns into concrete protection actions.