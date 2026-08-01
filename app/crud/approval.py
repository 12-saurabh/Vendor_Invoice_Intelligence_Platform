from sqlalchemy.orm import Session

from app.models.approval_history import ApprovalHistory
from app.models.invoice import Invoice
from app.models.user import User



# =====================================================
# Create Approval History
# =====================================================

def create_approval_history(

    db: Session,

    invoice_id: int,

    approved_by: int,

    action: str,

    comment: str | None = None

):

    history = ApprovalHistory(

        invoice_id=invoice_id,

        approved_by=approved_by,

        action=action,

        comment=comment

    )


    db.add(history)

    db.commit()

    db.refresh(history)


    return history





# =====================================================
# Get Approval History By Invoice
# =====================================================

def get_approval_history_by_invoice(

    db: Session,

    invoice_id: int

):


    return (

        db.query(
            ApprovalHistory
        )

        .filter(
            ApprovalHistory.invoice_id == invoice_id
        )

        .order_by(
            ApprovalHistory.created_at.desc()
        )

        .all()

    )





# =====================================================
# Update Invoice Status
# =====================================================

def update_invoice_status(

    db: Session,

    invoice_id: int,

    status: str

):


    invoice = (

        db.query(
            Invoice
        )

        .filter(
            Invoice.id == invoice_id
        )

        .first()

    )


    if not invoice:

        return None



    invoice.status = status


    db.commit()

    db.refresh(invoice)


    return invoice





# =====================================================
# Get Pending Approval Invoices
# =====================================================

def get_pending_approval_invoices(

    db: Session

):


    return (

        db.query(
            Invoice
        )

        .filter(

            Invoice.status == "PENDING_APPROVAL"

        )

        .order_by(

            Invoice.created_at.desc()

        )

        .all()

    )





# =====================================================
# Get Approval History With User Details
# =====================================================

def get_invoice_history_details(

    db: Session,

    invoice_id: int

):


    return (

        db.query(

            ApprovalHistory

        )

        .join(

            User,

            User.id == ApprovalHistory.approved_by

        )

        .filter(

            ApprovalHistory.invoice_id == invoice_id

        )

        .order_by(

            ApprovalHistory.created_at.desc()

        )

        .all()

    )