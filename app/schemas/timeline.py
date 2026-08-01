from datetime import datetime

from pydantic import BaseModel



class TimelineResponse(BaseModel):

    event: str

    performed_by: str

    old_value: str | None = None

    new_value: str | None = None

    timestamp: datetime