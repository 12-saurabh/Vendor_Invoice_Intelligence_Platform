from datetime import datetime
import asyncio

from app.celery_app import celery_app
from app.database import SessionLocal

from app.crud.invoice import (
    get_invoice_by_id,
    update_invoice_after_processing,
    mark_invoice_failed
)
from app.websocket_manager import manager
from app.services.invoice_extraction_service import extract_invoice_data
from app.services.validation_service import validate_invoice
from app.services.duplicate_service import check_duplicate
from app.services.fraud_service import calculate_risk_score
from app.services.vendor_score_service import calculate_vendor_score

from app.crud.extraction import save_extracted_invoice_data
from app.crud.notification import create_notification

from app.services.ocr_service import extract_text_from_pdf

from app.email.email_service import send_email


# =====================================================
# Email Background Task
# =====================================================

@celery_app.task
def send_invoice_email(
    email: str,
    subject: str,
    body: str
):

    try:

        asyncio.run(
            send_email(
                email=email,
                subject=subject,
                body=body
            )
        )

        return {
            "status": "Email Sent"
        }


    except Exception as e:

        print(
            f"Email Error : {e}"
        )

        return {
            "status": "Failed",
            "error": str(e)
        }



# =====================================================
# Invoice Processing Task
# =====================================================

@celery_app.task
def process_invoice(invoice_id: int):

    db = SessionLocal()


    try:

        print(
            f"Processing Invoice {invoice_id}"
        )


        invoice = get_invoice_by_id(
            db,
            invoice_id
        )


        if not invoice:

            return {

                "invoice_id": invoice_id,

                "status": "Failed",

                "error": "Invoice not found"

            }



        # ---------------------------------
        # Processing Start Time
        # ---------------------------------

        invoice.processing_started_at = datetime.utcnow()

        db.commit()



        # ---------------------------------
        # OCR Processing
        # ---------------------------------

        extracted_text = extract_text_from_pdf(
            invoice.file_path
        )



        # ---------------------------------
        # AI Invoice Extraction
        # ---------------------------------

        structured_data = extract_invoice_data(
            extracted_text
        )


        save_extracted_invoice_data(
            db,
            invoice.id,
            structured_data
        )



        # ---------------------------------
        # Duplicate Detection
        # ---------------------------------

        duplicate = check_duplicate(
            db,
            structured_data,
            invoice.vendor_id
        )


        invoice.duplicate_invoice = duplicate



        # ---------------------------------
        # Fraud Risk Calculation
        # ---------------------------------

        risk = calculate_risk_score(
            structured_data,
            duplicate
        )


        invoice.risk_score = risk["score"]

        invoice.risk_level = risk["level"]

        invoice.fraud_detected = risk["fraud"]



        # ---------------------------------
        # Vendor Trust Score
        # ---------------------------------

        vendor_score = calculate_vendor_score(
            db,
            invoice.vendor_id
        )


        invoice.vendor_score = vendor_score


        db.commit()



        # ---------------------------------
        # AI Validation
        # ---------------------------------

        validation_errors = validate_invoice(
            extracted_text
        )



        # ---------------------------------
        # Final Status Decision
        # ---------------------------------

        if duplicate:

            final_status = "Pending Duplicate Review"


        elif risk["fraud"]:

            final_status = "Fraud Review"


        elif validation_errors:

            final_status = "Pending Manual Review"


        else:

            final_status = "Completed"



        # ---------------------------------
        # Update Invoice
        # ---------------------------------

        update_invoice_after_processing(
            db,
            invoice.id,
            extracted_text,
            final_status
        )


        invoice.processing_completed_at = datetime.utcnow()


        db.commit()
        
        # ---------------------------------
        # Create Notification
        # ---------------------------------

        if duplicate:

            title = "Duplicate Invoice Detected"

            message = (
                f"Invoice {invoice.invoice_number} "
                "appears to be a duplicate."
            )


        elif risk["fraud"]:

            title = "Fraud Risk Detected"

            message = (
                f"Invoice {invoice.invoice_number} "
                f"has high fraud risk."
            )


        elif validation_errors:

            title = "Invoice Requires Manual Review"

            message = (
                f"Invoice {invoice.invoice_number} "
                "requires manual review."
            )


        else:

            title = "Invoice Processing Completed"

            message = (
                f"Invoice {invoice.invoice_number} "
                "processed successfully."
            )



        create_notification(

            db=db,

            user_id=invoice.vendor_id,

            title=title,

            message=message

        )



        # ---------------------------------
        # Email Notification
        # ---------------------------------

        if duplicate:

            subject = "Duplicate Invoice Detected"

            body = f"""
Hello,

Invoice {invoice.invoice_number}

appears to be a duplicate invoice.

Status:
Pending Duplicate Review

Please verify before approval.

Thank You.
"""


        elif risk["fraud"]:

            subject = "Fraud Risk Detected"

            body = f"""
Hello,

Invoice {invoice.invoice_number}

has been detected as a high risk invoice.

Risk Score:
{invoice.risk_score}

Risk Level:
{invoice.risk_level}

Immediate review required.

Thank You.
"""


        elif validation_errors:

            subject = "Invoice Requires Manual Review"

            body = f"""
Hello,

Invoice {invoice.invoice_number}

requires manual review.

Validation Errors:

{chr(10).join(validation_errors)}

Thank You.
"""


        else:

            subject = "Invoice Processing Completed"

            body = f"""
Hello,

Invoice {invoice.invoice_number}

has been processed successfully.

Status:
Completed

Risk Score:
{invoice.risk_score}

Vendor Trust Score:
{invoice.vendor_score}

Thank You.
"""



        send_invoice_email.delay(

            "accountant@gmail.com",

            subject,

            body

        )
        
        # ---------------------------------
        # WebSocket Dashboard Update
        # ---------------------------------

        asyncio.run(
            manager.send_message(
                f"Invoice {invoice.invoice_number} processed successfully."
            )
        )



        print(
            f"Invoice {invoice_id} Completed"
        )


        return {

            "invoice_id": invoice.id,

            "status": final_status,

            "duplicate": duplicate,

            "risk_score": invoice.risk_score,

            "risk_level": invoice.risk_level,

            "fraud_detected": invoice.fraud_detected,

            "vendor_score": vendor_score,

            "validation_errors": validation_errors

        }



    except Exception as e:


        print(
            f"Invoice Processing Failed : {e}"
        )


        db.rollback()



        mark_invoice_failed(

            db,

            invoice_id,

            str(e)

        )



        invoice = get_invoice_by_id(

            db,

            invoice_id

        )



        if invoice:


            create_notification(

                db=db,

                user_id=invoice.vendor_id,

                title="Invoice Processing Failed",

                message=(
                    f"Invoice {invoice.invoice_number} "
                    "processing failed."
                )

            )



        return {


            "invoice_id": invoice_id,


            "status": "Failed",


            "error": str(e)


        }



    finally:


        db.close()