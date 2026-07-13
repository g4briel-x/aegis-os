## FILE: `cli/CLI_OUTPUT_MODEL.md`

# Aegis OS — CLI Output Model

Version: 0.1.0  
Status: Draft  
Domain: CLI  
Category: Output Standard

---

# 1. Purpose

This document defines how Aegis OS CLI commands should communicate results to humans and automation systems.

The CLI must be readable, predictable and script-friendly.

---

# 2. Output Types

Aegis OS CLI output can be grouped into:

```text
informational output
success output
warning output
error output
list output
metadata output
diagnostic output
```

---

# 3. Human Output

Human output should use concise labels:

```text
OK
BAD
WARN
MISS
INFO
```

Example:

```text
OK   cli/aegis.ps1
BAD  registry/skills/skills.registry.yaml
WARN Working tree has changes
INFO Aegis OS version: 0.1.0
```

---

# 4. Automation Output

Future CLI versions may support:

```powershell
.\cli\aegis.ps1 registry:list --json
.\cli\aegis.ps1 asset:show engineering.senior-developer --json
```

The current version defaults to human-readable text.

---

# 5. Output Rules

CLI commands should:

```text
print useful context before results
avoid unnecessary noise
return proper exit codes
keep command names stable
avoid hiding failures
use consistent labels
```

---

# 6. Final Principle

> CLI output should be understandable by a human and dependable for automation.
