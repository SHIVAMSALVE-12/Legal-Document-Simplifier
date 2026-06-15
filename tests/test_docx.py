from modules.docx_parser import extract_docx

text = extract_docx(
    r"UPLOAD DOC FILE"
)

print(text)
