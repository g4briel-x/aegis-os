# Aegis OS — Application du correctif critique

## Rôle des fichiers

- `aegis-os-critical-hotfix.patch` : corrige le routage des commandes Python `asset`, ajoute les tests de non-régression, installe et teste le runtime Python dans GitHub Actions, renforce la validation des chemins, nettoie `.gitignore` et aligne la métadonnée de licence du package.
- `APPLY-AEGIS-HOTFIX.md` : procédure PowerShell et Git pour appliquer, tester, committer et publier le correctif.
- `aegis-os-critical-hotfix.zip` : bundle transportable contenant le patch et cette procédure.

## Corrections incluses

1. Restauration de `if args.command == "asset":` dans le routeur Python.
2. Test garantissant que `registry domains/tags` ne casse plus `asset show/find`.
3. Installation de `runtime[dev]` dans les deux workflows GitHub Actions.
4. Exécution de `pytest` et du validateur Python en CI.
5. Utilisation de `pwsh` dans les workflows.
6. Rejet des chemins absolus et des chemins sortant du dépôt.
7. Nettoyage des fences Markdown présentes dans `.gitignore`.
8. Ajout de `*.egg-info/` dans `.gitignore`.
9. Remplacement de la métadonnée MIT incorrecte dans `runtime/pyproject.toml`.

## Commandes PowerShell

Exécuter depuis la racine du dépôt `aegis-os`.

```powershell
git status
git checkout main
git pull origin main

git checkout -b fix/runtime-cli-ci-hardening

git apply --check .\aegis-os-critical-hotfix.patch
git apply .\aegis-os-critical-hotfix.patch

# Supprime de l'index les métadonnées Python générées déjà suivies.
git rm -r --cached runtime\src\aegis_runtime.egg-info

py -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -e ".\runtime[dev]"

python -m pytest

python -m aegis_runtime --repo-root . registry domains
python -m aegis_runtime --repo-root . registry tags
python -m aegis_runtime --repo-root . asset show engineering.senior-developer
python -m aegis_runtime --repo-root . asset find security
python -m aegis_runtime --repo-root . validate

pwsh -NoProfile -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1

git status
git diff --check
git diff

git add .
git commit -m "fix(runtime): restore asset routing and harden CI"
git push -u origin fix/runtime-cli-ci-hardening
```

## Création de la pull request avec GitHub CLI

```powershell
gh pr create `
  --base main `
  --head fix/runtime-cli-ci-hardening `
  --title "fix(runtime): restore asset routing and harden CI" `
  --body "Restores Python asset command routing, adds regression tests, installs and tests the Python runtime in CI, hardens registry path validation, cleans .gitignore, and aligns package license metadata."
```

## Vérification attendue

Les commandes suivantes doivent retourner un code de sortie `0` :

```powershell
python -m pytest
python -m aegis_runtime --repo-root . asset show engineering.senior-developer
python -m aegis_runtime --repo-root . validate
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts\testing\test-cli-smoke.ps1
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts\validation\validate-all.ps1
```

## Annulation avant commit

```powershell
git reset --hard HEAD
git clean -fd
git checkout main
git branch -D fix/runtime-cli-ci-hardening
```
