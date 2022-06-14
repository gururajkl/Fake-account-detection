# Importing essential libraries and modules
import pandas as pd
import numpy as np

from flask import Flask, render_template, request, Markup
import pickle


# Load ML model
model = pickle.load(open('RandomForest.pkl', 'rb')) 

app = Flask(__name__)

@ app.route('/')
def home():
    title = 'Home'
    return render_template('index.html', title=title)

# @ app.route('/yeild')
# def yeild():
#     title = 'Rice-yeild Suggestion'
#     return render_template('crop_yeild.html', title=title)

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        features = [float(i) for i in request.form.values()]
        print(features)
        # Convert features to array
        array_features = [np.array(features)]
        # Predict features
        prediction = model.predict(array_features)
        
        output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
        if output == 1:
            return render_template('main_page.html', 
                                result = 'The Twitter Account is Fake!')
        else:
            return render_template('main_page.html', 
                                result = 'The Twitter Account is Not Fake!')
    
    return render_template('main_page.html')

if __name__ == '__main__':
#Run the application
    app.run()