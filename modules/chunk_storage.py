import pickle


def save_chunks(chunks):

    with open(
        "vector_db/chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(chunks, f)


def load_chunks():

    with open(
        "vector_db/chunks.pkl",
        "rb"
    ) as f:

        return pickle.load(f)