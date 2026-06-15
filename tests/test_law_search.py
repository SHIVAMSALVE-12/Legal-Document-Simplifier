from modules.legal_analyzer import (
    retrieve_law_context
)

query = ("Definition of rape")

results = retrieve_law_context(
    query
)

print(results)