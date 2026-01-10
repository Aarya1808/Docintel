from typing import List
from backend.core.schema import DocumentChunk

def parse_markdown(file_path: str) -> List[DocumentChunk]:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        return []

    return [
        DocumentChunk(
            text=text,
            source=file_path,
            page=None
        )
    ]
