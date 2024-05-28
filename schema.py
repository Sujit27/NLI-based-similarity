from pydantic import BaseModel

class Request(BaseModel):
    sent1: str
    sent2: str

class Response(BaseModel):
    sent1: str
    sent2: str
    similarity_score: float