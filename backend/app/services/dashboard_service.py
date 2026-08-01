from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.models.user import User


def get_dashboard_summary(
    db: Session
):

    total_invoices = (
        db.query(Invoice)
        .count()
    )


    completed = (
        db.query(Invoice)
        .filter(
            Invoice.status=="Completed"
        )
        .count()
    )


    pending_review = (
        db.query(Invoice)
        .filter(
            Invoice.status.in_(
                [
                    "Pending Manual Review",
                    "Pending Duplicate Review",
                    "Pending Fraud Review"
                ]
            )
        )
        .count()
    )


    rejected = (
        db.query(Invoice)
        .filter(
            Invoice.status=="Rejected"
        )
        .count()
    )


    duplicate = (
        db.query(Invoice)
        .filter(
            Invoice.duplicate_invoice==True
        )
        .count()
    )


    fraud = (
        db.query(Invoice)
        .filter(
            Invoice.fraud_detected==True
        )
        .count()
    )


    return {

        "total_invoices": total_invoices,

        "completed_invoices": completed,

        "pending_review": pending_review,

        "rejected_invoices": rejected,

        "duplicate_invoices": duplicate,

        "fraud_detected": fraud

    }