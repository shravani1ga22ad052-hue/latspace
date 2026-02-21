from __future__ import annotations

from typing import Any


NULLISH = {"n/a", "na", "null", "none", "-", ""}
TRUEISH = {"yes", "y", "true"}
FALSEISH = {"no", "n", "false"}


def parse_value(raw: Any) -> float | None:
    """Parse heterogeneous spreadsheet values into normalized floats."""
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        return float(raw)

    text = str(raw).strip()
    lowered = text.lower()

    if lowered in NULLISH:
        return None
    if lowered in TRUEISH:
        return 1.0
    if lowered in FALSEISH:
        return 0.0

    is_percent = text.endswith("%")
    cleaned = text.replace(",", "").replace("%", "")

    try:
        parsed = float(cleaned)
        return parsed / 100.0 if is_percent else parsed
    except ValueError:
        return None
