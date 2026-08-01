from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.dependencies import (
    get_db,
    get_current_user
)

from app.models.user import User
from app.models.invoice import Invoice

from app.services.report_service import (
    generate_pdf_report,
    generate_excel_report
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# ----------------------------------------
# PDF Report
# ----------------------------------------

@router.get("/pdf")
def download_pdf_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    invoices = db.query(Invoice).all()

    pdf = generate_pdf_report(invoices)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=invoice_report.pdf"
        }
    )


# ----------------------------------------
# Excel Report
# ----------------------------------------

@router.get("/excel")
def download_excel_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    invoices = db.query(Invoice).all()

    excel = generate_excel_report(invoices)

    return StreamingResponse(
        excel,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition":
            "attachment; filename=invoice_report.xlsx"
        }
    )