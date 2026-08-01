from sqlalchemy.orm import Session

from app.models.invoice import Invoice


# =====================================================
# Calculate Vendor Trust Score
# =====================================================

def calculate_vendor_score(
    db: Session,
    vendor_id: int
):

    try:

        # Fetch vendor invoices
        invoices = (
            db.query(Invoice)
            .filter(
                Invoice.vendor_id == vendor_id
            )
            .all()
        )


        # New vendor default score
        if not invoices:

            return 50



        total_invoices = len(invoices)

        completed = 0

        rejected = 0

        duplicate_count = 0



        for invoice in invoices:


            if invoice.status == "Completed":

                completed += 1


            if invoice.status == "Rejected":

                rejected += 1


            if invoice.duplicate_invoice:

                duplicate_count += 1



        # ---------------------------------
        # Score Calculation
        # ---------------------------------

        completion_rate = (
            completed / total_invoices
        ) * 100


        rejection_penalty = (
            rejected / total_invoices
        ) * 20


        duplicate_penalty = (
            duplicate_count / total_invoices
        ) * 30



        score = (
            completion_rate
            - rejection_penalty
            - duplicate_penalty
        )



        # Keep score between 0-100

        score = max(
            0,
            min(
                100,
                score
            )
        )


        return round(
            score,
            2
        )


    except Exception as e:


        print(
            f"Vendor score calculation error: {e}"
        )


        # Safe fallback

        return 50
    