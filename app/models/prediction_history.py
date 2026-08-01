from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class PredictionHistory(Base):

    __tablename__ = "prediction_history"


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


    risk = Column(
        String,
        nullable=False
    )


    confidence = Column(
        Float,
        nullable=False
    )


    # invoice = relationship(
    #     "Invoice",
    #     back_populates="predictions_history"
    # )