from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

import os
import shutil
import uuid


from app.dependencies import (
    get_db,
    get_current_user
)


from app.models.user import User


from app.crud.invoice import create_invoice

from app.crud.audit import create_audit_log

from app.crud.notification import create_notification


from app.tasks import (
    process_invoice,
    send_invoice_email
)


from app.cache import delete_cache





router = APIRouter(

    prefix="/upload",

    tags=["OCR Upload"]

)





UPLOAD_DIR = "uploads"


os.makedirs(

    UPLOAD_DIR,

    exist_ok=True

)





ALLOWED_TYPES = [

    "application/pdf",

    "image/png",

    "image/jpeg"

]







@router.post("/")
def upload_invoice(

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user: User = Depends(get_current_user)

):


    # ---------------------------------
    # Validate File Type
    # ---------------------------------

    if file.content_type not in ALLOWED_TYPES:


        raise HTTPException(

            status_code=400,

            detail="Only PDF, PNG and JPEG files allowed"

        )





    # ---------------------------------
    # Generate Unique Filename
    # ---------------------------------

    unique_filename = (

        f"{uuid.uuid4()}_{file.filename}"

    )



    file_path = os.path.join(

        UPLOAD_DIR,

        unique_filename

    )







    # ---------------------------------
    # Save File
    # ---------------------------------

    with open(

        file_path,

        "wb"

    ) as buffer:


        shutil.copyfileobj(

            file.file,

            buffer

        )







    # ---------------------------------
    # Create Invoice Record
    # ---------------------------------

    invoice_data = {


        "invoice_number":

            f"TEMP-{uuid.uuid4().hex[:8]}",



        "amount":

            0,



        "currency":

            "USD",



        "vendor_id":

            1,



        "file_name":

            file.filename,



        "file_path":

            file_path,



        "status":

            "Processing"


    }





    invoice = create_invoice(

        db,

        invoice_data

    )








    # ---------------------------------
    # Clear Dashboard Cache
    # ---------------------------------

    delete_cache(

        "dashboard_summary"

    )


    delete_cache(

        "monthly_statistics"

    )


    delete_cache(

        "vendor_statistics"

    )


    delete_cache(

        "risk_statistics"

    )







    # ---------------------------------
    # Notification
    # ---------------------------------

    create_notification(

        db=db,

        user_id=current_user.id,

        title="Invoice Uploaded",

        message=(

            f"Invoice '{invoice.file_name}' "

            "uploaded successfully. OCR processing started."

        )

    )








    # ---------------------------------
    # Email Notification
    # ---------------------------------

    # ---------------------------------
    # Send Email Background Task
    # ---------------------------------

    subject = "Invoice Uploaded Successfully"

    body = f"""
    Hello {current_user.username},

    Your invoice has been uploaded successfully.

    Invoice Number:
    {invoice.invoice_number}

    Current Status:
    {invoice.status}

    The invoice is now being processed in the background.

    Thank you.
    """

    send_invoice_email.delay(

        current_user.email,

        subject,

        body

    )







    # ---------------------------------
    # Start Background OCR + ML
    # ---------------------------------

    process_invoice.delay(

        invoice.id

    )








    # ---------------------------------
    # Audit Log
    # ---------------------------------

    create_audit_log(

        db=db,

        user_id=current_user.id,

        action="UPLOAD_INVOICE",

        entity="Invoice",

        entity_id=invoice.id,

        new_value=file.filename

    )








    return {


        "message":

            "Invoice uploaded successfully",



        "invoice_id":

            invoice.id,



        "invoice_number":

            invoice.invoice_number,



        "status":

            invoice.status,



        "background_processing":

            True,



        "file_name":

            file.filename


    }