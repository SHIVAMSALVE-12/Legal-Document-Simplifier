from modules.document_loader import load_document

from modules.chunker import create_chunks

from modules.embeddings import generate_embeddings

from modules.vector_store import (
    build_index,
    save_document_index
)

text = load_document(
    r"sample_legal_contract.pdf"
)

chunks = create_chunks(
    text
)

embeddings = generate_embeddings(
    chunks
)

index = build_index(
    embeddings
)

save_document_index(
    index,
    chunks
)

print(
    "Document chunks:",
    len(chunks)
)
