from flask import Flask, request
import pandas as pd  
import pickle 
import flasgger
from flasgger import Swagger


app = Flask(__name__)                 #Mandate  skewness,curtosis,entropy
Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route('/predict', methods=['GET'])          #GET HTTP request method
def predict_banknote_authentication():
    """ Bank Note Authentication
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true 
    responses:
        200:
            description: The output values
            
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    
    return "The Prediction is"+str(prediction)
    
    
@app.route('/predict_file_csv', methods=['POST'])        #POST  HTTP request method
def predict_banknote_authentication_by_csv():
    """Bank Note Authentication 
    ---
    parameters: 
      - name: file
        in: formData
        type: file
        required: true
    responses: 
        200: 
            description: The output values 
                        
    """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    
    return str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
