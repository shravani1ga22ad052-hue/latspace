# LatSpace AI Intern Take-Home — Track A (Intelligent Excel Parser)

**Track chosen:** ✅ **Track A**  
**Public GitHub Repository:** https://github.com/shravani1ga22ad052-hue/latspace  
**Screen Recording (2–5 min):** _add your Loom/Drive URL_  
**Hosted Demo (Bonus):** optional

## Is the project aligned with expectations?
Yes — this implementation follows Track A requirements:
- `POST /parse` API for `.xlsx` uploads
- Header-row auto detection
- Fuzzy column-to-parameter mapping against registry
- Asset detection from column headers
- Deterministic value parsing
- Unmapped column reporting
- Multi-sheet parsing
- Validation warnings for suspicious values

## Architecture
```text
app/
  main.py
  registry.py
  routers/
    parse.py
  services/
    excel_parser.py
    header_detector.py
    column_mapper.py
    asset_detector.py
    value_parser.py
    validator.py
data/
  parameter_registry.json
scripts/
  create_test_data.py
tests/
  test_parser.py
WORKING.md
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/create_test_data.py
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Usage
```bash
curl -X POST "http://localhost:8000/parse" -F "file=@test_data/messy_data.xlsx"
```

## Docker
```bash
docker compose up
```

## Tests
```bash
pytest -q
```

## Submission Zip
```bash
make package
```
Creates `latspace_track_a_submission.zip` including source code, docs, tests, and sample test data.

## Potential Improvements
- Add optional LLM-backed low-confidence remapping (human review mode)
- Add chunked row processing for large files
- Add async job mode with parse history
- Add richer domain-specific validation bounds
