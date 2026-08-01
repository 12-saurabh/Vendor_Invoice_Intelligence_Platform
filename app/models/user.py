from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    # admin
    # accountant
    # auditor
    role = Column(
        String,
        nullable=False,
        default="accountant"
    )

    approval_actions = relationship(
        "ApprovalHistory",
        back_populates="approver",
        overlaps="approval_history"
    )

    audit_logs = relationship(
        "AuditLog",
        back_populates="user"
    )

    notifications = relationship(
        "Notification",
        back_populates="user",
        cascade="all, delete-orphan"
    )