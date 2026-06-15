from modules.document_loader import (
    load_document
)

from modules.legal_report import (
    generate_legal_report
)

text = load_document(
    r"sample_legal_contract.pdf"
)

report = generate_legal_report(
    text
)

print("\n")
print("=" * 60)
print("SUMMARY")
print("=" * 60)

print(
    report["summary"]
)

print("\n")
print("=" * 60)
print("RISK SCORE")
print("=" * 60)

print(
    report["risk_score"]
)

print("\n")
print("=" * 60)
print("FLAGS")
print("=" * 60)

for flag in report["flags"]:

    print(flag)

print("\n")
print("=" * 60)
print("LEGAL ANALYSIS")
print("=" * 60)

print(
    report["legal_analysis"]
)
