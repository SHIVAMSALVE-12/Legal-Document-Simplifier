import faiss
import pickle

from modules.vector_store import search_index
from modules.llm import generate_response


# Load Law Index
law_index = faiss.read_index(
    "vector_db/law.index"
)

# Load Law Chunks
with open(
    "vector_db/law_chunks.pkl",
    "rb"
) as f:

    law_chunks = pickle.load(f)


def retrieve_law_context(question):
    """
    Search Indian law database and return
    most relevant law sections.
    """

    results = search_index(
        law_index,
        question,
        law_chunks,
        k=3
    )

    return "\n\n".join(results)


def analyze_document_legally(
        question,
        document_context
):
    """
    Combines uploaded document context
    with Indian law context.
    """

    law_context = retrieve_law_context(
        question
    )

    prompt = f"""
You are an Indian legal expert.

Document Context:

{document_context}

Relevant Indian Law:

{law_context}

Question:

{question}

Provide:

1. Answer

2. Legal Basis

3. Risks

4. Recommendations
"""

    return generate_response(
        prompt
    )