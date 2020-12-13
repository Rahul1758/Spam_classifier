from flask import Flask,render_template,request,url_for
import pandas as pd
import pickle

# load the model from disk
model=pickle.load(open('model.pkl', 'rb'))
cv=pickle.load(open('BOW.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message =request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction =model.predict(vect)
    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
	app.run(debug=True)