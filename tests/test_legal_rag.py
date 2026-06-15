from modules.legal_rag import (
    legal_rag
)

response = legal_rag(
    "Is a 90 day notice period valid?"
)

print(response)