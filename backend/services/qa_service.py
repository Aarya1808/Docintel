from backend.services.answer_service import generate_answer
from backend.services.conflict_service import detect_conflict
from langchain_core.documents import Document
from typing import List, Dict

def answer_question(
    question: str,
    retrieved_chunks: List[Document]
) -> Dict:
    conflict = detect_conflict(retrieved_chunks)

    result = generate_answer(question, retrieved_chunks)

    if conflict:
        result["warning"] = (
            "⚠️ Potential conflict detected between sources. "
            "Different documents may present differing information."
        )

    return result
