from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Vendor(Base):

    __tablename__ = "vendors"


    id = Column(
        Integer,
        primary_key=True
    )


    name = Column(
        String,
        nullable=False
    )


    email = Column(
        String,
        nullable=True
    )


    phone = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    invoices = relationship(
        "Invoice",
        back_populates="vendor"
    )