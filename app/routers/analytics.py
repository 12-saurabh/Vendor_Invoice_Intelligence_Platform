from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user

from app.models.user import User

from app.services.dashboard_service import get_dashboard_summary

from app.cache import get_cache, set_cache


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# =====================================================
# Dashboard Summary API
# =====================================================

@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # -------------------------
    # Check Redis Cache
    # -------------------------

    cached_data = get_cache(
        "dashboard_summary"
    )


    if cached_data:

        return cached_data



    # -------------------------
    # Database Calculation
    # -------------------------

    data = get_dashboard_summary(
        db
    )


    # -------------------------
    # Save Cache
    # -------------------------

    set_cache(
        "dashboard_summary",
        data,
        expire=300
    )


    return data