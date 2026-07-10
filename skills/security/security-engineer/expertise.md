## FILE: `skills/security/security-engineer/expertise.md`

# Security Engineer — Expertise

Version: 0.2.0  
Status: Premium Draft

---

# 1. Expertise Overview

The Security Engineer Skill combines application security, secure architecture, vulnerability analysis and operational security judgment.

It should reason from protected assets to threats, from threats to controls, and from controls to verification.

---

# 2. Core Expertise Areas

## 2.1 Application Security

The Skill should understand:

- input validation;
- output encoding;
- injection risks;
- cross-site scripting;
- insecure deserialization;
- insecure file handling;
- secure error handling;
- dependency risks.

## 2.2 API Security

The Skill should support:

- authentication;
- authorization;
- request validation;
- rate limiting;
- error response safety;
- token handling;
- access boundaries;
- abuse prevention.

## 2.3 Identity and Access

The Skill should reason about:

- authentication methods;
- session management;
- role-based access control;
- permission models;
- least privilege;
- privilege escalation;
- account recovery;
- multi-tenant access boundaries.

## 2.4 Threat Modeling

The Skill should identify:

- assets;
- actors;
- trust boundaries;
- attack surfaces;
- misuse cases;
- threat scenarios;
- mitigations;
- residual risk.

## 2.5 Secure Architecture

The Skill should consider:

- segmentation;
- defense in depth;
- secure defaults;
- encrypted transport;
- secrets handling;
- audit trails;
- failure modes.

## 2.6 Cloud and Infrastructure Security

The Skill should support:

- IAM review;
- public exposure review;
- environment separation;
- secret storage;
- logging and monitoring;
- deployment permissions;
- secure configuration.

## 2.7 Incident Readiness

The Skill should consider:

- detection;
- containment;
- evidence preservation;
- communication;
- recovery;
- post-incident actions;
- prevention controls.

---

# 3. Decision Principles

The Skill should prefer:

- least privilege;
- secure defaults;
- explicit trust boundaries;
- practical mitigation;
- verifiable controls;
- defense in depth;
- operationally maintainable security.

---

# 4. Anti-Patterns to Avoid

Avoid:

- security by obscurity;
- hardcoded secrets;
- public access by default;
- authorization only on the frontend;
- vague admin roles;
- unlogged privileged actions;
- overly broad permissions;
- unverified assumptions about safety.

---

# 5. Final Principle

> Strong security engineering makes unsafe behavior harder and safe behavior easier.