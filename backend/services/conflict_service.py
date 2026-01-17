from typing import List
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def detect_conflict(chunks: List[Document]) -> bool:
    if len(chunks) < 2:
        return False

    texts = [c.page_content for c in chunks]
    vectors = embeddings.embed_documents(texts)

    similarity_matrix = cosine_similarity(vectors)

   
    similarities = []

    for i in range(len(similarity_matrix)):
        for j in range(i + 1, len(similarity_matrix)):
            similarities.append(similarity_matrix[i][j])

    avg_similarity = np.mean(similarities)

   
    return avg_similarity < 0.6
