from datetime import datetime

def calculate_invoice_risk(invoice, extracted_data):

    score = 0

    reasons = []

    # Large Amount

    amount = extracted_data.get("amount", 0)

    if amount > 50000:

        score += 40

        reasons.append("Large invoice amount")

    # Weekend Invoice

    if datetime.today().weekday() >= 5:

        score += 20

        reasons.append("Weekend invoice")

    # Duplicate

    if invoice.duplicate_invoice:

        score += 40

        reasons.append("Duplicate invoice")

    # Missing Vendor

    if not extracted_data.get("vendor_name"):

        score += 20

        reasons.append("Vendor missing")

    if score >= 70:

        level = "High"

    elif score >= 40:

        level = "Medium"

    else:

        level = "Low"

    fraud = score >= 70

    return {

        "score": score,

        "level": level,

        "fraud": fraud,

        "reasons": reasons

    }
    
# app/services/fraud_service.py


# =====================================================
# Invoice Fraud Risk Calculation
# =====================================================

def calculate_risk_score(
    structured_data: dict,
    duplicate: bool = False
):

    score = 0


    # ---------------------------------
    # Duplicate Invoice Risk
    # ---------------------------------

    if duplicate:

        score += 50



    # ---------------------------------
    # Amount Risk
    # ---------------------------------

    amount = structured_data.get(
        "amount",
        0
    )


    try:

        amount = float(amount)

    except:

        amount = 0



    # High value invoice
    if amount > 100000:

        score += 20


    elif amount > 50000:

        score += 10



    # ---------------------------------
    # Missing Important Fields
    # ---------------------------------

    required_fields = [

        "invoice_number",

        "vendor_name",

        "amount",

        "date"

    ]


    missing = 0


    for field in required_fields:

        if not structured_data.get(field):

            missing += 1



    score += missing * 5



    # ---------------------------------
    # Final Risk Level
    # ---------------------------------

    if score >= 70:

        level = "High"

        fraud = True


    elif score >= 40:

        level = "Medium"

        fraud = False


    else:

        level = "Low"

        fraud = False



    return {

        "score": min(score, 100),

        "level": level,

        "fraud": fraud

    }