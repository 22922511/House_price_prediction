import pickle

import pandas as pd


with open(r'model/House_price_prediction_model.pkl','rb') as f:
    model=pickle.load(f) 

MODEL_VERSION='1.0.0.0'    
Model_loaded =model is not None
def Predict_output(df:pd.DataFrame):
    return model.predict(df)[0]