#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_tempate , request
app=Flask(_name_)
import pickle
import joblib
model=pickle.load(open("placement123.pkl",'rb'))
ct=joblib.load('placement')
@app.route('/')
def hello():
    return render_temple("index.html")
@app.route('/guest', methods =["POST"])
def Guest();
    sen1=request.from["sen1"]
    sen2=request.from["sen2"]
    sen3=request.from["sen3"]
    sen4=request.from["sen4"]
    sen5=request.from["sen5"]
    sen6=request.from["sen6"]
@app.route('/y_predict',methods =["POST"])
def y_predict():
    x_test = [[(yo) for yo in request.from.values()]]
    prediction =model.predict(x_test)
    Prediction =prediction[0]
    return render_template("secondpage.html",y=prediction)
app.run(debug=True)
    

