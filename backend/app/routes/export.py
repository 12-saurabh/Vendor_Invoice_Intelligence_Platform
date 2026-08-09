from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.services.export_service import (
    export_csv,
    export_excel,
    export_pdf
)

from app.database import get_db
from app.models.invoice import Invoice


router = APIRouter(
    prefix="/export",
    tags=["Export"]
)


@router.get("/csv")
def csv_export(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    file = export_csv(invoices)

    return FileResponse(
        file,
        filename="Invoices.csv",
        media_type="text/csv"
    )


@router.get("/excel")
def excel_export(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    file = export_excel(invoices)

    return FileResponse(
        file,
        filename="Invoices.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@router.get("/pdf")
def pdf_export(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    file = export_pdf(invoices)

    return FileResponse(
        file,
        filename="Invoices.pdf",
        media_type="application/pdf"
    )