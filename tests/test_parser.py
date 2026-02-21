from pathlib import Path

from app.parser import parse_workbook


def test_parse_clean_file() -> None:
    content = Path("test_data/clean_data.xlsx").read_bytes()
    result = parse_workbook(content)
    assert result["record_count"] > 0
    assert any(r["parameter"] == "coal_consumption" for r in result["records"])


def test_parse_messy_file_detects_unmapped() -> None:
    content = Path("test_data/messy_data.xlsx").read_bytes()
    result = parse_workbook(content)
    unmapped = result["sheets"][0]["unmapped_columns"]
    assert "Random Notes" in unmapped


def test_parse_multi_asset() -> None:
    content = Path("test_data/multi_asset.xlsx").read_bytes()
    result = parse_workbook(content)
    assets = {r["asset"] for r in result["records"] if r["parameter"] == "coal_consumption"}
    assert "AFBC-1" in assets
    assert "AFBC-2" in assets
