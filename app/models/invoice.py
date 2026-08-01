from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Date,
    Text,
    DateTime,
    Boolean
)

from app.services.fraud_service import calculate_invoice_risk
from sqlalchemy.orm import relationship

from datetime import datetime

from app.database import Base


class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    invoice_number = Column(
        String,
        unique=True,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    currency = Column(
        String,
        default="USD"
    )

    invoice_date = Column(
        Date,
        nullable=True
    )

    due_date = Column(
        Date,
        nullable=True
    )

    status = Column(
        String,
        default="Pending",
        nullable=False
    )

    vendor_id = Column(
        Integer,
        ForeignKey("vendors.id"),
        nullable=False
    )

    # ----------------------------
    # User who uploaded invoice
    # ----------------------------

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    # ----------------------------
    # OCR Fields
    # ----------------------------

    file_name = Column(
        String,
        nullable=True
    )

    file_path = Column(
        String,
        nullable=True
    )

    extracted_text = Column(
        Text,
        nullable=True
    )

    ocr_confidence = Column(
        Float,
        nullable=True
    )

    processing_error = Column(
        Text,
        nullable=True
    )

    # ----------------------------
    # Processing timestamps
    # ----------------------------

    processing_started_at = Column(
        DateTime,
        nullable=True
    )

    processing_completed_at = Column(
        DateTime,
        nullable=True
    )

    # ----------------------------
    # Created timestamp
    # ----------------------------

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    
    vendor_name = Column(
        String,
        nullable=True
    )


    extracted_invoice_number = Column(
        String,
        nullable=True
    )


    extracted_amount = Column(
        Float,
        nullable=True
    )
    
    risk_score = Column(Float, default=0)

    risk_level = Column(
        String,
        default="Low"
    )
    
    

    fraud_detected = Column(
        Boolean,
        default=False
    )


    extracted_invoice_date = Column(
        Date,
        nullable=True
    )


    extracted_due_date = Column(
        Date,
        nullable=True
    )
    
    duplicate_invoice = Column(
        Boolean,
        default=False
    )

    # ----------------------------
    # Relationships
    # ----------------------------

    vendor = relationship(
        "Vendor",
        back_populates="invoices"
    )

    uploader = relationship(
        "User",
        foreign_keys=[created_by]
    )

    predictions = relationship(
        "Prediction",
        back_populates="invoice",
        cascade="all, delete-orphan"
    )

    approval_history = relationship(
        "ApprovalHistory",
        back_populates="invoice",
        cascade="all, delete-orphan"
    )

    documents = relationship(
        "InvoiceDocument",
        back_populates="invoice",
        cascade="all, delete-orphan"
    )