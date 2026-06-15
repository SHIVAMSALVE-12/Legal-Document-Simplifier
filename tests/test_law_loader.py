from modules.law_loader import load_law_documents

text = load_law_documents("data/laws")

print("Total Characters:", len(text))

print(text[:2000])