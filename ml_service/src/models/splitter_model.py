from typing import List
from sentence_transformers import SentenceTransformer, util
import spacy
from abc import ABC, abstractmethod


class Splitter(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def split(self, text: str) -> List[str]:
        pass


class SpacySentenceSplitter(Splitter):

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.max_length = 3e106

    def split(self, text: str) -> List[str]:
        doc = self.nlp(text)
        return [str(sent).strip() for sent in doc.sents]


class SentenceTransformersSimilarity():
    def __init__(self, model='all-MiniLM-L6-v2', similarity_threshold=0.2):
        self.model = SentenceTransformer(model)
        self.similarity_threshold = similarity_threshold

    def similarities(self, sentences: List[str]):
        # Encode all sentences
        embeddings = self.model.encode(sentences)

        # Calculate cosine similarities for neighboring sentences
        similarities = []
        for i in range(1, len(embeddings)):
            sim = util.pytorch_cos_sim(embeddings[i - 1], embeddings[i]).item()
            similarities.append(sim)

        return similarities


class SimilarSentenceSplitter(Splitter):

    def __init__(self, similarity_model, sentence_splitter: Splitter):
        self.model = similarity_model
        self.sentence_splitter = sentence_splitter

    def split(self, text: str, group_max_sentences=5) -> List[str]:
        '''
            group_max_sentences: The maximum number of sentences in a group.
        '''
        sentences = self.sentence_splitter.split(text)

        if len(sentences) == 0:
            return []

        similarities = self.model.similarities(sentences)

        # The first sentence is always in the first group.
        groups = [[sentences[0]]]

        # Using the group min/max sentences contraints,
        # group together the rest of the sentences.
        for i in range(1, len(sentences)):
            if len(groups[-1]) >= group_max_sentences:
                groups.append([sentences[i]])
            elif similarities[i - 1] >= self.model.similarity_threshold:
                groups[-1].append(sentences[i])
            else:
                groups.append([sentences[i]])

        return groups


def chunks_splitter_model():
    model = SentenceTransformersSimilarity()
    sentence_splitter = SpacySentenceSplitter()
    splitter = SimilarSentenceSplitter(model, sentence_splitter=sentence_splitter)
    return splitter
