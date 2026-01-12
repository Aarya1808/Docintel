from typing import List
from backend.core.schema import DocumentChunk

CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

def chunk_text(chunks: List[DocumentChunk]) -> List[DocumentChunk]:
    new_chunks = []

    for chunk in chunks:
        text = chunk.text
        start = 0

        while start < len(text):
            end = start + CHUNK_SIZE
            chunk_text = text[start:end]

            new_chunks.append(
                DocumentChunk(
                    text=chunk_text,
                    source=chunk.source,
                    page=chunk.page
                )
            )

            if end >= len(text):
                break

            start += CHUNK_SIZE - CHUNK_OVERLAP

    return new_chunks