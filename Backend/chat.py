#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#### Libraries that we use for giving the response
import nltk
import random
import numpy as np
import json
import pickle
import utils
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
lemmatizer=WordNetLemmatizer() 

## load the json file and store in a variable
with open('breastCancer.json') as json_file:
    intents = json.load(json_file)


words=pickle.load(open('words.pkl','rb'))  ## load unique word vocabulary
classes=pickle.load(open('classes.pkl','rb')) ## load unique clases
model=load_model('chatbotmodel1.h5') ## load the train model

correctQues = ""


## add new question in the dataset
def addQuestionInDataSet(quest: str, ind: int):
    intents["intents"][ind]['patterns'].append(quest)
    with open("breastCancer1.json", "w") as f:
        f.write(json.dumps(intents))
    return "Question added Successfully"
    

## correct spelling by using edit distance algorithm and replace the word with minimum edit distance
def correct_spelling(sentence):
  sentence_list = []
  for sent in sentence.split():
    word = ""
    dist = 5
    for w in words:
        n = len(sent)
        m = len(w)
        dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
        diff = utils.minDis(sent, w, n, m, dp)
        if dist > diff:
            dist = diff
            word = w
    sentence_list.append(word)
  return ' '.join(sentence_list)


## preProcessing the question by correcting
## tokenize the correct question
## lemmatize the tokenize question
def clean_up_sentence(sentence):
  global correctQues
  sentence = correct_spelling(sentence)
  correctQues = sentence
  sentence_words=nltk.word_tokenize(sentence)
  sentence_words=[lemmatizer.lemmatize(word) for word in sentence_words]
  return sentence_words


## store the word counts in a bag of word list
## and return numpy array 
def bag_of_words(sentence):
  sentence_words=clean_up_sentence(sentence)
  bag=[0]*len(words)
  for w in sentence_words:
    for i,word in enumerate(words):
      if word == w:
        bag[i]=1
  return np.array(bag)

## predict the class using the train model and the bag of word array 
## and return the result with the highest probability
def predict_class(sentence):
  bow=bag_of_words(sentence)
  res=model.predict(np.array([bow]))[0]
  ERROR_THRESHOLD=0.25
  results=[[i,r] for i,r in enumerate(res) if r> ERROR_THRESHOLD]
  results.sort(key=lambda x:x[1],reverse=True)
  return_list=[]
  for r in results:
    return_list.append({'intent': classes[r[0]],'probability':str(r[1])})
  return return_list


## return the correct response by using tags and return correct question, index and response
def get_response(intents_list,intents_json):
    global correctQues
    result = None
    tag=intents_list[0]['intent']
    print(intents_list[0])
    list_of_intents=intents_json['intents']
    ind = -1
    for index, i in enumerate(list_of_intents):
        if tag in i['tags']:
            result=i['responses']
            ind = index
            break
    return result,ind,correctQues


## main function
def main_(message:str):
    ints=predict_class(message)
    if len(ints) > 0:
        res=get_response(ints,intents)
        return res
    else:
        return ["I Donot know about it",-1,""]


# In[ ]:




