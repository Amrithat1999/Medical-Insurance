from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from format import FormatData


app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

le_sex = pickle.load(open("le_sex.pkl", "rb"))
le_region = pickle.load(open("le_region.pkl", "rb"))
le_smoker = pickle.load(open("le_smoker.pkl", "rb"))



@app.get("/")
def insurance():
    return "Welcome to the Insurance API"

#age	sex	bmi	children	smoker	region	charges
@app.post('/predict')
def prediction(data:FormatData):
    data = data.dict()
    age=data['age']
    bmi=data['bmi']
    children=data['children']
    sex = le_sex.transform([data['sex']])[0]
    region = le_region.transform([data['region']])[0] 
    smoker = le_smoker.transform([data['smoker']])[0]


    input_data = [[age, sex, bmi, children, smoker, region]]
    predictions = model.predict(input_data)
    prediction = predictions[0]
    return {
        "The predicted insurance charge is: ": float(prediction)
            

    }
   
 

    





