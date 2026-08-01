from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.dependencies import (
    get_db,
    get_current_user
)

from app.models.user import User

from app.models.audit_log import AuditLog

from app.models.invoice import Invoice

from app.schemas.timeline import TimelineResponse



router = APIRouter(
    prefix="/invoices",
    tags=["Invoice Timeline"]
)



@router.get(
    "/{invoice_id}/timeline",
    response_model=list[TimelineResponse]
)
def get_invoice_timeline(

    invoice_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    invoice = (
        db.query(Invoice)
        .filter(
            Invoice.id == invoice_id
        )
        .first()
    )


    if not invoice:

        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )


    logs = (
        db.query(AuditLog)
        .filter(
            AuditLog.entity == "Invoice",
            AuditLog.entity_id == invoice_id
        )
        .order_by(
            AuditLog.created_at.asc()
        )
        .all()
    )


    timeline = []


    for log in logs:

        timeline.append(

            TimelineResponse(

                event=log.action,

                performed_by=log.user.email,

                old_value=log.old_value,

                new_value=log.new_value,

                timestamp=log.created_at

            )

        )


    return timeline