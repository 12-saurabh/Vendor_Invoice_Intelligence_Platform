from datetime import date

from fastapi import APIRouter, Depends, Query

from sqlalchemy.orm import Session

from app.dependencies import (
    get_db,
    get_current_user
)

from app.models.user import User

from app.crud.search import search_invoices


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/invoices")
def search(

    invoice_number: str | None = None,

    vendor: str | None = None,

    status: str | None = None,

    risk_level: str | None = None,

    min_amount: float | None = None,

    max_amount: float | None = None,

    start_date: date | None = None,

    end_date: date | None = None,

    page: int = Query(1, ge=1),

    page_size: int = Query(10, ge=1, le=100),

    sort_by: str = "id",

    order: str = "desc",

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return search_invoices(

        db=db,

        invoice_number=invoice_number,

        vendor=vendor,

        status=status,

        risk_level=risk_level,

        min_amount=min_amount,

        max_amount=max_amount,

        start_date=start_date,

        end_date=end_date,

        page=page,

        page_size=page_size,

        sort_by=sort_by,

        order=order
    )