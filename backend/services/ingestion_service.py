import os
from typing import List
from backend.core.schema import DocumentChunk
from backend.services.parsers.pdf_parser import parse_pdf
from backend.services.parsers.docx_parser import parse_docx
from backend.services.parsers.markdown_parser import parse_markdown

def ingest_file(file_path: str) -> List[DocumentChunk]:
    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)
    elif file_path.endswith(".docx"):
        return parse_docx(file_path)
    elif file_path.endswith(".md"):
        return parse_markdown(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
