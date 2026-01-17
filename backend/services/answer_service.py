from typing import List, Dict
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.documents import Document


def generate_answer(
    question: str,
    retrieved_chunks: List[Document]
) -> Dict:
    context = ""
    sources = []

    for idx, chunk in enumerate(retrieved_chunks, start=1):
        source = chunk.metadata.get("source", "unknown")
        page = chunk.metadata.get("page", "unknown")

        context += f"[{idx}] Source: {source}, Page: {page}\n"
        context += chunk.page_content + "\n\n"

        sources.append({
            "source": source,
            "page": page
        })

    prompt = f"""
You are a document-based question answering assistant.

RULES:
- Answer ONLY using the provided context.
- Do NOT add any facts that are not explicitly stated in the context.
- Do NOT infer beyond the context.
- If the answer is not present, say: "I don't know based on the documents."
- Cite sources using [number] notation.

Context:
{context}

Question:
{question}

Answer:
"""

    llm = ChatOllama(
        model="mistral",
        temperature=0
    )

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "answer": response.content,
        "sources": sources
    }
