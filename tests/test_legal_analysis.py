from modules.legal_analyzer import (
    analyze_document_legally
)

document_context = """
Employee shall serve
90 days notice period.

Employer may terminate
employment for misconduct.
"""

question = """
Is the 90 day notice period valid?
"""

response = analyze_document_legally(
    question,
    document_context
)

print(response)