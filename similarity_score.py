from sentence_transformers import SentenceTransformer # A library for machine learning.
from scipy import spatial

class SimilarityScorer:
    def __init__(self,model_path):
        self.model_path = model_path
        self.load_model__()
    
    def load_model__(self):
        self.model = SentenceTransformer(self.model_path)

    def calulate_similarity(self, sentence0: str,sentence1: str) -> float:
        embedding_0 = self.model.encode(sentence0)
        embedding_1 = self.model.encode(sentence1)
        similarity_score = 1.0 - spatial.distance.cosine(embedding_0,embedding_1)

        return similarity_score
        