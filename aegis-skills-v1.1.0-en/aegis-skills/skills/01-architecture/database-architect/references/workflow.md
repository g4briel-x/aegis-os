# Detailed workflow — Database Architect

## 1. Frame the request

- Restate the request and the expected outcome.
- Identify the decision maker, users, systems, data, and risk level.
- Define delivery, budget, security, compliance, compatibility, and operational constraints.
- Establish observable success criteria and explicit exclusions.

## 2. Inventory evidence

Collect only the artifacts relevant to the context: source code, tests, architecture, schemas, tickets, logs, metrics, traces, designs, user journeys, contracts, incidents, data, or documentation.

Classify every material item as:

- observed fact;
- testable assumption;
- missing information;
- existing decision;
- non-negotiable constraint.

## 3. Analyze

- Decompose the problem into independently verifiable subproblems.
- Rank risks by impact, probability, detectability, and validation cost.
- Identify dependencies, interfaces, and accountable owners.
- Prefer the simplest solution that satisfies the criteria.
- Define at least one credible alternative for structural decisions.

## 4. Design the recommendation or deliverable

State:

- the selected option;
- rejected alternatives and why they were rejected;
- trade-offs and consequences;
- prerequisites and dependencies;
- product, architecture, security, quality, operations, and documentation impact;
- migration or adoption path;
- rollback or recovery strategy.

## 5. Execute incrementally

1. Build the smallest testable increment.
2. Validate the highest-risk assumption first.
3. Automate repeatable controls.
4. Measure before and after when performance, quality, cost, or user outcomes are involved.
5. Record stable decisions throughout execution.

## 6. Validate

Verify at least:

- alignment with the request;
- technical and domain correctness;
- security and confidentiality;
- data integrity;
- performance and cost;
- operability and supportability;
- maintainability;
- accessibility when users are affected;
- documentation and knowledge transfer.

## 7. Deliver

The result must be usable by another senior team without hidden context. It must explain:

- what to do;
- in what order;
- with which tools or artifacts;
- how to verify success;
- how to recover or roll back;
- who owns each action;
- which risks remain open.
