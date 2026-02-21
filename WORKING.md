# How the Project Works (Track A)

## Flow Overview
1. Client uploads an `.xlsx` file to `POST /parse`.
2. API validates extension and empty payload guards.
3. Workbook parser iterates all sheets.
4. For each sheet:
   - detect header row using deterministic scoring
   - map each header to canonical parameter names
   - detect asset from header text
   - parse values into normalized floats
5. Aggregate records, sheet metadata, unmapped columns, and warnings.
6. Return structured JSON payload.

## Modules
- `app/routers/parse.py` — HTTP endpoints
- `app/services/header_detector.py` — header row heuristic
- `app/services/column_mapper.py` — fuzzy header mapping
- `app/services/asset_detector.py` — regex-based asset extraction
- `app/services/value_parser.py` — deterministic value parsing
- `app/services/validator.py` — warning rules
- `app/services/excel_parser.py` — orchestration
- `data/parameter_registry.json` — canonical parameter registry

## Run Locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/create_test_data.py
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Test
```bash
pytest -q
```

## Create Zip Submission
```bash
make package
```
This generates `latspace_track_a_submission.zip` in repository root.
