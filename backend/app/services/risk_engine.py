from datetime import date


def calculate_risk(invoice):

    score = 0
    reasons = []


    if invoice.amount > 10000:
        score += 30
        reasons.append("Large invoice amount")


    if invoice.currency is None:
        score += 10
        reasons.append("Currency missing")


    if invoice.invoice_date and invoice.due_date:

        if invoice.due_date < invoice.invoice_date:
            score += 40
            reasons.append("Invalid due date")


    if score >= 70:
        prediction = "High Risk"

    elif score >= 30:
        prediction = "Medium Risk"

    else:
        prediction = "Low Risk"


    confidence = min(95, score + 20)

    return {
        "risk_score": score,
        "prediction": prediction,
        "confidence": confidence,
        "reasons": reasons
    }