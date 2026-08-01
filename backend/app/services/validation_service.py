from typing import List


def validate_invoice(extracted_data: dict) -> List[str]:
    """
    Validate extracted invoice data.

    Returns:
        List of validation errors.
        Empty list means invoice is valid.
    """

    errors = []

    # -------------------------
    # Vendor
    # -------------------------

    if not extracted_data.get("vendor_name"):
        errors.append("Vendor name missing")

    # -------------------------
    # Invoice Number
    # -------------------------

    if not extracted_data.get("invoice_number"):
        errors.append("Invoice number missing")

    # -------------------------
    # Amount
    # -------------------------

    amount = extracted_data.get("amount")

    if amount is None:
        errors.append("Invoice amount missing")

    elif amount <= 0:
        errors.append("Invoice amount must be greater than zero")

    # -------------------------
    # Dates
    # -------------------------

    if not extracted_data.get("invoice_date"):
        errors.append("Invoice date missing")

    if not extracted_data.get("due_date"):
        errors.append("Due date missing")

    return errors