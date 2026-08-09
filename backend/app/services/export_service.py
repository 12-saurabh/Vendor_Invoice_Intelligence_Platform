import os
import tempfile

import pandas as pd

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
)


def invoice_to_dict(invoice):
    return {
        "Invoice ID": invoice.id,
        "Invoice Number": invoice.invoice_number,
        "Vendor": invoice.vendor_name,
        "Amount": invoice.amount,
        "Currency": invoice.currency,
        "Status": invoice.status,
        "Risk Score": invoice.risk_score,
        "Risk Level": invoice.risk_level,
        "Fraud Detected": invoice.fraud_detected,
        "Duplicate Invoice": invoice.duplicate_invoice,
    }


def export_csv(invoices):
    data = [
        invoice_to_dict(invoice)
        for invoice in invoices
    ]

    df = pd.DataFrame(data)

    fd, path = tempfile.mkstemp(
        suffix=".csv",
        prefix="invoices_"
    )

    os.close(fd)

    df.to_csv(path, index=False)

    return path


def export_excel(invoices):
    data = [
        invoice_to_dict(invoice)
        for invoice in invoices
    ]

    df = pd.DataFrame(data)

    fd, path = tempfile.mkstemp(
        suffix=".xlsx",
        prefix="invoices_"
    )

    os.close(fd)

    df.to_excel(
        path,
        index=False,
        engine="openpyxl"
    )

    return path


def export_pdf(invoices):
    fd, path = tempfile.mkstemp(
        suffix=".pdf",
        prefix="invoices_"
    )

    os.close(fd)

    document = SimpleDocTemplate(
        path,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20,
    )

    styles = getSampleStyleSheet()

    title = Paragraph(
        "Vendor Invoice Report",
        styles["Title"]
    )

    rows = [
        [
            "ID",
            "Invoice",
            "Vendor",
            "Amount",
            "Currency",
            "Status",
            "Risk",
            "Risk Level",
        ]
    ]

    for invoice in invoices:
        rows.append(
            [
                str(invoice.id),
                str(invoice.invoice_number),
                str(invoice.vendor_name or ""),
                str(invoice.amount),
                str(invoice.currency or ""),
                str(invoice.status),
                str(invoice.risk_score or 0),
                str(invoice.risk_level or "Low"),
            ]
        )

    table = Table(
        rows,
        repeatRows=1
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
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8,
                ),
                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER",
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE",
                ),
            ]
        )
    )

    document.build(
        [
            title,
            table,
        ]
    )

    return path

