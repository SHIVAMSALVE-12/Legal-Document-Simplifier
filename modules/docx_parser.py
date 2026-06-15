from docx import Document

def extract_docx(doc_path):
    doc = Document(doc_path)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)