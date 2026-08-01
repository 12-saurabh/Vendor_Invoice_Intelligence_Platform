from pydantic import BaseModel



class InvoiceUploadResponse(BaseModel):

    filename: str

    invoice_number: str | None

    amount: float | None

    message: str