from dotenv import load_dotenv
load_dotenv()
from typing import List, Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.documents import Document


def generate_answer(
    question: str,
    retrieved_chunks: List[Document]
) -> Dict:
    """
    Generate an answer strictly from retrieved document chunks.
    """

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
- Do NOT use outside knowledge.
- Do NOT infer beyond the context.
- If the answer is not present, say: "I don't know based on the documents."
- Cite sources using [number] notation.

Context:
{context}

Question:
{question}

Answer:
"""

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0
    )

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return {
        "answer": response.content,
        "sources": sources
    }
