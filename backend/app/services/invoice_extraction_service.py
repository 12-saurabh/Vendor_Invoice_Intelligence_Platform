import re
from datetime import datetime


def _extract_date(text: str):
    """
    Supports:
    DD/MM/YYYY
    DD-MM-YYYY
    YYYY-MM-DD
    """

    patterns = [

        r"\d{2}/\d{2}/\d{4}",

        r"\d{2}-\d{2}-\d{4}",

        r"\d{4}-\d{2}-\d{2}"

    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:

            value = match.group()

            for fmt in (

                "%d/%m/%Y",

                "%d-%m-%Y",

                "%Y-%m-%d"

            ):

                try:

                    return datetime.strptime(

                        value,

                        fmt

                    ).date()

                except ValueError:

                    pass

    return None


def extract_invoice_data(ocr_text: str):

    """
    Extract structured invoice information
    from OCR text.
    """

    data = {

        "vendor_name": None,

        "invoice_number": None,

        "amount": None,

        "invoice_date": None,

        "due_date": None

    }

    if not ocr_text:

        return data

    # -------------------------------------
    # Invoice Number
    # -------------------------------------

    invoice_match = re.search(

        r"Invoice\s*(Number|No\.?|#)?\s*[:\-]?\s*([A-Za-z0-9\-]+)",

        ocr_text,

        re.IGNORECASE

    )

    if invoice_match:

        data["invoice_number"] = invoice_match.group(2)

    # -------------------------------------
    # Vendor
    # -------------------------------------

    vendor_match = re.search(

        r"Vendor\s*[:\-]?\s*(.+)",

        ocr_text,

        re.IGNORECASE

    )

    if vendor_match:

        data["vendor_name"] = vendor_match.group(1).strip()

    # -------------------------------------
    # Amount
    # -------------------------------------

    amount_match = re.search(

        r"(Total|Amount|Grand Total)\s*[:\-]?\s*\$?\s*([\d,]+\.?\d*)",

        ocr_text,

        re.IGNORECASE

    )

    if amount_match:

        try:

            data["amount"] = float(

                amount_match.group(2).replace(",", "")

            )

        except:

            pass

    # -------------------------------------
    # Invoice Date
    # -------------------------------------

    invoice_date_match = re.search(

        r"Invoice Date\s*[:\-]?\s*(.+)",

        ocr_text,

        re.IGNORECASE

    )

    if invoice_date_match:

        data["invoice_date"] = _extract_date(

            invoice_date_match.group(1)

        )

    # -------------------------------------
    # Due Date
    # -------------------------------------

    due_date_match = re.search(

        r"Due Date\s*[:\-]?\s*(.+)",

        ocr_text,

        re.IGNORECASE

    )

    if due_date_match:

        data["due_date"] = _extract_date(

            due_date_match.group(1)

        )

    return data