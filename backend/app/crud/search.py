from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from app.models.invoice import Invoice
from app.models.vendor import Vendor


def search_invoices(
    db: Session,
    invoice_number: str = None,
    vendor: str = None,
    status: str = None,
    risk_level: str = None,
    min_amount: float = None,
    max_amount: float = None,
    start_date=None,
    end_date=None,
    page: int = 1,
    page_size: int = 10,
    sort_by: str = "id",
    order: str = "desc"
):

    query = db.query(Invoice).join(
        Vendor,
        Invoice.vendor_id == Vendor.id
    )

    if invoice_number:
        query = query.filter(
            Invoice.invoice_number.ilike(f"%{invoice_number}%")
        )

    if vendor:
        query = query.filter(
            Vendor.name.ilike(f"%{vendor}%")
        )

    if status:
        query = query.filter(
            Invoice.status == status
        )

    if risk_level:
        query = query.filter(
            Invoice.risk_level == risk_level
        )

    if min_amount is not None:
        query = query.filter(
            Invoice.amount >= min_amount
        )

    if max_amount is not None:
        query = query.filter(
            Invoice.amount <= max_amount
        )

    if start_date:
        query = query.filter(
            Invoice.invoice_date >= start_date
        )

    if end_date:
        query = query.filter(
            Invoice.invoice_date <= end_date
        )

    column = getattr(
        Invoice,
        sort_by,
        Invoice.id
    )

    if order == "asc":
        query = query.order_by(asc(column))
    else:
        query = query.order_by(desc(column))

    total = query.count()

    invoices = query.offset(
        (page - 1) * page_size
    ).limit(page_size).all()

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "results": invoices
    }