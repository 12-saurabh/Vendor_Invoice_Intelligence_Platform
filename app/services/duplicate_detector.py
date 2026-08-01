from sqlalchemy.orm import Session

from app.models.invoice import Invoice


def check_duplicate_invoice(
    db: Session,
    invoice_number: str,
    vendor_id: int,
    amount: float
):

    duplicate = (
        db.query(Invoice)
        .filter(
            Invoice.invoice_number == invoice_number,
            Invoice.vendor_id == vendor_id,
            Invoice.amount == amount
        )
        .first()
    )

    return duplicate