from pydantic import BaseModel


class DocumentResponse(BaseModel):

    id: int
    invoice_id: int
    file_name: str
    file_path: str


    class Config:
        from_attributes = True