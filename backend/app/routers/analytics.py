from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.invoice import Invoice

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/summary")
def analytics_summary(db: Session = Depends(get_db)):

    total_invoices = db.query(Invoice).count()

    total_amount = (
        db.query(func.sum(Invoice.amount))
        .scalar()
        or 0
    )

    pending = (
        db.query(Invoice)
        .filter(Invoice.status == "Pending")
        .count()
    )

    approved = (
        db.query(Invoice)
        .filter(Invoice.status == "Approved")
        .count()
    )

    rejected = (
        db.query(Invoice)
        .filter(Invoice.status == "Rejected")
        .count()
    )

    return {
        "total_invoices": total_invoices,
        "total_amount": float(total_amount),
        "pending": pending,
        "approved": approved,
        "rejected": rejected
    }