from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.dependencies import (
    get_db,
    require_role
)

from app.models.user import User

from app.crud.admin import (
    get_system_statistics,
    get_all_users,
    get_all_invoices
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/statistics")
def statistics(

    db: Session = Depends(get_db),

    admin: User = Depends(require_role("admin"))

):

    return get_system_statistics(db)


@router.get("/users")
def users(

    db: Session = Depends(get_db),

    admin: User = Depends(require_role("admin"))

):

    return get_all_users(db)


@router.get("/invoices")
def invoices(

    db: Session = Depends(get_db),

    admin: User = Depends(require_role("admin"))

):

    return get_all_invoices(db)