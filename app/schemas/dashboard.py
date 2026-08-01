from pydantic import BaseModel


class DashboardResponse(BaseModel):

    total_invoices:int

    total_amount:float

    status:dict

    high_risk_invoices:int