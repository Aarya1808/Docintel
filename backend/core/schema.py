from dataclasses import dataclass
from typing import Optional
@dataclass
class DocumentChunk:
    text:str
    source:str
    page:Optional[int] = None