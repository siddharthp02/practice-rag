from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("imdb_top_100.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content = str(row["Series_Title"]) + " " + str(row["IMDB_Rating"]) + " " + str(row["Overview"]),
            medatada = {"Release date": str(row["Released_Year"]), "Genre":str(row["Genre"])},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name = "Movie_ratings",
    persist_directory = db_location,
    embedding_function = embeddings
)

if add_documents:
    vector_store.add_documents(documents = documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs = {"k":5}
)