from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey
)

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database import Base



class AuditLog(Base):

    __tablename__ = "audit_logs"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    action = Column(
        String,
        nullable=False
    )


    entity = Column(
        String,
        nullable=False
    )


    entity_id = Column(
        Integer,
        nullable=True
    )


    old_value = Column(
        Text,
        nullable=True
    )


    new_value = Column(
        Text,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    user = relationship(
        "User",
        back_populates="audit_logs"
    )