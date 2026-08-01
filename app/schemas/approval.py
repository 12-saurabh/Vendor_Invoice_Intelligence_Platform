from datetime import datetime

from pydantic import BaseModel



# =====================================================
# Approval Create Schema
# =====================================================

class ApprovalCreate(BaseModel):

    invoice_id: int

    action: str

    comment: str | None = None



# =====================================================
# Approval Response Schema
# =====================================================

class ApprovalResponse(BaseModel):

    id: int

    invoice_id: int

    approved_by: int

    action: str

    comment: str | None

    created_at: datetime


    class Config:

        from_attributes = True



# =====================================================
# Invoice Approval Request
# =====================================================

class InvoiceApprovalRequest(BaseModel):

    action: str

    comment: str | None = None