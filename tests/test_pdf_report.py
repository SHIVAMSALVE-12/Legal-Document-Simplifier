from modules.document_loader import (
    load_document
)

from modules.legal_report import (
    generate_legal_report
)

from modules.report_generator import (
    create_pdf_report
)

text = load_document(
    r"data/uploads/sample_legal_contract.pdf"
)

report = generate_legal_report(
    text
)

path = create_pdf_report(
    report,
    "reports/legal_report.pdf"
)

print(path)