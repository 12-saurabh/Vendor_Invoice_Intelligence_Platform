from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database import Base


class ApprovalHistory(Base):

    __tablename__ = "approval_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    invoice_id = Column(
        Integer,
        ForeignKey("invoices.id"),
        nullable=False
    )


    approved_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    action = Column(
        String,
        nullable=False
    )
    # APPROVED / REJECTED


    comment = Column(
        Text,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    # Invoice relationship
    invoice = relationship(
        "Invoice",
        back_populates="approval_history"
    )


    # User who approved/rejected invoice
    approver = relationship(
        "User",
        foreign_keys=[approved_by],
        back_populates="approval_actions"
    )