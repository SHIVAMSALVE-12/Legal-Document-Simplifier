from modules.document_loader import load_document
from modules.chunker import create_chunks
from modules.embeddings import generate_embeddings

text = load_document(
    r"C:\Users\SHIVAM\Downloads\7 SEM YCCE.pdf"

)

chunks = create_chunks(text)

embeddings = generate_embeddings(
    chunks
)

print(embeddings.shape)