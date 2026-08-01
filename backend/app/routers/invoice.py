from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import Optional
from datetime import date

from app.dependencies import (
    get_db,
    get_current_user
)

from app.models.user import User

from app.crud.audit import create_audit_log

from app.crud.invoice import (
    get_invoice_by_id,
    update_invoice_status,
    delete_invoice,
    search_invoices,
    get_invoices_paginated
)


router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)



# -------------------------------------------------
# Role checker
# -------------------------------------------------

def check_roles(*allowed_roles):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role not in allowed_roles:

            raise HTTPException(
                status_code=403,
                detail="Permission denied"
            )

        return current_user


    return role_checker



# -------------------------------------------------
# Get all invoices
# -------------------------------------------------

@router.get("/")
def get_invoices(

    page: int = 1,

    limit: int = 10,

    sort_by: str = "id",

    order: str = "asc",

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_invoices_paginated(

        db,

        page,

        limit,

        sort_by,

        order

    )





# -------------------------------------------------
# Advanced Search invoices
# -------------------------------------------------

@router.get(
    "/search",
    response_model=dict
)
def search_invoice(

    invoice_number: Optional[str] = None,

    keyword: Optional[str] = None,

    status: Optional[str] = None,

    vendor_id: Optional[int] = None,

    min_amount: Optional[float] = None,

    max_amount: Optional[float] = None,

    start_date: Optional[date] = None,

    end_date: Optional[date] = None,


    page: int = 1,

    limit: int = 10,

    sort_by: Optional[str] = None,


    db: Session = Depends(get_db),


    current_user: User = Depends(get_current_user)

):


    return search_invoices(

        db,

        invoice_number,

        keyword,

        status,

        vendor_id,

        min_amount,

        max_amount,

        start_date,

        end_date,

        page,

        limit,

        sort_by

    )





# -------------------------------------------------
# Get invoice by ID
# -------------------------------------------------

@router.get("/{invoice_id}")
def get_invoice(

    invoice_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    invoice = get_invoice_by_id(

        db,

        invoice_id

    )


    if not invoice:

        raise HTTPException(

            status_code=404,

            detail="Invoice not found"

        )


    return invoice






# -------------------------------------------------
# Update invoice status
# -------------------------------------------------

@router.put("/{invoice_id}/status")
def update_status(

    invoice_id: int,

    status: str,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        check_roles(
            "admin",
            "accountant"
        )
    )

):


    invoice = get_invoice_by_id(
        db,
        invoice_id
    )


    if not invoice:

        raise HTTPException(

            status_code=404,

            detail="Invoice not found"

        )


    old_status = invoice.status


    if old_status == status:

        raise HTTPException(

            status_code=400,

            detail="Invoice already has this status"

        )


    invoice = update_invoice_status(

        db,

        invoice_id,

        status

    )



    create_audit_log(

        db,

        user_id=current_user.id,

        action="UPDATE_STATUS",

        entity="Invoice",

        entity_id=invoice_id,

        old_value=old_status,

        new_value=status

    )


    return invoice






# -------------------------------------------------
# Delete invoice
# -------------------------------------------------

@router.delete("/{invoice_id}")
def remove_invoice(

    invoice_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        check_roles("admin")
    )

):


    invoice = get_invoice_by_id(

        db,

        invoice_id

    )


    if not invoice:

        raise HTTPException(

            status_code=404,

            detail="Invoice not found"

        )


    invoice_number = invoice.invoice_number



    delete_invoice(

        db,

        invoice_id

    )



    create_audit_log(

        db,

        user_id=current_user.id,

        action="DELETE",

        entity="Invoice",

        entity_id=invoice_id,

        old_value=invoice_number,

        new_value="Deleted"

    )



    return {

        "message": "Invoice deleted successfully"

    }