from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from app.models.invoice import Invoice


# -----------------------------------------
# Create Invoice
# -----------------------------------------

def create_invoice(
    db: Session,
    invoice_data: dict
):

    invoice = Invoice(

        invoice_number=invoice_data.get(
            "invoice_number",
            "UNKNOWN"
        ),

        amount=invoice_data.get(
            "amount",
            0
        ),

        currency=invoice_data.get(
            "currency",
            "USD"
        ),

        vendor_id=invoice_data.get(
            "vendor_id",
            1
        ),

        created_by=invoice_data.get(
            "created_by"
        ),

        file_name=invoice_data.get(
            "file_name"
        ),

        file_path=invoice_data.get(
            "file_path"
        ),

        extracted_text=invoice_data.get(
            "extracted_text"
        ),

        ocr_confidence=invoice_data.get(
            "ocr_confidence"
        ),

        status=invoice_data.get(
            "status",
            "Processing"
        )
    )


    db.add(invoice)

    db.commit()

    db.refresh(invoice)

    return invoice



# -----------------------------------------
# Get Invoice By ID
# -----------------------------------------

def get_invoice_by_id(
    db: Session,
    invoice_id: int
):

    return (
        db.query(Invoice)
        .filter(
            Invoice.id == invoice_id
        )
        .first()
    )



# -----------------------------------------
# Update After OCR Processing
# -----------------------------------------

def update_invoice_after_processing(
    db: Session,
    invoice_id: int,
    extracted_text: str,
    status: str
):

    invoice = get_invoice_by_id(
        db,
        invoice_id
    )


    if not invoice:
        return None


    invoice.extracted_text = extracted_text

    invoice.status = status


    db.commit()

    db.refresh(invoice)


    return invoice



# -----------------------------------------
# Mark Invoice Failed
# -----------------------------------------

def mark_invoice_failed(
    db: Session,
    invoice_id: int,
    error_message: str
):

    invoice = get_invoice_by_id(
        db,
        invoice_id
    )


    if not invoice:
        return None


    invoice.status = "Failed"

    invoice.processing_error = error_message


    db.commit()

    db.refresh(invoice)


    return invoice



# -----------------------------------------
# Update Invoice Status
# -----------------------------------------

def update_invoice_status(
    db: Session,
    invoice_id: int,
    status: str
):

    invoice = get_invoice_by_id(
        db,
        invoice_id
    )


    if not invoice:
        return None


    invoice.status = status


    db.commit()

    db.refresh(invoice)


    return invoice



# -----------------------------------------
# Get Approval History
# -----------------------------------------

def get_approval_history(
    db: Session,
    invoice_id: int
):

    invoice = get_invoice_by_id(
        db,
        invoice_id
    )


    if not invoice:
        return []


    return invoice.approval_history



# -----------------------------------------
# Get All Invoices
# -----------------------------------------

def get_all_invoices(
    db: Session
):

    return (
        db.query(Invoice)
        .all()
    )



# -----------------------------------------
# Delete Invoice
# -----------------------------------------

def delete_invoice(
    db: Session,
    invoice_id: int
):

    invoice = get_invoice_by_id(
        db,
        invoice_id
    )


    if not invoice:
        return None


    db.delete(invoice)

    db.commit()


    return invoice



# -----------------------------------------
# Search Invoices
# -----------------------------------------

def search_invoices(

    db: Session,

    invoice_number=None,

    status=None,

    vendor_id=None,

    min_amount=None,

    max_amount=None,

    page=1,

    limit=10,

    sort_by=None

):


    query = db.query(Invoice)


    if invoice_number:

        query = query.filter(
            Invoice.invoice_number.ilike(
                f"%{invoice_number}%"
            )
        )


    if status:

        query = query.filter(
            Invoice.status == status
        )


    if vendor_id:

        query = query.filter(
            Invoice.vendor_id == vendor_id
        )


    if min_amount is not None:

        query = query.filter(
            Invoice.amount >= min_amount
        )


    if max_amount is not None:

        query = query.filter(
            Invoice.amount <= max_amount
        )


    total = query.count()


    if sort_by == "amount_high":

        query = query.order_by(
            Invoice.amount.desc()
        )


    elif sort_by == "amount_low":

        query = query.order_by(
            Invoice.amount.asc()
        )


    else:

        query = query.order_by(
            Invoice.id.desc()
        )



    invoices = (
        query
        .offset(
            (page - 1) * limit
        )
        .limit(limit)
        .all()
    )


    return {

        "total": total,

        "page": page,

        "limit": limit,

        "data": invoices

    }



# -----------------------------------------
# Pagination
# -----------------------------------------

def get_invoices_paginated(

    db: Session,

    page: int = 1,

    limit: int = 10,

    sort_by: str = "id",

    order: str = "asc"

):


    query = db.query(Invoice)


    total = query.count()


    allowed_fields = {

        "id": Invoice.id,

        "amount": Invoice.amount,

        "status": Invoice.status,

        "invoice_date": Invoice.invoice_date

    }


    sort_column = allowed_fields.get(
        sort_by,
        Invoice.id
    )


    if order == "desc":

        query = query.order_by(
            desc(sort_column)
        )

    else:

        query = query.order_by(
            asc(sort_column)
        )


    invoices = (
        query
        .offset(
            (page - 1) * limit
        )
        .limit(limit)
        .all()
    )


    return {

        "page": page,

        "limit": limit,

        "total": total,

        "data": invoices

    }