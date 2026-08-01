from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.vendor import Vendor
from app.schemas.vendor import VendorCreate, VendorUpdate
from app.models.invoice import Invoice
from app.models.prediction import Prediction

def create_vendor(
    db: Session,
    vendor: VendorCreate,
):
    db_vendor = Vendor(
        name=vendor.name,
        email=vendor.email,
        phone=vendor.phone,
    )

    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)

    return db_vendor


def get_vendor(
    db: Session,
    vendor_id: int,
):
    return (
        db.query(Vendor)
        .filter(Vendor.id == vendor_id)
        .first()
    )


def get_all_vendors(db: Session):
    return db.query(Vendor).all()


def update_vendor(
    db: Session,
    db_vendor: Vendor,
    vendor_update: VendorUpdate,
):
    db_vendor.name = vendor_update.name
    db_vendor.email = vendor_update.email
    db_vendor.phone = vendor_update.phone

    db.commit()
    db.refresh(db_vendor)

    return db_vendor


def delete_vendor(
    db: Session,
    db_vendor: Vendor,
):
    db.delete(db_vendor)
    db.commit()
    
def get_vendor_statistics(

    db: Session,

    vendor_id: int

):


    total_invoice = (

        db.query(Invoice)

        .filter(
            Invoice.vendor_id == vendor_id
        )

        .count()

    )



    total_amount = (

        db.query(
            func.sum(
                Invoice.amount
            )
        )

        .filter(
            Invoice.vendor_id == vendor_id
        )

        .scalar()

    )


    return {


        "vendor_id":

            vendor_id,


        "invoice_count":

            total_invoice,


        "total_amount":

            total_amount or 0

    }