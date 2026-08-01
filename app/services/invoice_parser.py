import re
from datetime import datetime, date, timedelta



def extract_invoice_details(text: str):

    invoice_number = None
    amount = None
    invoice_date = None
    due_date = None
    currency = "USD"



    # -----------------------------------
    # Extract Invoice Number
    # Supports:
    # Invoice Number: INV001
    # Invoice No: INV001
    # -----------------------------------

    invoice_match = re.search(
        r"Invoice\s*(?:Number|No)\s*[:\-]?\s*([A-Za-z0-9\-]+)",
        text,
        re.IGNORECASE
    )


    if invoice_match:
        invoice_number = invoice_match.group(1)



    # -----------------------------------
    # Extract Amount
    # Supports:
    # Amount: 2500
    # Total: 2500
    # Total Amount: $2500
    # -----------------------------------

    amount_match = re.search(
        r"(?:Amount|Total(?:\s+Amount)?)\s*[:\-]?\s*\$?\s*([\d,]+\.?\d*)",
        text,
        re.IGNORECASE
    )


    if amount_match:

        amount = float(
            amount_match.group(1)
            .replace(",", "")
        )



    # -----------------------------------
    # Extract Invoice Date
    # Format:
    # 29-07-2026
    # -----------------------------------

    date_match = re.search(
        r"(?:Invoice\s*)?Date\s*[:\-]?\s*(\d{2}-\d{2}-\d{4})",
        text,
        re.IGNORECASE
    )


    if date_match:

        invoice_date = datetime.strptime(
            date_match.group(1),
            "%d-%m-%Y"
        ).date()



    # -----------------------------------
    # Extract Due Date
    # -----------------------------------

    due_match = re.search(
        r"Due\s*Date\s*[:\-]?\s*(\d{2}-\d{2}-\d{4})",
        text,
        re.IGNORECASE
    )


    if due_match:

        due_date = datetime.strptime(
            due_match.group(1),
            "%d-%m-%Y"
        ).date()



    return {

        "invoice_number": invoice_number or "UNKNOWN",

        "amount": amount or 0,

        "currency": currency,

        "invoice_date": invoice_date or date.today(),

        "due_date": due_date or (
            date.today()
            +
            timedelta(days=30)
        ),

        "status": "Pending"

    }



# ------------------------------------------------
# Compatibility function
# upload.py currently imports parse_invoice
# ------------------------------------------------

def parse_invoice(text):

    invoice_number = None
    amount = None


    # Invoice number extraction
    invoice_match = re.search(
        r"(invoice\s*(number|no)?)[\s:#-]*([A-Za-z0-9-]+)",
        text,
        re.I
    )

    if invoice_match:
        invoice_number = invoice_match.group(3)


    # Amount extraction
    amount_match = re.search(
        r"(total|amount|grand total)[\s:$]*([0-9,]+\.?[0-9]*)",
        text,
        re.I
    )

    if amount_match:
        amount = float(
            amount_match.group(2).replace(",", "")
        )


    return {
        "invoice_number": invoice_number,
        "amount": amount
    }
    
def parse_invoice_text(

    text: str

):


    invoice_number = None

    amount = None



    invoice_match = re.search(

        r"invoice\s*no[:\s]*([A-Za-z0-9-]+)",

        text,

        re.IGNORECASE

    )


    if invoice_match:

        invoice_number = invoice_match.group(1)




    amount_match = re.search(

        r"(total|amount)[^\d]*(\d+\.?\d*)",

        text,

        re.IGNORECASE

    )


    if amount_match:

        amount = float(

            amount_match.group(2)

        )




    return {


        "invoice_number": invoice_number,


        "amount": amount,


        "raw_text": text

    }