from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session


from app.dependencies import (
    get_db,
    get_current_user
)


from app.models.user import User


from app.crud.approval import (

    create_approval_history,

    get_approval_history_by_invoice,

    update_invoice_status,

    get_pending_approval_invoices

)



from app.schemas.approval import (
    InvoiceApprovalRequest
)



router = APIRouter(

    prefix="/approval",

    tags=["Approval Workflow"]

)





# =====================================================
# Get Pending Approval Invoices
# =====================================================

@router.get("/pending")
def pending_invoices(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    invoices = get_pending_approval_invoices(
        db
    )


    return invoices





# =====================================================
# Approve / Reject Invoice
# =====================================================

@router.post("/{invoice_id}")
def approve_invoice(

    invoice_id: int,

    request: InvoiceApprovalRequest,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    # Role validation

    if current_user.role not in [

        "admin",

        "approver"

    ]:

        raise HTTPException(

            status_code=status.HTTP_403_FORBIDDEN,

            detail="User not allowed to approve invoices"

        )





    if request.action not in [

        "APPROVED",

        "REJECTED"

    ]:

        raise HTTPException(

            status_code=400,

            detail="Invalid approval action"

        )





    invoice = update_invoice_status(

        db,

        invoice_id,

        request.action

    )



    if not invoice:


        raise HTTPException(

            status_code=404,

            detail="Invoice not found"

        )





    history = create_approval_history(

        db,

        invoice_id,

        current_user.id,

        request.action,

        request.comment

    )





    return {


        "message": "Invoice status updated successfully",


        "invoice_id": invoice_id,


        "status": request.action,


        "approved_by": current_user.email,


        "approval_history_id": history.id


    }







# =====================================================
# Approval History
# =====================================================

@router.get("/history/{invoice_id}")
def approval_history(

    invoice_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    history = get_approval_history_by_invoice(

        db,

        invoice_id

    )


    return history