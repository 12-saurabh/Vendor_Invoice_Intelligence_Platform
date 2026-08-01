from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.dependencies import (
    get_db,
    get_current_user
)

from app.models.user import User

from app.crud.notification import (
    get_notifications,
    mark_notification_read
)

router = APIRouter(

    prefix="/notifications",

    tags=["Notifications"]

)


@router.get("/")
def my_notifications(

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    return get_notifications(

        db,

        current_user.id

    )


@router.put("/{notification_id}/read")
def read_notification(

    notification_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):

    notification = mark_notification_read(

        db,

        notification_id

    )

    if not notification:

        raise HTTPException(

            status_code=404,

            detail="Notification not found"

        )

    return {

        "message": "Notification marked as read"

    }