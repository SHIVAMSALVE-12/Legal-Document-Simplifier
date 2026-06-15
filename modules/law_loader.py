import os

from modules.pdf_parser import extract_pdf_text
from modules.docx_parser import extract_docx


def load_law_documents(root_dir):

    all_text = ""

    for root, dirs, files in os.walk(root_dir):

        for file in files:

            path = os.path.join(
                root,
                file
            )

            if file.endswith(".pdf"):

                all_text += (
                    extract_pdf_text(path)
                    + "\n"
                )

            elif file.endswith(".docx"):

                all_text += (
                    extract_docx(path)
                    + "\n"
                )

    return all_text