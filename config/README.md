## FILE: `config/README.md`

# Aegis OS — Configuration

Version: 0.1.0  
Status: Draft

---

# 1. Purpose

This folder contains configuration examples for Aegis OS local tooling.

Configuration files define where the CLI should find registries, scripts, reports, documentation and output folders.

---

# 2. Configuration Files

```text
config/aegis.config.example.yaml
config/aegis.config.local.example.yaml
```

---

# 3. Rule

The example configuration is safe to commit.

Local configuration should be copied from the example when needed.

Recommended local file:

```text
config/aegis.config.local.yaml
```

This file should be ignored later if it contains user-specific local paths.

---

# 4. Final Principle

> Configuration should make local tooling predictable without hardcoding machine-specific assumptions.
