## FILE: `SECURITY.md`

# Security Policy

## Supported Versions

Aegis OS is currently in foundation development.

| Version | Supported |
|---|---|
| v0.7.x | Yes |
| Earlier versions | No |

---

## Reporting a Vulnerability

If a security issue is discovered, do not open a public issue with exploit details.

Recommended report content:

```text
Affected file or command
Description of the vulnerability
Steps to reproduce
Possible impact
Suggested fix if available
```

---

## Security Scope

Security issues may include:

```text
unsafe script behavior
path traversal risk
secret exposure
incorrect permission assumptions
unsafe workflow configuration
registry tampering risk
supply chain risk
CI/CD misconfiguration
```

---

## Out of Scope

The following are not considered security vulnerabilities at this stage:

```text
missing runtime features
missing marketplace implementation
missing SDK implementation
incomplete future roadmap items
```

---

## Current Security Model

Aegis OS v0.7 focuses on:

```text
repository structure
validation
traceability
manual review
CLI transparency
GitHub workflow checks
```

Future versions should include stronger controls for:

```text
signed packages
asset verification
permission policies
runtime sandboxing
audit logs
role-based access
```

---

## Final Principle

> Security reports should help protect the integrity, trust and safety of the Aegis OS repository.
