from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class InvoiceDocument(Base):

    __tablename__ = "invoice_documents"


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


    file_name = Column(
        String,
        nullable=False
    )


    file_path = Column(
        String,
        nullable=False
    )