#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import json
import pickle
import numpy as np
import pandas as pd

import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import metrics

def train():
    lemmatizer=WordNetLemmatizer()

    with open('breastCancer.json') as json_file:
        intents = json.load(json_file)

    #print(intents)

    words=[]
    classes=[]
    documents=[]
    ignore_letters=['?','!','.',',']

    for intent in intents['intents']:
      for pattern in intent['patterns']:
        word_list=nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tags']))
        if intent['tags'] not in classes:
          classes.append(intent['tags'])


    words =[lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
    words = sorted(set(words))
    classes=sorted(set(classes))
    pickle.dump(words,open('words.pkl','wb'))
    pickle.dump(classes,open('classes.pkl','wb'))



    training=[]
    output_empty=[0]*len(classes)

    for document in documents:
      bag=[]
      word_patterns=document[0]
      words = [lemmatizer.lemmatize(word.lower()) for word in words if word and word not in ignore_letters]
      for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

      output_row=list(output_empty)
      output_row[classes.index(document[1])]=1
      training.append([bag,output_row])

    random.shuffle(training)
    training=np.array(training)

    train_x=list(training[:,0])
    train_y=list(training[:,1])

    model=Sequential()
    model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(len(train_y[0]),activation='softmax'))

    sgd=SGD(learning_rate=0.0001,decay=1e-6,momentum=0.9,nesterov=True)


    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy','Precision','Recall'])
    # model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=METRICS)
    hist = model.fit(np.array(train_x),np.array(train_y),epochs=50,batch_size=12,verbose=1)
    model.save('chatbotmodel1.h5', hist)
    return 'training Done'

