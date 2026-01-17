from dataclasses import dataclass
from typing import Optional, List
from pydantic import BaseModel

@dataclass
class DocumentChunk:
    text:str
    source:str
    page:Optional[int] = None

class QueryRequest(BaseModel):
    question: str

class SourceInfo(BaseModel):
    source: str
    page: Optional[int]

class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceInfo]
    warning: Optional[str] = None