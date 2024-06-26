import configparser
import os

import numpy as np
 
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 
from fastapi.responses import HTMLResponse
from middlewares.exception import ExceptionHandlerMiddleware

from inference import SimilarityScorer
from schema import Request,Response

config = configparser.ConfigParser()
config.read('config/config.ini')

model_path = config.get('PATH','model')
model_type = int(config.get('MODEL','type'))
scorer = SimilarityScorer(model_path,model_type)

app = FastAPI()
app.add_middleware(ExceptionHandlerMiddleware)

@app.post("/findSimilarity")
async def findSimilarity(item: Request) -> Response:
    
    score = scorer.calulate_similarity(item.sent1,item.sent2)
    
    return {"sent1":item.sent1,
            "sent2":item.sent2,
            "similarity_score":score}

if __name__ == "__main__":
    uvicorn.run(app,host=config.get('SERVER','host'),port=int(config.get('SERVER','port')))
