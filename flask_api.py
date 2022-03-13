
from flask import Flask, request
import pandas as pd 
import numpy as np  
import pickle 


app = Flask(__name__)                 #Mandate  skewness,curtosis,entropy

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route('/predict', methods=['GET'])          #GET HTTP request method
def predict_banknote_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "The Prediction is"+str(prediction)
    
    
@app.route('/predict_file_csv', methods=['POST'])        #POST  HTTP request method
def predict_banknote_authentication_by_csv():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    
    return str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

