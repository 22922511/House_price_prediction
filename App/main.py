import json
import pandas as pd
import numpy as np
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from App.predict_output import Predict_output,MODEL_VERSION,Model_loaded
from App.schema.user_input import UserInput
from App.schema.output_validation import Api_response
app=FastAPI()


with open(r'config/columns_name.json','r') as f:
    columns_name=json.load(f)
columns_name=columns_name['columns']    
    

length_ip=len(columns_name)  
@app.get('/home')
def home():
   return {'message' : 'House price pridection API'}

@app.get('/about')
def about():
   return {'status' : 'ok',
           'Version':MODEL_VERSION,
           'Model loaded' : Model_loaded}

@app.post('/predict',response_model=Api_response)
def input_from_user(data:UserInput):
    
 x=np.zeros(length_ip)
 location=(data.location)
 location=location.lower()
 if location in columns_name:
  index_of_location=columns_name.index(location)
  x[index_of_location]=1

 x[0]=data.total_sqft
 x[1]=data.bath
 x[2]=data.BHK
 
 x_df = pd.DataFrame([x], columns=columns_name)
 try:
  result= Predict_output(x_df)
  return JSONResponse(status_code=200, content={'predicted_category': result})
 except Exception as e:
  return JSONResponse(status_code=500,content=str(e))
