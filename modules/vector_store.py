import faiss
import pickle
import os

from modules.embeddings import model


def build_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    return index


def save_document_index(index, chunks):

    os.makedirs(
        "vector_db",
        exist_ok=True
    )

    faiss.write_index(
        index,
        "vector_db/document.index"
    )

    with open(
        "vector_db/chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )


def load_index():

    return faiss.read_index(
        "vector_db/document.index"
    )


def search_index(
        index,
        query,
        chunks,
        k=5
):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:

        if idx < len(chunks):

            results.append(
                chunks[idx]
            )

    return results