from modules.document_loader import load_document

from modules.red_flag_engine import (
    detect_red_flags
)

from modules.clause_explainer import (
    explain_flag
)

text = load_document(
    r"UPLOD YOUR DOCUMENT PDF"
)

flags = detect_red_flags(text)

for flag in flags:

    print("\n")
    print("=" * 60)

    print(flag["title"])

    print("=" * 60)

    explanation = explain_flag(
        flag,
        text
    )

    print(explanation)
