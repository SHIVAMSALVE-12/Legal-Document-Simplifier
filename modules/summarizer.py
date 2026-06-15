from modules.llm import generate_response

def summarize_document(text):

    prompt = f"""
You are an Indian legal document analyst.

Analyze the document and provide:

1. Executive Summary

2. Key Parties

3. Important Clauses

4. Obligations

5. Risks

6. Deadlines

7. Financial Commitments

8. Termination Conditions

9. Potential Red Flags

Document:
{text}
"""

    return generate_response(prompt)