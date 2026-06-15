from modules.document_loader import load_document
from modules.chunker import create_chunks

text = load_document(
    r"UPLOAD PDF PATH"
)

chunks = create_chunks(text)

print("Total Chunks:", len(chunks))

print("\nChunk 1:\n")
print(chunks[0])
