'''
From use_local_model.py
'''
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
from scipy.special import softmax
import os

# use offline mode avoiding downloading models from huggingface
def setEnvir():
    os.environ["TRANSFORMERS_OFFLINE"] = '1'


# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def analyze(text):
    setEnvir()
    if not text:
        return 'Not Input Detected.'

    MODEL = "/app/sentimentAnalysis/analysis/trained_model/roberta_local"

    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # Print labels and scores
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    results = list()
    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        s = scores[ranking[i]]
        # print(f"{i+1}) {l} {np.round(float(s), 4)}")
        results.append([np.round(float(s), 4), l])
    sorted_results = sorted(results, key=lambda x: x[0], reverse=True)
    # print(sorted_results)
    return sorted_results[0][1]

