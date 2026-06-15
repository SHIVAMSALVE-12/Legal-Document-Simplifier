from modules.docx_parser import extract_docx

text = extract_docx(
    r"C:\Users\SHIVAM\Downloads\Project_Guide_Allotment_VLSI.docx"
)

print(text)