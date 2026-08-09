from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.invoice import Invoice

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import os

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)


@router.get("/csv")
def export_csv(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    data = []

    for inv in invoices:
        data.append({
            "Invoice No": inv.invoice_number,
            "Vendor": inv.vendor_name,
            "Amount": inv.amount,
            "Currency": inv.currency,
            "Status": inv.status
        })

    df = pd.DataFrame(data)

    path = os.path.join(EXPORT_DIR, "invoices.csv")
    df.to_csv(path, index=False)

    return FileResponse(
        path,
        filename="Invoices.csv",
        media_type="text/csv"
    )


@router.get("/excel")
def export_excel(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    data = []

    for inv in invoices:
        data.append({
            "Invoice No": inv.invoice_number,
            "Vendor": inv.vendor_name,
            "Amount": inv.amount,
            "Currency": inv.currency,
            "Status": inv.status
        })

    df = pd.DataFrame(data)

    path = os.path.join(EXPORT_DIR, "invoices.xlsx")
    df.to_excel(path, index=False)

    return FileResponse(
        path,
        filename="Invoices.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@router.get("/pdf")
def export_pdf(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()

    rows = [
        ["Invoice No", "Vendor", "Amount", "Currency", "Status"]
    ]

    for inv in invoices:
        rows.append([
            str(inv.invoice_number),
            str(inv.vendor_name),
            str(inv.amount),
            str(inv.currency),
            str(inv.status)
        ])

    path = os.path.join(EXPORT_DIR, "invoices.pdf")

    pdf = SimpleDocTemplate(
        path,
        pagesize=letter
    )

    table = Table(rows)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ])
    )

    pdf.build([table])

    return FileResponse(
        path,
        filename="Invoices.pdf",
        media_type="application/pdf"
    )