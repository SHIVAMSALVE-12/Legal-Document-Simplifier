from modules.pdf_parser import extract_pdf_text

text = extract_pdf_text(
    r"pdf"
)

print(text)
