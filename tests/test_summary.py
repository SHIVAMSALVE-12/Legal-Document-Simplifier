from modules.document_loader import load_document

from modules.summarizer import (
    summarize_document
)

text = load_document(
    r"data\uploads\sample_legal_contract.pdf"
)

summary = summarize_document(
    text
)

print(summary)
