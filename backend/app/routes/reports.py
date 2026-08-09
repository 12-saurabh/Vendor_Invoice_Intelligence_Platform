from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)



@router.get("/export/csv")
def export_csv():

    return FileResponse(
        "reports/invoices.csv",
        filename="invoices.csv"
    )



@router.get("/export/excel")
def export_excel():

    return FileResponse(
        "reports/invoices.xlsx",
        filename="invoices.xlsx"
    )



@router.get("/export/pdf")
def export_pdf():

    return FileResponse(
        "reports/invoices.pdf",
        filename="invoices.pdf"
    )