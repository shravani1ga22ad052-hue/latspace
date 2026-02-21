from __future__ import annotations

import re

ASSET_PATTERNS = [
    r"\b(AFBC[-\s]?\d+)\b",
    r"\b(TG[-\s]?\d+)\b",
    r"\b(Boiler[-\s]?\d+)\b",
    r"\b(Turbine[-\s]?\d+)\b",
]


def detect_asset(header: str) -> str | None:
    """Extract and normalize asset names from column headers."""
    for pattern in ASSET_PATTERNS:
        match = re.search(pattern, header, flags=re.IGNORECASE)
        if not match:
            continue
        value = match.group(1).upper().replace(" ", "-")
        if value.startswith("BOILER"):
            return value.replace("BOILER", "AFBC")
        if value.startswith("TURBINE"):
            return value.replace("TURBINE", "TG")
        return value
    return None
