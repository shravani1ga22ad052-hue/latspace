from __future__ import annotations

from typing import Any


def build_validation_warnings(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    warnings: list[dict[str, Any]] = []

    for item in records:
        value = item.get("value")
        parameter = item.get("parameter")
        if value is None:
            continue
        if parameter == "coal_consumption" and value < 0:
            warnings.append({"type": "negative_coal", "item": item})
        if parameter == "efficiency" and value > 1:
            warnings.append({"type": "efficiency_gt_100pct", "item": item})
        if parameter in {"co2_emissions", "so2_emissions", "nox_emissions"} and value < 0:
            warnings.append({"type": "negative_emission", "item": item})

    return warnings
