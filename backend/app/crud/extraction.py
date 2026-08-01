from sqlalchemy.orm import Session

from app.models.invoice import Invoice


def save_extracted_invoice_data(
    db: Session,
    invoice_id: int,
    extracted_data: dict
):
    """
    Save AI extracted invoice data
    into the Invoice table.
    """

    invoice = (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id)
        .first()
    )

    if not invoice:
        return None

    invoice.vendor_name = extracted_data.get(
        "vendor_name"
    )

    invoice.extracted_invoice_number = extracted_data.get(
        "invoice_number"
    )

    invoice.extracted_amount = extracted_data.get(
        "amount"
    )

    invoice.invoice_date = extracted_data.get(
        "invoice_date"
    )

    invoice.due_date = extracted_data.get(
        "due_date"
    )

    db.commit()

    db.refresh(invoice)

    return invoice