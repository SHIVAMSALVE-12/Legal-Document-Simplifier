import fitz

def extract_pdf_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        page_text = page.get_text()

        text += page_text

    return text