from app.schemas.prediction import PredictionCreate


def predict_invoice_risk(invoice):

    amount = invoice.amount

    if amount > 10000:

        risk_score = 0.92
        prediction = "High Risk"
        confidence = 0.95

    elif amount > 5000:

        risk_score = 0.60
        prediction = "Medium Risk"
        confidence = 0.87

    else:

        risk_score = 0.15
        prediction = "Low Risk"
        confidence = 0.98

    return PredictionCreate(

        invoice_id=invoice.id,

        risk_score=risk_score,

        prediction=prediction,

        confidence=confidence
    )