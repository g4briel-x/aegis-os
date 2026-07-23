# Building Aegis Runtime

This repository is prepared to build a Python wheel and source distribution.
Building artifacts does not publish anything to PyPI.

## Build locally

From the repository root:

```console
python -m pip install "./runtime[dev]"
python -m build runtime --outdir dist
python scripts/testing/verify-package-artifacts.py dist
python scripts/testing/verify-package-install.py dist
```

The result contains one `.whl` file and one `.tar.gz` source distribution.
The verification script checks that both carry the runtime module and package
metadata, then installs the wheel into a clean virtual environment and runs
the `aegis` and `aegis-runtime` console entry points.

## Publication boundary

No PyPI token or publishing workflow is configured. A future release process
must explicitly select a version, confirm the package name is available and
publish through trusted CI credentials. Publication must also be approved by
the project owner under the Aegis OS Business Source License 1.1.
