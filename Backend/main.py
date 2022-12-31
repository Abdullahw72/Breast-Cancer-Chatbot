from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from chat import main_, addQuestionInDataSet
from train import train

app = FastAPI()

class QA(BaseModel):
    question: str


## GET API for train the model
@app.get('/api/train')
def trainModel():
    """
        this function call train function of the model 
        train the model on new DataSet
    """
    msg = train()
    return {'msg':msg}

class Questions(BaseModel):
    question: str
    index: int 

## POST API for Add new question in a dataSet
@app.post('/api/addQuestion')    
def addQuestion(request: Questions):
    """
        requestBody contain the question
        and index of the response to add that 
        question on a relevant index
    """
    msg = addQuestionInDataSet(request.question, request.index)
    return {'msg':msg}
   
## POST API for to response the user  
@app.post('/api/predict')
def predict(request: QA):
    """
        requestBody contain the question
        in a string fromat and it return the response
    """
    msg = main_(request.question.lower())
    print(msg)
    return {'data': msg}
