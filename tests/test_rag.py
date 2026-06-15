from modules.document_loader import load_document

from modules.chunker import create_chunks

from modules.embeddings import generate_embeddings

from modules.vector_store import build_index

from modules.rag import ask_question


text = load_document(
    r"\uploads\sample_legal_contract.pdf"
)

chunks = create_chunks(text)

embeddings = generate_embeddings(
    chunks
)

index = build_index(
    embeddings
)

question = (
    "What is the notice period?"
)


answer = ask_question(
    question,
    index,
    chunks
)

print(answer)
