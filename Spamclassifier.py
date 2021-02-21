# -*- coding: utf-8 -*-
import pandas as pd
import pickle

messages=pd.read_csv(r'C:\Users\shruti and rahul\Desktop\Python\Spyder Practice\Spam classifier\spam.csv',encoding='latin-1')
messages.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'],axis=1,inplace=True)

import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer

ps=PorterStemmer()
corpus=[]

for i in range(len(messages)):
     corpus.append(messages['message'][i])

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()

pickle.dump(cv,open('BOW.pkl','wb'))

y=pd.get_dummies(messages['class'])
y=y.iloc[:,1].values
 

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest=train_test_split(X, y,test_size=0.2, random_state=42)  

from sklearn.naive_bayes import MultinomialNB
spam_detect=MultinomialNB().fit(Xtrain,ytrain)

pickle.dump(spam_detect,open('model.pkl','wb'))

ypred=spam_detect.predict(Xtest)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
accuracy=accuracy_score(ytest,ypred)
cf=confusion_matrix(ytest,ypred)
report=classification_report(ytest,ypred)

