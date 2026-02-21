from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

REGISTRY_PATH = Path("data/parameter_registry.json")


@lru_cache(maxsize=1)
def load_parameter_registry() -> list[dict[str, Any]]:
    """Load the canonical parameter registry from disk."""
    return json.loads(REGISTRY_PATH.read_text())
