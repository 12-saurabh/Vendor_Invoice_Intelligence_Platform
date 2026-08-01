from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel



# -----------------------------
# Vendor response
# -----------------------------

class VendorBasicResponse(BaseModel):

    id: int

    name: str


    class Config:
        from_attributes = True




# -----------------------------
# Prediction response
# -----------------------------

class PredictionResponse(BaseModel):

    id: int

    prediction: Optional[str] = None

    confidence: Optional[float] = None


    class Config:
        from_attributes = True





# -----------------------------
# Approval history response
# -----------------------------

class ApprovalHistoryResponse(BaseModel):

    id: int

    action: str

    comment: Optional[str] = None

    approved_by: int

    created_at: datetime


    class Config:
        from_attributes = True






# -----------------------------
# Invoice detailed response
# -----------------------------

class InvoiceDetailResponse(BaseModel):

    id: int

    invoice_number: str

    amount: float

    currency: str

    invoice_date: Optional[date] = None

    due_date: Optional[date] = None

    status: str


    vendor: VendorBasicResponse


    predictions: List[PredictionResponse] = []


    approval_history: List[ApprovalHistoryResponse] = []


    class Config:
        from_attributes = True