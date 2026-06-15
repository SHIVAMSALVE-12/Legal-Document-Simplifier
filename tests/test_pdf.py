from modules.pdf_parser import extract_pdf_text

text = extract_pdf_text(
    r"C:\Users\SHIVAM\Downloads\7 SEM YCCE.pdf"
)

print(text)