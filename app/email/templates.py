def invoice_uploaded_template(
    invoice_number
):

    return f"""

    <h2>
    Invoice Uploaded
    </h2>

    <p>
    Invoice {invoice_number}
    has been uploaded successfully.
    </p>

    """



def invoice_approved_template(
    invoice_number
):

    return f"""

    <h2>
    Invoice Approved
    </h2>

    <p>
    Invoice {invoice_number}
    has been approved.
    </p>

    """



def invoice_rejected_template(
    invoice_number
):

    return f"""

    <h2>
    Invoice Rejected
    </h2>

    <p>
    Invoice {invoice_number}
    has been rejected.
    </p>

    """