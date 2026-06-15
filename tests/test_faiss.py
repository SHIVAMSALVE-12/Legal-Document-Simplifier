from modules.document_loader import load_document

from modules.chunker import create_chunks

from modules.embeddings import generate_embeddings

from modules.vector_store import (
    build_index,
    save_index,
    load_index
)

# Load document
text = load_document(
    r"C:\Users\SHIVAM\Downloads\Project_Guide_Allotment_VLSI.docx"
)

# Create chunks
chunks = create_chunks(text)

# Generate embeddings
embeddings = generate_embeddings(chunks)

# Build index
index = build_index(embeddings)

# Save index
save_index(index)

print("FAISS Index Saved Successfully")

# Load index again
loaded_index = load_index()

print(
    "Total vectors in index:",
    loaded_index.ntotal
)