from __future__ import annotations

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.excel_parser import parse_workbook

router = APIRouter(tags=["parse"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/parse")
async def parse(file: UploadFile = File(...)) -> dict:
    if not file.filename or not file.filename.lower().endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Only .xlsx files are supported")

    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    return parse_workbook(content)
