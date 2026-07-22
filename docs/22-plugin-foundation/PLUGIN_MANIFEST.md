# Plugin manifest foundation

A plugin is declared by `plugins/<plugin-name>/aegis-plugin.yaml`. Discovery is
purely declarative: Aegis reads and validates YAML files; it does not import or
execute an entrypoint. Execution will require a later, explicit security model.

Required fields are `id`, `name`, `version`, and `entrypoint`. IDs use lowercase
letters, digits, dots and hyphens. Versions use semantic version notation, and
entrypoints use `module:function` notation.

Use `aegis --repo-root . plugin list` to inspect discovered manifests and
`aegis --repo-root . plugin validate` to reject invalid or duplicate IDs.
