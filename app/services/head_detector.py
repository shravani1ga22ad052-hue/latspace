from __future__ import annotations

from typing import Any


def detect_header_row(rows: list[list[Any]]) -> int:
    """Heuristic header detection: dense row + mostly strings in first 25 rows."""
    best_idx = 0
    best_score = -1.0

    for idx, row in enumerate(rows[:25]):
        non_empty = sum(1 for cell in row if cell is not None and str(cell).strip())
        string_like = sum(1 for cell in row if isinstance(cell, str) and cell.strip())
        score = non_empty + (1.5 * string_like)
        if score > best_score:
            best_score = score
            best_idx = idx
    return best_idx
