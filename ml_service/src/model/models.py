from .splitter_model import SentenceTransformersSimilarity, SpacySentenceSplitter, SimilarSentenceSplitter
from embeddings_model import embeddings_model
from prediction_model import create_prediction_model
def chunks_splitter_model(): #-> text splitter
    model = SentenceTransformersSimilarity()
    sentence_splitter = SpacySentenceSplitter()
    splitter = SimilarSentenceSplitter(model, sentence_splitter=sentence_splitter)
    return splitter

def prediction_model():#
    model, tokenizer = create_prediction_model()
    return model, tokenizer