from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.user import User
from app.models.invoice import Invoice
from app.models.notification import Notification


def get_system_statistics(db: Session):

    return {

        "users": db.query(User).count(),

        "invoices": db.query(Invoice).count(),

        "notifications": db.query(Notification).count(),

        "completed": db.query(Invoice).filter(
            Invoice.status == "Completed"
        ).count(),

        "processing": db.query(Invoice).filter(
            Invoice.status == "Processing"
        ).count(),

        "manual_review": db.query(Invoice).filter(
            Invoice.status == "Pending Manual Review"
        ).count(),

        "fraud_review": db.query(Invoice).filter(
            Invoice.status == "Fraud Review"
        ).count()
    }


def get_all_users(db: Session):

    return db.query(User).all()


def get_all_invoices(db: Session):

    return db.query(Invoice).order_by(
        Invoice.id.desc()
    ).all()