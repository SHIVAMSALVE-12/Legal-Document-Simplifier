from modules.document_loader import load_document

from modules.chunker import create_chunks

from modules.embeddings import generate_embeddings

from modules.vector_store import (
    build_index,
    search_index
)

text = load_document(
    r"data\uploads\sample_legal_contract.pdf"
)

chunks = create_chunks(text)

embeddings = generate_embeddings(
    chunks
)

index = build_index(
    embeddings
)

results = search_index(
    index,
    "notice period",
    chunks
)

for r in results:

    print("\n================")
    print(r)
