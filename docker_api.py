from fastapi import FastAPI
from pydantic import BaseModel
from sentimentAnalysis.analysis.trained_model.use_model_from_docker import analyze

app = FastAPI()

class TextIn(BaseModel):
    text: str

class TextOut(BaseModel):
    sentiment: str

@app.get('/')
def home():
    return {"health_check": "OK"}

@app.post('/analyze_sentiment', response_model=TextOut)
def analyze_sentiment(payload: TextIn):
    result = analyze(payload.text)
    return {'sentiment': result}
