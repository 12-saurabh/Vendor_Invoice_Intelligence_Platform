def calculate_risk(invoice):

    score = 0

    if invoice.amount > 10000:
        score += 40

    if invoice.status.lower() == "pending":
        score += 20

    if invoice.currency != "USD":
        score += 10

    if score >= 70:
        prediction = "High Risk"

    elif score >= 40:
        prediction = "Medium Risk"

    else:
        prediction = "Low Risk"

    confidence = min(score / 100, 0.99)

    return {
        "risk_score": score,
        "prediction": prediction,
        "confidence": confidence
    }