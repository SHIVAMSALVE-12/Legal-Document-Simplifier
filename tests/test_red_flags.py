from modules.document_loader import load_document

from modules.red_flag_engine import (
    detect_red_flags,
    calculate_risk_score
)

text = load_document(
    r"C:\Projects\legal-document-simplifier\data\uploads\sample_legal_contract.pdf"
)

flags = detect_red_flags(text)

score = calculate_risk_score(flags)

print("\n==============================")
print("RISK SCORE:", score)
print("==============================\n")

for flag in flags:

    print(
        f"[{flag['severity']}] "
        f"{flag['title']}"
    )

    print(
        f"Description: "
        f"{flag['description']}"
    )

    print("-" * 50)