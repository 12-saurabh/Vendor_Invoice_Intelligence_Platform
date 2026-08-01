from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.dependencies import (
    get_db,
    get_current_user
)


from app.models.user import User

from app.models.audit_log import AuditLog


from app.schemas.audit import AuditResponse



router = APIRouter(

    prefix="/audit",

    tags=["Audit"]

)



@router.get(
    "/logs",
    response_model=list[AuditResponse]
)
def get_audit_logs(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    return (
        db.query(AuditLog)
        .order_by(
            AuditLog.created_at.desc()
        )
        .all()
    )