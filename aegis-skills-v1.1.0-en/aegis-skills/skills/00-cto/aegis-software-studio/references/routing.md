# Aegis Skill Routing

## Selection rules

1. Select the smallest set of skills that fully covers the request.
2. Assign one lead skill accountable for the final result.
3. Add a validation role only when it covers a distinct material risk.
4. Do not activate multiple roles merely to repeat the same analysis.
5. Consolidate disagreements as explicit trade-offs and record the decision owner.
6. Preserve facts, assumptions, decisions, dependencies, and residual risks across handoffs.

## Skill catalog

| Skill | Category | Mission |
|---|---|---|
| `cto` | Technology Leadership | Orchestrate Aegis Skills, select the relevant expertise, arbitrate structural decisions, and validate delivery alignment with the Aegis OS strategy. |
| `cloud-architect` | Architecture | Design secure, scalable, cost-efficient, and operable cloud architectures. |
| `cloud-engineer` | Architecture | Implement and maintain cloud resources according to architecture, security, reliability, and cost standards. |
| `database-administrator` | Architecture | Operate critical databases with reliable backups, monitoring, security, maintenance, and recovery procedures. |
| `database-architect` | Architecture | Design data models, schemas, indexes, migrations, and availability strategies. |
| `database-performance` | Architecture | Diagnose and optimize database performance and critical queries. |
| `software-architect` | Architecture | Design software architecture, domain boundaries, structural patterns, and migration paths. |
| `solution-architect` | Architecture | Translate business requirements into a coherent technical solution spanning applications, integrations, data, security, and operations. |
| `api-engineer` | Engineering | Design reliable, secure, versioned, documented, and consumer-friendly APIs. |
| `legacy-modernization` | Engineering | Modernize existing systems incrementally while reducing risk, technical debt, and operating cost. |
| `performance-engineer` | Engineering | Measure, diagnose, and optimize application and infrastructure performance. |
| `security-engineer` | Engineering | Reduce application and platform risk by strengthening authentication, authorization, encryption, APIs, secrets, and DevSecOps controls. |
| `senior-code-reviewer` | Engineering | Review code to identify defects, anti-patterns, security risks, performance issues, and maintainability concerns. |
| `senior-debugger` | Engineering | Identify root causes, analyze logs, dumps, traces, and profiles, correct critical defects, and produce a rigorous root-cause analysis. |
| `senior-developer` | Engineering | Deliver clean, robust, maintainable, tested, enterprise-grade software. |
| `automation-engineer` | Quality Assurance | Automate reliable, fast, and maintainable tests to accelerate delivery without sacrificing quality. |
| `penetration-tester` | Quality Assurance | Identify and demonstrate exploitable vulnerabilities, then recommend verifiable remediation. |
| `qa-engineer` | Quality Assurance | Define the quality strategy, identify product risks, and verify that the product satisfies measurable acceptance criteria. |
| `devops` | DevOps and Reliability | Industrialize build, test, deployment, environment management, release, and operational automation. |
| `kubernetes` | DevOps and Reliability | Design, deploy, and operate secure, observable, and resilient Kubernetes workloads. |
| `observability` | DevOps and Reliability | Make systems observable enough to diagnose incidents, performance degradation, and user-experience issues. |
| `sre` | DevOps and Reliability | Protect reliability, availability, capacity, observability, and incident-response readiness. |
| `business-analyst` | Product | Clarify business needs, processes, requirements, rules, and acceptance criteria. |
| `product-manager` | Product | Turn business objectives and user needs into a prioritized roadmap, an evidence-based MVP, and measurable product outcomes. |
| `scrum-master` | Product | Facilitate team delivery, remove blockers, protect flow, and improve delivery cadence and team health. |
| `design-system` | Design | Build and govern a coherent, reusable, accessible, and maintainable design system. |
| `ui-designer` | Design | Design readable, coherent, accessible, responsive interfaces that product and engineering teams can implement directly. |
| `ux-designer` | Design | Design effective user journeys, clarify user needs, and improve end-to-end workflows. |
| `api-documentation` | Documentation | Document APIs so they are understandable, testable, secure, and easy to integrate. |
| `technical-writer` | Documentation | Produce clear, accurate, maintainable documentation tailored to its audience and operational context. |
| `user-manual` | Documentation | Create task-oriented user documentation that reduces friction, support demand, and usage errors. |
| `ai-architect` | Artificial Intelligence | Design the end-to-end AI architecture across models, data, evaluation, safety, privacy, cost, and product integration. |
| `agent-architect` | Artificial Intelligence | Design robust, controllable, observable, and secure agent architectures. |
| `mcp-architect` | Artificial Intelligence | Design secure, maintainable, auditable, and useful Model Context Protocol integrations for AI agents. |
| `prompt-engineer` | Artificial Intelligence | Optimize prompts, AI workflows, evaluations, guardrails, tool use, and multi-agent orchestration. |
| `rag-engineer` | Artificial Intelligence | Build reliable retrieval-augmented generation systems covering ingestion, chunking, retrieval, reranking, grounding, evaluation, and observability. |

## Recommended sequences

- **New SaaS feature**: `product-manager` → `ux-designer` → `software-architect` → `senior-developer` → `qa-engineer` → `devops`.
- **Production incident**: `sre` → `observability` → `senior-debugger` → accountable engineering skill → `technical-writer` for the postmortem.
- **Security-sensitive API**: `api-engineer` → `security-engineer` → `penetration-tester` → `qa-engineer` → `devops`.
- **Cloud migration**: `solution-architect` → `cloud-architect` → `database-architect` → `cloud-engineer` → `sre`.
- **AI or agent feature**: `product-manager` → `ai-architect` → relevant AI specialist → `security-engineer` → `qa-engineer`.
