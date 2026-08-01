from app.crud.duplicate import is_duplicate_invoice


def check_duplicate(
    db,
    extracted_data,
    vendor_id
):
    """
    Checks whether the extracted invoice
    already exists.
    """

    invoice_number = extracted_data.get(
        "invoice_number"
    )

    if not invoice_number:
        return False

    return is_duplicate_invoice(
        db,
        invoice_number,
        vendor_id
    )