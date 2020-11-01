from flask import Flask,request,render_template
import joblib
import numpy as np

app = Flask(__name__)
model=joblib.load("model.pkl")
@app.route("/")
def hello():
    return render_template('index1.html')
@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
       Squareft = request.form["Squareft"]
       Squareft = int(Squareft)
       print(Squareft)
       Price = model.predict([[Squareft]])
       return render_template('index1.html',prediction_test="Price = {}".format(Price))

if __name__ =="__main__":
    app.run()