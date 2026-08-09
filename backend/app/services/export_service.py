import os
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)


def export_csv(invoices):
    data = []

    for invoice in invoices:
        data.append({
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
        })

    df = pd.DataFrame(data)

    path = os.path.join(EXPORT_DIR, "invoices.csv")
    df.to_csv(path, index=False)

    return path


def export_excel(invoices):
    data = []

    for invoice in invoices:
        data.append({
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
        })

    df = pd.DataFrame(data)

    path = os.path.join(EXPORT_DIR, "invoices.xlsx")
    df.to_excel(path, index=False)

    return path


def export_pdf(invoices):
    path = os.path.join(EXPORT_DIR, "invoices.pdf")

    rows = [
        [
            "ID",
            "Invoice",
            "Vendor",
            "Amount",
            "Currency",
            "Status",
            "Risk",
            "Risk Level"
        ]
    ]

    for invoice in invoices:
        rows.append([
            str(invoice.id),
            str(invoice.invoice_number),
            str(invoice.vendor_name or ""),
            str(invoice.amount),
            str(invoice.currency or ""),
            str(invoice.status),
            str(invoice.risk_score or 0),
            str(invoice.risk_level or "Low"),
        ])

    pdf = SimpleDocTemplate(path)

    table = Table(rows)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
        ])
    )

    pdf.build([table])

    return path