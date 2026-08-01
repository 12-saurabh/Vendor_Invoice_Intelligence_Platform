import pandas as pd
from reportlab.pdfgen import canvas


def export_csv(invoices):

    data=[]

    for invoice in invoices:
        data.append({
            "id":invoice.id,
            "vendor":invoice.vendor_name,
            "amount":invoice.total_amount,
            "status":invoice.status
        })

    df=pd.DataFrame(data)

    path="exports/invoices.csv"

    df.to_csv(path,index=False)

    return path



def export_excel(invoices):

    data=[]

    for invoice in invoices:
        data.append({
            "id":invoice.id,
            "vendor":invoice.vendor_name,
            "amount":invoice.total_amount,
        })


    df=pd.DataFrame(data)

    path="exports/invoices.xlsx"

    df.to_excel(path,index=False)

    return path



def export_pdf(invoices):

    path="exports/invoices.pdf"

    pdf=canvas.Canvas(path)

    y=800

    for invoice in invoices:

        pdf.drawString(
            50,
            y,
            f"{invoice.vendor_name} {invoice.total_amount}"
        )

        y-=30


    pdf.save()

    return path