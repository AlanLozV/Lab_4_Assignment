# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:24:30 2022

@author: alan-
"""

import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
pickle_in = open("fish_classifier.pkl", "rb")
model = pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predict():
    """ Rendering results on HTML GUI
    """
    features =  [x for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    
    return render_template('index.html', prediction_text = "The fish belongs to the species {}".format(str(prediction)))


if __name__=='__main__':
    app.run()