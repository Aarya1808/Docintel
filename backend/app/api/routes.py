from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.services.ingestion_service import ingest_file
from backend.services.chunking_service import chunk_text
from backend.services.vector_store import build_vector_store
from backend.services.qa_service import answer_question
from backend.core.schema import QueryRequest, QueryResponse

router = APIRouter()

DATA_DIR = "data"
VECTORSTORE = None


@router.post("/upload")
def upload_document(file: UploadFile = File(...)):
    os.makedirs(DATA_DIR, exist_ok=True)

    file_path = os.path.join(DATA_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    raw_chunks = ingest_file(file_path)
    chunks = chunk_text(raw_chunks)

    global VECTORSTORE
    VECTORSTORE = build_vector_store(chunks)

    return {"message": f"{file.filename} uploaded and indexed successfully."}


@router.post("/query", response_model=QueryResponse)
def query_docs(request: QueryRequest):
    if VECTORSTORE is None:
        return {"answer": "No documents uploaded yet.", "sources": []}

    retrieved_chunks = VECTORSTORE.similarity_search(
        request.question, k=3
    )

    result = answer_question(request.question, retrieved_chunks)
    return result
