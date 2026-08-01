from io import BytesIO
from openpyxl import Workbook
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
)

from app.models.invoice import Invoice


def generate_excel_report(invoices):

    wb = Workbook()

    ws = wb.active

    ws.title = "Invoices"

    ws.append([
        "Invoice No",
        "Vendor",
        "Amount",
        "Status",
        "Risk",
    ])

    for invoice in invoices:

        ws.append([
            invoice.invoice_number,
            invoice.vendor.name if invoice.vendor else "",
            invoice.amount,
            invoice.status,
            invoice.risk_level,
        ])

    stream = BytesIO()

    wb.save(stream)

    stream.seek(0)

    return stream


def generate_pdf_report(invoices):

    stream = BytesIO()

    doc = SimpleDocTemplate(
        stream,
        pagesize=letter
    )

    data = [[
        "Invoice",
        "Vendor",
        "Amount",
        "Status",
        "Risk"
    ]]

    for invoice in invoices:

        data.append([
            invoice.invoice_number,
            invoice.vendor.name if invoice.vendor else "",
            str(invoice.amount),
            invoice.status,
            invoice.risk_level
        ])

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

        ])

    )

    doc.build([table])

    stream.seek(0)

    return stream