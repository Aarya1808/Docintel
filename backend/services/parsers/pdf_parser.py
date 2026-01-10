import fitz
from typing import List
from backend.core.schema import DocumentChunk

def parse_pdf(file_path: str) -> List[DocumentChunk]:
    doc = fitz.open(file_path)
    chunks = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text().strip()
        if text:
            chunks.append(
                DocumentChunk(
                    text=text,
                    source=file_path,
                    page=page_num
                )
            )

    return chunks
