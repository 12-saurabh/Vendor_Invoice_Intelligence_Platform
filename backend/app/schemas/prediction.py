from pydantic import BaseModel


class PredictionCreate(BaseModel):

    invoice_id: int
    risk_score: float
    prediction: str
    confidence: float


class PredictionResponse(PredictionCreate):

    id: int

    class Config:
        from_attributes = True