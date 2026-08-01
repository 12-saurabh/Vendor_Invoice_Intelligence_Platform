from sqlalchemy.orm import Session

from app.models.invoice import Invoice


def get_all_invoices(db: Session):

    return (
        db.query(Invoice)
        .all()
    )


def get_invoice(db: Session, invoice_id: int):

    return (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id)
        .first()
    )


def delete_invoice(db: Session, invoice_id: int):

    invoice = get_invoice(db, invoice_id)

    if invoice:

        db.delete(invoice)

        db.commit()

    return invoice


def update_status(
    db: Session,
    invoice_id: int,
    status: str
):

    invoice = get_invoice(db, invoice_id)

    if not invoice:

        return None

    invoice.status = status

    db.commit()

    db.refresh(invoice)

    return invoice