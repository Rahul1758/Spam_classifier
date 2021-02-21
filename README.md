# SMS Spam classifier

***1. DESCRIPTION***
--------------
Everyone receives tons of spam messages on their smartphones everyday. Nowadays smartphones are also smart enough to identify the spam messages and automatically dump them to the spam folder to save your time. This application is a glimpse of identification part that the smartphone does but using just Machine learning to solve the problem.

**2. DATA**
--------------
The dataset for was obtained from https://archive.ics.uci.edu/ml/machine-learning-databases/00228/.

**3. MODEL TRAINING**
--------------
This classification task was performed using the concepts of NLP like Stemming & Bag of Words (BOW).
The training model used for this classification is Multinomial Naive Bayes.
The library used to create this application is NLTK (Natural Language Tool Kit) which one of the popular most widely used libraries for NLP tasks.

**4. DEPLOYMENT**
--------------
The app uses Flask framework to create a front-end API and is deployed on Heroku along with Dockers.
Please feel free to try out the app by hitting this link!! https://nlp-sms-spam-classifier.herokuapp.com/

