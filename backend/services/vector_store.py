from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from backend.core.schema import DocumentChunk

def build_vector_store(chunks: list[DocumentChunk]):
    texts = [c.text for c in chunks]
    metadatas = [
        {"source": c.source, "page": c.page}
        for c in chunks
    ]

    embeddings = HuggingFaceEmbeddings(
         model_name="sentence-transformers/all-MiniLM-L6-v2"
    )  
    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas,
        persist_directory="chroma_db"
    )

    return vectorstore
