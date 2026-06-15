import faiss
import pickle

from modules.vector_store import search_index
from modules.llm import generate_response


# ==========================================
# Load Document Database
# ==========================================

document_index = faiss.read_index(
    "vector_db/document.index"
)

with open(
    "vector_db/chunks.pkl",
    "rb"
) as f:
    document_chunks = pickle.load(f)


# ==========================================
# Load Law Database
# ==========================================

law_index = faiss.read_index(
    "vector_db/law.index"
)

with open(
    "vector_db/law_chunks.pkl",
    "rb"
) as f:
    law_chunks = pickle.load(f)


# ==========================================
# Retrieve Document Context
# ==========================================

def retrieve_document_context(
        question,
        k=3
):

    results = search_index(
        document_index,
        question,
        document_chunks,
        k=k
    )

    return "\n\n".join(results)


# ==========================================
# Retrieve Law Context
# ==========================================

def retrieve_law_context(
        question,
        k=3
):

    results = search_index(
        law_index,
        question,
        law_chunks,
        k=k
    )

    return "\n\n".join(results)


# ==========================================
# Main Legal RAG Function
# ==========================================

def legal_rag(question):

    document_context = retrieve_document_context(
        question
    )

    law_context = retrieve_law_context(
        question
    )

    prompt = f"""
You are an expert Indian Legal Analyst.

Use ONLY the information present in:

1. Document Context
2. Relevant Indian Law

Rules:

- Do NOT invent laws.
- Do NOT assume facts.
- Do NOT provide unrelated legal provisions.
- If information is missing, clearly say:
  "Insufficient information available."
- Prefer Indian legal interpretation.
- Focus on practical legal implications.

==================================================

DOCUMENT CONTEXT

{document_context}

==================================================

RELEVANT INDIAN LAW

{law_context}

==================================================

QUESTION

{question}

==================================================

Provide output in exactly this format:

1. Answer

2. Legal Basis

3. Risks

4. Recommendations

5. Confidence Level
(High / Medium / Low)

==================================================
"""

    response = generate_response(
        prompt
    )

    return response