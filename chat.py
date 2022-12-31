#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
import random
import numpy as np
import json
import pickle
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
lemmatizer=WordNetLemmatizer()

with open('breastCancer.json') as json_file:
    intents = json.load(json_file)

words=pickle.load(open('words.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))
model=load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
  sentence_words=nltk.word_tokenize(sentence)
  sentence_words=[lemmatizer.lemmatize(word) for word in sentence_words]
  return sentence_words

def bag_of_words(sentence):
  sentence_words=clean_up_sentence(sentence)
  bag=[0]*len(words)
  for w in sentence_words:
    for i,word in enumerate(words):
      if word == w:
        bag[i]=1
  return np.array(bag)

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

def get_response(intents_list,intents_json):
    result = None
    tag=intents_list[0]['intent']
    print(intents_list[0])
    list_of_intents=intents_json['intents']
    for i in list_of_intents:
        if tag in i['tags']:
            result=i['responses']
            break
    return result


def main_(message:str):
    while True:
        ints=predict_class(message)
        if len(ints) > 0:
            res=get_response(ints,intents)
            return res
        else:
            return "I Donot know about it"


# In[ ]:




