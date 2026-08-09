import os

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.invoice import Invoice
from app.services.export_service import (
    export_csv,
    export_excel,
    export_pdf,
)


router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.get("/csv")
def csv_export(
    db: Session = Depends(get_db),
):
    invoices = db.query(Invoice).all()

    file_path = export_csv(invoices)

    return FileResponse(
        file_path,
        filename="Invoices.csv",
        media_type="text/csv",
        background=None,
    )


@router.get("/excel")
def excel_export(
    db: Session = Depends(get_db),
):
    invoices = db.query(Invoice).all()

    file_path = export_excel(invoices)

    return FileResponse(
        file_path,
        filename="Invoices.xlsx",
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
    )


@router.get("/pdf")
def pdf_export(
    db: Session = Depends(get_db),
):
    invoices = db.query(Invoice).all()

    file_path = export_pdf(invoices)

    return FileResponse(
        file_path,
        filename="Invoices.pdf",
        media_type="application/pdf",
    )

