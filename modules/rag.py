from modules.vector_store import search_index
from modules.llm import generate_response


def ask_question(
        question,
        index,
        chunks
):

    retrieved_chunks = search_index(
        index,
        question,
        chunks,
        k=3
    )

    context = "\n\n".join(
        retrieved_chunks
    )

    prompt = f"""
You are a legal document analyst.

Document Context:
{context}

Question:
{question}

Instructions:
- Answer using only the document context.
- Keep answer under 3 sentences.
- Do not repeat information.
"""

    answer = generate_response(
        prompt
    )

    return answer