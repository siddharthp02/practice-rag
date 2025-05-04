> **Note:** This is a quick practice repository to get familiar with running a local LLM and using it via LangChain. The code and setup are intended for experimentation and learning purposes.

# Movie Embedding Vector Store

This project demonstrates how to use LangChain, Ollama embeddings, and Chroma to create a vector database of the top 100 IMDB movies. The script reads movie data from a CSV file, generates embeddings for each movie using the `mxbai-embed-large` model, and stores them in a persistent Chroma vector database. This setup enables efficient semantic search and retrieval of movie information based on vector similarity.

## Features
- Reads movie data from `imdb_top_100.csv`
- Generates embeddings for each movie using Ollama's embedding model
- Stores embeddings in a Chroma vector database for fast retrieval
- Supports semantic search for movie recommendations or information

## Usage
1. Place your `imdb_top_100.csv` file in the project directory.
2. Run `vector.py` to generate embeddings and populate the vector store.
3. The script will create a persistent Chroma database in the `chroma_langchain_db` directory.

## Requirements
- Python 3.8+
- pandas
- langchain_ollama
- langchain_chroma
- langchain_core

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Notes
- The `.gitignore` is set up to exclude the vector database and CSV files from version control.
- You can modify the script to use your own dataset or embedding model as needed. 