import os
import faiss
import pickle

from modules.law_loader import load_law_documents
from modules.chunker import create_chunks
from modules.embeddings import generate_embeddings
from modules.vector_store import build_index


def build_law_index():

    text = load_law_documents(
        "data/laws"
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

    return index, chunks


def save_law_index(
        index,
        chunks
):

    os.makedirs(
        "vector_db",
        exist_ok=True
    )

    faiss.write_index(
        index,
        "vector_db/law.index"
    )

    with open(
        "vector_db/law_chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )
        