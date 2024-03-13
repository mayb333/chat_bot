from chromadb import PersistentClient
from chromadb.utils import embedding_functions


class ChromaManager:
    def __init__(self, model_name: str = "intfloat/multilingual-e5-base", output_path: str = "src/artifacts/chromadb"):
        self.emb_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)
        self.chroma_client = PersistentClient(path=output_path)

    def create_collection(self, name):
        return self.chroma_client.create_collection(name=name, embedding_function=self.emb_func)

    def delete_collection(self, name):
        return self.chroma_client.delete_collection(name=name)

    def add_documents(self, collection_name, embeddings, documents, metadatas, ids):
        collection = self.chroma_client.get_collection(name=collection_name)
        return collection.add(embeddings=embeddings, documents=documents, metadatas=metadatas, ids=ids)

    def query_documents(self, collection_name, query_texts, n_results=5):
        collection = self.chroma_client.get_collection(name=collection_name)
        return collection.query(query_texts=query_texts, n_results=n_results)
