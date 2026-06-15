from sentence_transformers import SentenceTransformer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device=device
)

def generate_embeddings(chunks):

    return model.encode(
        chunks,
        convert_to_numpy=True
    )