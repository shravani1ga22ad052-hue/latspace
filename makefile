.PHONY: install test run generate-data package

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

generate-data:
	python scripts/create_test_data.py

test:
	pytest -q

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

package:
	python scripts/package_zip.py
