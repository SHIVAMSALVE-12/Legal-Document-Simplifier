from modules.law_index_builder import (
    build_law_index,
    save_law_index
)

index, chunks = build_law_index()

save_law_index(
    index,
    chunks
)

print("Law Chunks:", len(chunks))