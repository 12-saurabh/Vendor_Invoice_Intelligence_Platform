from sqlalchemy.orm import Session

from app.models.invoice import Invoice


def is_duplicate_invoice(
    db: Session,
    invoice_number: str,
    vendor_id: int
):
    """
    Returns True if an invoice already exists
    with the same invoice number and vendor.
    """

    invoice = (
        db.query(Invoice)
        .filter(
            Invoice.invoice_number == invoice_number,
            Invoice.vendor_id == vendor_id
        )
        .first()
    )

    return invoice is not None