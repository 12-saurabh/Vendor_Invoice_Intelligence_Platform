from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud.invoice import (
    create_invoice,
    delete_invoice,
    get_all_invoices,
    get_invoice,
    get_invoice_by_number,
    update_invoice,
)
from app.crud.vendor import get_vendor
from app.schemas.invoice import InvoiceCreate, InvoiceUpdate


def create_invoice_service(db: Session, invoice: InvoiceCreate):
    # Check vendor exists
    vendor = get_vendor(db, invoice.vendor_id)

    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found",
        )

    # Check duplicate invoice number
    existing_invoice = get_invoice_by_number(
        db,
        invoice.invoice_number,
    )

    if existing_invoice:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invoice number already exists",
        )

    return create_invoice(db, invoice)


def get_invoice_service(db: Session, invoice_id: int):
    invoice = get_invoice(db, invoice_id)

    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found",
        )

    return invoice


def get_all_invoices_service(db: Session):
    return get_all_invoices(db)


def update_invoice_service(
    db: Session,
    invoice_id: int,
    invoice_update: InvoiceUpdate,
):
    db_invoice = get_invoice(db, invoice_id)

    if not db_invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found",
        )

    return update_invoice(
        db,
        db_invoice,
        invoice_update,
    )


def delete_invoice_service(
    db: Session,
    invoice_id: int,
):
    db_invoice = get_invoice(db, invoice_id)

    if not db_invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found",
        )

    delete_invoice(
        db,
        db_invoice,
    )

    return {
        "message": "Invoice deleted successfully"
    }