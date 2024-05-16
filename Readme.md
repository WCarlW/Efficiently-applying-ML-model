# Optimizing RoBERTa Model Deployment for Sentiment Analysis in Django: A Performance-driven Approach

This project aims to find the most optimal way to deploy a RoBERTa model to an app for sentiment analysis. Three deployment methods are taken into consideration: local deployment, container deployment (Docker), and cloud deployment. The RoBERTa model trained by COSE and the pre-trained model, TimeLMs, by Cardiff NLP are considered and compared, and TimeLMs is selected to be deployed. 

## Models
### **RoBERTa model trained by COSE**
> [!IMPORTANT]
> This model is not in use. Using this model requires modification of the source code.

The [source code](sentimentAnalysis/analysis/src/Models/RoBERTa/RoBERTa.py) to train the model is located at `sentimentAnalysis/analysis/src/Models/RoBERTa/RoBERTa.py`.

The model can be trained with either your local device or [Google Colab](https://colab.google/). The python notebook, [Sentiment](Sentiment.ipynb), can be used directly in Colab for model training. 
> [!NOTE]
> The trained model will be stored in your Google Drive and has to be downloaded manually due to the large size of the model.
 
> [!CAUTION]
> This notebook requires access to your Google Drive.

### **TimeLMs by Cardiff NLP**
This is an open-source RoBERTa model trained by Cardiff NLP. 

[The model can be accessed on HuggingFace.](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)

## App
This app is only for research purposes, and only necessary functions are implemented. 

Because log in function is not implemented, the current user will always be the same and cannot be changed in the app. 

### Run the app

1. Create a `Python virtual environment` in the **root directory**
2. Go to the `virtual environment`
3. Install all required packages in `requirements.txt`. `pip install -r requirements.txt` if using pip.
4. Go to **SentimentAnalysis** directory and run `python manage.py runserver`
5. The default URL is `http://127.0.0.1:8000/

The only way to add more users and publish content with other users' names is in the admin panel. 

1. Go to `http://127.0.0.1:8000/admin`
2. Default username and password are `admin`
> [!NOTE]
> If the username or password doesn't work, create an account by running `python manage.py createsuperuser`   
3. Add users or messages

## Sentiment Analysis
All three deployment methods are implemented in the [views.py](sentimentAnalysis/textInput/views.py).
Uncomment the relative code to apply the method

* [Locally Deployed Model](#Locally-Deployed-Model)
* [Cloud Deployed Model](#Cloud-Deployed-Model)
* [Docker Deployed Model](#Docker-Deployed-Model)

> [!IMPORTANT]
> Only one model should be selected at a time. If not, the program may be extremely slow or crash. 

### Locally Deployed Model
To use the locally deployed model, uncomment the code under `A. locally deployed model` at the **top of the file** and in the **perform_sentiment_analysis** function.

### Cloud Deployed Model
To use the cloud deployed model, uncomment the code under `B. cloud deployed model` at the **top of the file** and in the **perform_sentiment_analysis** function.

### Docker Deployed Model
To use the Docker deployed model, uncomment the code under `C. Docker deployed model` at the **top of the file** and in the **perform_sentiment_analysis** function.
> [!NOTE]
> The Docker container is stored locally. 
