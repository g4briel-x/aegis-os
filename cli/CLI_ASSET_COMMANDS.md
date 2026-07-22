# Asset commands

```console
aegis --repo-root . asset show engineering.senior-developer
aegis --repo-root . asset find security
aegis --repo-root . asset related security.security-review-template
aegis --repo-root . asset path business.pricing-strategy-template
aegis --repo-root . asset open design.ux-flow-template
aegis --repo-root . asset domain security
aegis --repo-root . asset tag api
aegis --repo-root . asset type skill
```

`show`, `path` and `open` return exit code `5` when the requested asset or path
does not exist. `open` uses the operating system's default application.
