from sentence_transformers import SentenceTransformer


def embeddings_model():
    model = SentenceTransformer('intfloat/multilingual-e5-base')
    return model
