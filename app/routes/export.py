from fastapi import APIRouter,Depends
from fastapi.responses import FileResponse

from app.services.export_service import *
from app.database import get_db
from app.models.invoice import Invoice


router=APIRouter()


@router.get("/export/csv")
def csv_export(db=Depends(get_db)):

    invoices=db.query(Invoice).all()

    file=export_csv(invoices)

    return FileResponse(file)



@router.get("/export/excel")
def excel_export(db=Depends(get_db)):

    invoices=db.query(Invoice).all()

    file=export_excel(invoices)

    return FileResponse(file)



@router.get("/export/pdf")
def pdf_export(db=Depends(get_db)):

    invoices=db.query(Invoice).all()

    file=export_pdf(invoices)

    return FileResponse(file)