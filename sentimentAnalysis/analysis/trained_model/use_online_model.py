from transformers import pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"


# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def analyze(text):
    sentiment_task = pipeline("sentiment-analysis", model=MODEL_NAME, tokenizer=MODEL_NAME)
    text = preprocess(text)
    result = sentiment_task(text)

    return result[0]['label']

# if __name__ == "__main__":
#     text = "Covid cases are increasing fast!"
#     print(analyze(text))