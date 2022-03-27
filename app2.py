#import libraries
import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

#initialize flask app
app=Flask(__name__)
model=pickle.load(open('diabetes_model.pkl','rb'))

#default page of our web page
@app.route('/')
def home():
    return render_template('index.html')

#to use predict button in web app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI 
    '''
    int_features=[float(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    
    output=round(prediction[0],2)
    
    if output==1:
        text='you have diabetes'
    else:
        text='No diabetes'
            
    return render_template('index.html',prediction_text=text)
        
if __name__=="__main__":
            app.run(debug=True)
    