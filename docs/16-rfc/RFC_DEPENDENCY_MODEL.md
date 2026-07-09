# Aegis OS — RFC Dependency Model

Version: 0.1  
Status: RFC Document

---

# 1. Introduction

This document defines how RFCs may depend on one another.

---

# 2. Dependency Types

Possible dependency relationships:

- blocks;
- blocked-by;
- supersedes;
- extends;
- requires prior approval of;
- implementation depends on.

---

# 3. Example

```yaml
rfc_dependencies:
  blocks:
    - RFC-0012
  blocked_by:
    - RFC-0008
```

---

# 4. Final Principle

> RFC dependency visibility prevents contradictory or prematurely sequenced changes.
