## FILE: `cli/CLI_EXIT_CODES.md`

# Aegis OS — CLI Exit Codes

Version: 0.1.0  
Status: Draft  
Domain: CLI  
Category: Error Handling

---

# 1. Purpose

This document defines standard exit codes for Aegis OS CLI commands.

Exit codes allow CI, scripts and automation to know whether a command succeeded or failed.

---

# 2. Standard Exit Codes

```text
0   Success
1   Generic failure
2   Missing argument
3   Missing file or folder
4   Invalid command
5   Validation failure
6   Test failure
7   Configuration failure
8   Registry failure
9   Git failure
10  Report generation failure
```

---

# 3. Usage Rules

## Success

Use:

```text
exit 0
```

When the command completed successfully.

---

## Missing Argument

Use:

```text
exit 2
```

When a command requires an argument and none was provided.

Example:

```powershell
.\cli\aegis.ps1 asset:show
```

---

## Missing File

Use:

```text
exit 3
```

When an expected file or folder is missing.

---

## Invalid Command

Use:

```text
exit 4
```

When the command name is unknown.

---

## Validation Failure

Use:

```text
exit 5
```

When registry or structural validation fails.

---

# 4. Current Compatibility

Some existing scripts may still return `exit 1` for all failures.

That is acceptable during the early CLI foundation stage.

Future versions should migrate toward the standard codes defined here.

---

# 5. Final Principle

> Exit codes make CLI behavior reliable for automation and CI.
