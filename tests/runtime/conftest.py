from __future__ import annotations

import sys
from pathlib import Path

RUNTIME_SRC = Path(__file__).resolve().parents[2] / "runtime" / "src"
if str(RUNTIME_SRC) not in sys.path:
    sys.path.insert(0, str(RUNTIME_SRC))
