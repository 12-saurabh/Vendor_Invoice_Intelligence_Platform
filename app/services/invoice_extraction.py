import uuid
import re
from datetime import datetime, date, timedelta
from uuid import uuid4


def extract_invoice_details(text: str):

    invoice_number = None
    amount = None
    invoice_date = None
    due_date = None

    invoice_match = re.search(
        r"(?:Invoice\s*(?:Number|No|#)?[:\s]*)\s*([A-Za-z0-9\-\/]+)",
        text,
        re.IGNORECASE
    )

    amount_match = re.search(
        r"Amount[:\s]*\$?([\d,]+(?:\.\d{2})?)",
        text,
        re.IGNORECASE
    )

    date_match = re.search(
        r"Date[:\s]*(\d{2}-\d{2}-\d{4})",
        text,
        re.IGNORECASE
    )

    due_match = re.search(
        r"Due\s*Date[:\s]*(\d{2}-\d{2}-\d{4})",
        text,
        re.IGNORECASE
    )

    if invoice_match:
        invoice_number = invoice_match.group(1).strip()

    else:
        # Generate a unique invoice number if none is found
        invoice_number = f"INV-{uuid4().hex[:8].upper()}"

    if amount_match:
        amount = float(
            amount_match.group(1).replace(",", "")
        )
    else:
        amount = 0.0

    if date_match:
        invoice_date = datetime.strptime(
            date_match.group(1),
            "%d-%m-%Y"
        ).date()
    else:
        invoice_date = date.today()

    if due_match:
        due_date = datetime.strptime(
            due_match.group(1),
            "%d-%m-%Y"
        ).date()
    else:
        due_date = invoice_date + timedelta(days=30)

    return {
        "invoice_number": f"INV-{uuid.uuid4().hex[:8].upper()}",
        "amount": amount,
        "currency": "USD",
        "invoice_date": invoice_date,
        "due_date": due_date,
        "status": "Pending"
    }