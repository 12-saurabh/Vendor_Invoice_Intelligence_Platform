from datetime import datetime

from pydantic import BaseModel



class AuditResponse(BaseModel):

    id: int

    user_id: int

    action: str

    entity: str

    entity_id: int | None

    old_value: str | None

    new_value: str | None

    created_at: datetime


    class Config:
        from_attributes = True