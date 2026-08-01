from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.dependencies import (
    get_db,
    get_current_user
)


from app.models.user import User


from app.crud.dashboard import (
    get_dashboard_summary,
    get_monthly_statistics,
    get_vendor_statistics,
    get_risk_statistics
)



router = APIRouter(

    prefix="/dashboard",

    tags=["Dashboard"]

)




# -----------------------------------
# Dashboard Summary
# -----------------------------------

@router.get("/summary")
def dashboard_summary(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_dashboard_summary(
        db
    )





# -----------------------------------
# Monthly Invoice Statistics
# -----------------------------------

@router.get("/monthly")
def monthly_statistics(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_monthly_statistics(
        db
    )





# -----------------------------------
# Vendor Statistics
# -----------------------------------

@router.get("/vendors")
def vendor_statistics(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_vendor_statistics(
        db
    )





# -----------------------------------
# Risk Statistics
# -----------------------------------

@router.get("/risk")
def risk_statistics(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_risk_statistics(
        db
    )