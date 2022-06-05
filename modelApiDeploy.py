from flask import Flask,request,jsonify
import  joblib
import pandas as pd

# crate flask app

app = Flask(__name__)

# connect postApi call --> predict Function()
@app.route('/predict',methods=['POST'])

def predict():
    #Get json
    feat_data = request.json
    #convert json to pandas DF
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    #predict
    prediction = list(model.predict(df))
    return jsonify({'prediction':str(prediction)})

#Load my model and load column names
if __name__ == '__main__':
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('col_names.pkl')
    app.run(debug=True)