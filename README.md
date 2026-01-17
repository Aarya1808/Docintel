# DocIntel

DocIntel is a multi-document Retrieval-Augmented Generation (RAG) system that answers questions from uploaded documents with source citations and flags potential conflicts across sources.

## Problem

Large Language Models can generate fluent answers but often hallucinate or fail to cite sources.
For document-heavy use cases (research papers, reports, policies), users need answers grounded in their documents with transparent attribution.

## What DocIntel Does

- Ingests PDFs, DOCX, and Markdown documents
- Parses and chunks documents into semantic segments
- Generates embeddings locally and stores them in a vector database
- Retrieves relevant document chunks for a user query
- Generates answers strictly from retrieved context
- Attaches source citations (document name and page)
- Flags potential conflicts when retrieved sources disagree

## Architecture Overview

User uploads documents → 
Documents are parsed and chunked → 
Chunks are embedded using a local sentence-transformer → 
Embeddings are stored in Chroma → 
User query retrieves top-k relevant chunks → 
Retrieved context is passed to a local LLM (via Ollama) → 
Answer is generated with citations → 
Conflict detection heuristics flag inconsistencies

## Tech Stack

- Backend: FastAPI
- Language: Python
- Embeddings: sentence-transformers (all-MiniLM-L6-v2)
- Vector Database: Chroma
- LLM: Mistral via Ollama (local)
- Document Parsing: PyMuPDF, python-docx

## Design Decisions

- Local embeddings were used to avoid external dependencies and better understand the full RAG pipeline.
- Retrieval is performed before generation to ground answers and reduce hallucinations.
- The LLM is constrained with strict prompting and temperature=0 to minimize creativity.
- Conflict detection is heuristic-based to signal potential inconsistencies without attempting to determine truth.

## API Endpoints

POST /upload  
Uploads and indexes a document.

POST /query  
Accepts a question and returns an answer with citations and optional conflict warnings.

## Limitations

- Conflict detection is heuristic-based and may produce false positives or negatives.
- No authentication or multi-user support (single-session MVP).
- Vector store is stored in-memory for the current session.
- Accuracy depends on document quality and chunking strategy.
