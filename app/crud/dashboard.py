from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.models.prediction import Prediction
from app.models.vendor import Vendor

from app.cache import (
    get_cache,
    set_cache
)



# ---------------------------------------
# Dashboard Summary (Redis Cached)
# ---------------------------------------

def get_dashboard_summary(
    db: Session
):

    cache_key = "dashboard_summary"


    cached_data = get_cache(
        cache_key
    )


    if cached_data:
        return cached_data



    total_invoices = (
        db.query(Invoice)
        .count()
    )



    pending = (
        db.query(Invoice)
        .filter(
            Invoice.status == "PENDING_APPROVAL"
        )
        .count()
    )



    processing = (
        db.query(Invoice)
        .filter(
            Invoice.status == "PROCESSING"
        )
        .count()
    )



    approved = (
        db.query(Invoice)
        .filter(
            Invoice.status == "APPROVED"
        )
        .count()
    )



    rejected = (
        db.query(Invoice)
        .filter(
            Invoice.status == "REJECTED"
        )
        .count()
    )



    total_amount = (
        db.query(
            func.coalesce(
                func.sum(Invoice.amount),
                0
            )
        )
        .scalar()
    )



    high_risk = (
        db.query(Prediction)
        .filter(
            Prediction.prediction == "High Risk"
        )
        .count()
    )



    medium_risk = (
        db.query(Prediction)
        .filter(
            Prediction.prediction == "Medium Risk"
        )
        .count()
    )



    low_risk = (
        db.query(Prediction)
        .filter(
            Prediction.prediction == "Low Risk"
        )
        .count()
    )



    data = {

        "total_invoices": total_invoices,

        "total_amount": float(total_amount),


        "invoice_status": {

            "pending": pending,

            "processing": processing,

            "approved": approved,

            "rejected": rejected

        },


        "risk": {

            "high": high_risk,

            "medium": medium_risk,

            "low": low_risk

        }

    }



    set_cache(

        cache_key,

        data,

        expire=300

    )


    return data





# ---------------------------------------
# Monthly Invoice Statistics
# ---------------------------------------

def get_monthly_statistics(
    db: Session
):

    cache_key = "monthly_statistics"


    cached_data = get_cache(
        cache_key
    )


    if cached_data:
        return cached_data



    result = (

        db.query(

            func.to_char(
                Invoice.invoice_date,
                "YYYY-MM"
            ).label("month"),


            func.count(
                Invoice.id
            ).label("count")

        )

        .filter(
            Invoice.invoice_date.isnot(None)
        )

        .group_by(
            "month"
        )

        .order_by(
            "month"
        )

        .all()

    )



    data = [

        {
            "month": month,
            "count": count
        }

        for month, count in result

    ]



    set_cache(

        cache_key,

        data,

        expire=300

    )


    return data





# ---------------------------------------
# Vendor Statistics
# ---------------------------------------

def get_vendor_statistics(
    db: Session
):

    cache_key = "vendor_statistics"


    cached_data = get_cache(
        cache_key
    )


    if cached_data:
        return cached_data



    result = (

        db.query(

            Vendor.name,

            func.count(
                Invoice.id
            ).label("count")

        )

        .join(

            Invoice,

            Vendor.id == Invoice.vendor_id

        )

        .group_by(
            Vendor.name
        )

        .order_by(

            func.count(
                Invoice.id
            ).desc()

        )

        .all()

    )



    data = [

        {
            "vendor": vendor,
            "count": count
        }

        for vendor, count in result

    ]



    set_cache(

        cache_key,

        data,

        expire=300

    )


    return data





# ---------------------------------------
# Risk Statistics
# ---------------------------------------

def get_risk_statistics(
    db: Session
):

    cache_key = "risk_statistics"


    cached_data = get_cache(
        cache_key
    )


    if cached_data:
        return cached_data



    result = (

        db.query(

            Prediction.prediction,

            func.count(
                Prediction.id
            )

        )

        .group_by(
            Prediction.prediction
        )

        .all()

    )



    data = {

        prediction: count

        for prediction, count in result

    }



    set_cache(

        cache_key,

        data,

        expire=300

    )


    return data