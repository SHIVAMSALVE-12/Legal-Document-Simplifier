import os

from modules.pdf_parser import extract_pdf_text
from modules.docx_parser import extract_docx
from modules.ocr_parser import image_to_text


def load_document(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_pdf_text(file_path)

    elif ext == ".docx":
        return extract_docx(file_path)

    elif ext in [".jpg", ".jpeg", ".png"]:
        return image_to_text(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {ext}"
        )