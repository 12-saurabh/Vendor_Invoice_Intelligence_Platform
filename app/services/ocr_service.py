import pytesseract
from PIL import Image
from pdf2image import convert_from_path


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


POPPLER_PATH = r"C:\Program Files\poppler-26.02.0\Library\bin"


def extract_text_from_pdf(pdf_path):

    pages = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )

    extracted_text = ""

    for page in pages:
        text = pytesseract.image_to_string(page)
        extracted_text += text + "\n"

    return extracted_text



def extract_text_from_image(
    image_path: str
):

    text = pytesseract.image_to_string(

        Image.open(image_path)

    )


    return text