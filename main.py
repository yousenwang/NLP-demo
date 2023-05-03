from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
# import nltk
# import sklearn

app = FastAPI()


class Question(BaseModel):
    user_input:str


# repalce with database
faq = pd.read_csv('english_FAQ.csv')

str_to_numerical = joblib.load('trained_estimators/trained_tfidf_vectorizer.pkl')
info_retrieve = joblib.load('trained_estimators/trained_kd_tree.pkl')

@app.post("/")
async def answer_endpoint(input_q: Question):
    question = input_q.dict()
    numerical = str_to_numerical.transform([question["user_input"]]).toarray()
    distance, idx = info_retrieve.query(numerical, k=1)

    best_answer = list(enumerate(idx[0]))[0]

    return {
        "user_input": question["user_input"],
        "distance": distance[0][best_answer[0]],
        "preidcted_q": faq["question"][best_answer[1]],
        "preidcted_ans": faq["reply"][best_answer[1]],
    }
@app.get("/")
async def root():
    return {
        "message": "this is get"
    }