import csv
from io import BytesIO, StringIO

from openpyxl import Workbook
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet


def invoice_to_dict(invoice):
    """
    Convert SQLAlchemy invoice object into a dictionary.

    Adjust these fields if your Invoice model uses different names.
    """

    return {
        "id": getattr(invoice, "id", ""),
        "invoice_number": getattr(invoice, "invoice_number", ""),
        "vendor_id": getattr(invoice, "vendor_id", ""),
        "invoice_date": getattr(invoice, "invoice_date", ""),
        "due_date": getattr(invoice, "due_date", ""),
        "total_amount": getattr(invoice, "total_amount", ""),
        "currency": getattr(invoice, "currency", ""),
        "status": getattr(invoice, "status", ""),
        "manual_approval_required": getattr(
            invoice,
            "manual_approval_required",
            "",
        ),
        "created_at": getattr(invoice, "created_at", ""),
    }


def generate_csv(invoices):
    output = StringIO()

    rows = [invoice_to_dict(invoice) for invoice in invoices]

    if not rows:
        return output.getvalue()

    fieldnames = list(rows[0].keys())

    writer = csv.DictWriter(
        output,
        fieldnames=fieldnames,
    )

    writer.writeheader()
    writer.writerows(rows)

    return output.getvalue()


def generate_excel(invoices):
    output = BytesIO()

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Invoices"

    headers = [
        "ID",
        "Invoice Number",
        "Vendor ID",
        "Invoice Date",
        "Due Date",
        "Total Amount",
        "Currency",
        "Status",
        "Manual Approval Required",
        "Created At",
    ]

    worksheet.append(headers)

    for invoice in invoices:
        data = invoice_to_dict(invoice)

        worksheet.append(
            [
                data["id"],
                data["invoice_number"],
                data["vendor_id"],
                str(data["invoice_date"]),
                str(data["due_date"]),
                data["total_amount"],
                data["currency"],
                data["status"],
                data["manual_approval_required"],
                str(data["created_at"]),
            ]
        )

    # Make columns easier to read
    column_widths = {
        "A": 10,
        "B": 25,
        "C": 15,
        "D": 18,
        "E": 18,
        "F": 15,
        "G": 12,
        "H": 20,
        "I": 25,
        "J": 25,
    }

    for column, width in column_widths.items():
        worksheet.column_dimensions[column].width = width

    workbook.save(output)

    output.seek(0)

    return output


def generate_pdf(invoices):
    output = BytesIO()

    document = SimpleDocTemplate(
        output,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20,
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Vendor Invoice Report",
        styles["Title"],
    )

    elements.append(title)
    elements.append(Spacer(1, 20))

    data = [
        [
            "ID",
            "Invoice Number",
            "Vendor ID",
            "Invoice Date",
            "Total",
            "Currency",
            "Status",
            "Approval",
        ]
    ]

    for invoice in invoices:
        invoice_data = invoice_to_dict(invoice)

        data.append(
            [
                str(invoice_data["id"]),
                str(invoice_data["invoice_number"]),
                str(invoice_data["vendor_id"]),
                str(invoice_data["invoice_date"]),
                str(invoice_data["total_amount"]),
                str(invoice_data["currency"]),
                str(invoice_data["status"]),
                str(invoice_data["manual_approval_required"]),
            ]
        )

    table = Table(
        data,
        repeatRows=1,
    )

    table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.grey,
                ),
                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white,
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold",
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.black,
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER",
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    8,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, 0),
                    8,
                ),
            ]
        )
    )

    elements.append(table)

    document.build(elements)

    output.seek(0)

    return output

