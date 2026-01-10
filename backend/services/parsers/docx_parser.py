from typing import List
from docx import Document
from backend.core.schema import DocumentChunk

def parse_docx(file_path: str) -> List[DocumentChunk]:
    doc = Document(file_path)
    chunks = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            chunks.append(
                DocumentChunk(
                    text=text,
                    source=file_path,
                    page=None
                )
            )

    return chunks
