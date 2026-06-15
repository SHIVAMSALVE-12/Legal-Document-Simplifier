from modules.llm import generate_response


def explain_flag(flag, document_text):

    prompt = f"""
You are an Indian legal expert.

Detected Red Flag:

{flag['title']}

Severity:

{flag['severity']}

Description:

{flag['description']}

Document:

{document_text[:4000]}

Explain:

1. Why this clause matters
2. Legal implications in India
3. Potential risks
4. Recommendation

Keep answer concise.
"""

    return generate_response(prompt)