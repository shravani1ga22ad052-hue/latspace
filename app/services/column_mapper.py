from __future__ import annotations

import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Any

from app.services.asset_detector import detect_asset


@dataclass
class MappingResult:
    column_index: int
    original_header: str
    parameter: str | None
    asset: str | None
    confidence: float
    mapped_by: str


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", text.lower())).strip()


def map_header(header: str, registry: list[dict[str, Any]]) -> MappingResult:
    header_norm = normalize(header)
    best_name: str | None = None
    best_score = 0.0

    for entry in registry:
        candidates = [entry["display_name"], entry["name"].replace("_", " ")]
        for candidate in candidates:
            candidate_norm = normalize(candidate)
            score = SequenceMatcher(None, header_norm, candidate_norm).ratio()
            if candidate_norm and candidate_norm in header_norm:
                score = max(score, 0.95)
            if score > best_score:
                best_score = score
                best_name = entry["name"]

    if best_score >= 0.95:
        mapped_by = "exact_or_contains"
    elif best_score >= 0.72:
        mapped_by = "fuzzy"
    else:
        mapped_by = "unmapped"
        best_name = None

    return MappingResult(
        column_index=-1,
        original_header=header,
        parameter=best_name,
        asset=detect_asset(header),
        confidence=round(best_score, 3),
        mapped_by=mapped_by,
    )
