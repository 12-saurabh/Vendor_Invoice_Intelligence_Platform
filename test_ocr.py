from app.services.ocr_service import extract_text_from_pdf


pdf_path = "invoice.pdf"


text = extract_text_from_pdf(pdf_path)


print("--------- OCR RESULT ---------")
print(text)