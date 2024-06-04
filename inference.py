from sentence_transformers import SentenceTransformer
from sentence_transformers import CrossEncoder
from scipy import spatial
from scipy.special import softmax

model_type_dict = {1:'SentenceTransformer',2:'CrossEncoder'} 

class SimilarityScorer:
    
    def __init__(self,model_path,model_type):
        self.model_path = model_path
        self.model_type = model_type_dict[model_type]
        self.model = None
        self.load_model__()
    
    def load_model__(self):
        if self.model_type == 'SentenceTransformer':
            self.model = SentenceTransformer(self.model_path)
        elif self.model_type == 'CrossEncoder':
            self.model = CrossEncoder(self.model_path)
        else:
            pass

    def calulate_similarity(self, sentence0: str,sentence1: str) -> float:       
        if self.model_type == 'SentenceTransformer':
            embedding_0 = self.model.encode(sentence0)
            embedding_1 = self.model.encode(sentence1)
            similarity_score = 1.0 - spatial.distance.cosine(embedding_0,embedding_1)
        
        elif self.model_type == 'CrossEncoder':
            scores = self.model.predict([(sentence0, sentence1)])
            similarity_score = softmax(scores,axis=1)[:,1][0]

        else:
            similarity_score = None

        return similarity_score
        