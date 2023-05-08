#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
from keras.models import sequential
from tensorflow.keras import layers


# In[2]:


[]  classifier = sequential()
classifier.add(keras.layers.Dens(6,activation = 'relu', input_dim = 6))
classifier.add(keras.layers.Dropout(0.50))
classifier.add(keras.layers.Dens(6,activation = 'relu'))
classifier.add(keras.layers.Dropout(0.50))
classifier.add(keras.layers.Dens(1,activation = 'sigmoid'))



# In[5]:


loss_1 = tf.keras.losses.BinaryCrossentropy()
classifier.compile(optimizer = 'Adam',loss = loss_1, metrics = ['accuracy'])
classifier.fit(X_train, Y_test, batch_size = 20, epochs = 100)


# In[6]:


[] import pickle
pickle.dump(knn,open("Placement.pkl",'wb'))
model = pickle.load(open('Placement.pk1', 'rb'))


# In[7]:


<section id="hero"class="d-flex flex-column justify-content-center">
<div class="container">
<div class="row justify-content-center">
<div class="col-xl-8">
<h1>Identifying Patterns and Treands in Campus Placement Data using Machine Learning</h1>
</div>
</div>
</div>
</section><!-- End Hero -->


# In[8]:


<section id="about" class= "about">
<div class="container">
<div class="section-title">
<h2>File the details</h2>
</div>
<div class="row content">
div class= "first">
<form action="{{url_-for('y_predict')}}" method="POST">
<input type="number" id="sen1" name="sen1" placeholder="Age">
<input type="number" id="sen2" name="sen2" placeholder="Gender M(0), F(0)">
<input type="number" id="sen3" name="sen3" placeholder="Stream CS(0),IT(1),ECE(2),Mech(3),EEE(4),Civil">
<input type="number" id="sen4" name="sen4" placeholder="Internships">
<input type="number" id="sen5" name="sen5" placeholder="CGPA">
<input type="number" id="sen6" name="sen6" placeholder="Number of backlogs">
<input type="submit" value="submit" >
</form>
</div>
</div>
</div>
</section><!-- End About Us Section -->


# In[9]:


<section id="hero"class="d-flex flex-column justify-content-center">
<div class="container">
<div class="row justify-content-center">
<div class="col-xl-8">
<h1> The Prediction is : {{y}}</h1>
    <h3> 0 represents Not-placed </h3>
    <h3> 1 represents placed<h2>
    </div>
    </div>
    </div>
    </section><! --End Hero -->


# In[12]:


from flask import Flask, render_template , request
app=Flask(__name__)
import pickle
import joblib
model=pickle.load(open("placement123.pkl",'rb'))
ct=joblib.load('placement')


# In[14]:


@app.route('/')
def hello():
    return render_template("index.html")


# In[16]:


@app.route('/guest', methods = ["Post"])
def Guest():
    sen1=request.form["sen1"]
    sen2=request.form["sen2"]
    sen3=request.form["sen3"]
    sen4=request.form["sen4"]
    sen5=request.form["sen5"]
    sen6=request.form["sen6"]
    @app.route('/y_predict', methods = ["POST"])
    def y_predict():
        x_test = [[(yo) for yo in request.form.values()]]
        prediction =model.predict(x_test)
        prediction = prediction[0]
        return render_template("secondpage.html",y=prediction)


# In[17]:


app.run(debug=True)


# In[20]:


* Serving Flask app "app" (lazy loading)
Environment : production
    Use a production WSGI server instead.
    Debug mode: on
        Restarting with watchdog(windowsapi)
        Debugger is active!
        Debugger PIN: 146-359-21
            Running on http://127.0.0.1:5000/ 


# In[ ]:




