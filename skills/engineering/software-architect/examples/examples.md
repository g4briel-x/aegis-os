## FILE: `skills/engineering/software-architect/examples/examples.md`

# Software Architect — Examples

Version: 0.2.0  
Status: Premium Draft

---

# 1. Example — SaaS Architecture

## User Request

Design the architecture for a SaaS platform that helps audiovisual projects move from idea to financing.

## Expected Skill Behavior

The Skill should:

- identify users and roles;
- define core modules;
- propose a tenant model;
- define data boundaries;
- propose phased implementation;
- identify security and operational risks;
- avoid overengineering.

## Expected Output Structure

```text
Assumptions
Architecture overview
Core modules
Data model
Security model
Deployment model
Roadmap
Risks
Validation notes
```

---

# 2. Example — Monolith vs Microservices

## User Request

Should my startup begin with microservices or a monolith?

## Expected Skill Behavior

The Skill should:

- assess team size;
- assess domain complexity;
- consider deployment maturity;
- recommend a modular monolith unless microservices are justified;
- document trade-offs.

---

# 3. Example — Architecture Review

## User Request

Review this architecture: React frontend, Node.js API, PostgreSQL database, Airtable integration and external payment provider.

## Expected Skill Behavior

The Skill should review:

- component boundaries;
- API responsibilities;
- data ownership;
- integration risks;
- payment security;
- observability;
- failure handling.

---

# 4. Example — ADR

## User Request

Create an ADR for choosing PostgreSQL as the primary database.

## Expected Skill Behavior

The Skill should produce:

- context;
- decision;
- alternatives;
- consequences;
- risks;
- follow-up actions.

---

# 5. Example — AI System Architecture

## User Request

Design an architecture for an AI-powered expert assistant with Skills, memory and tool use.

## Expected Skill Behavior

The Skill should:

- separate orchestration, memory, tools and model execution;
- define trust boundaries;
- document validation loops;
- identify safety controls;
- define extension points.

---

# 6. Final Principle

> Examples prove that the Skill can move from abstract requirements to architecture decisions.