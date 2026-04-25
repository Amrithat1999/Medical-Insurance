# from fastapi import FastAPI
# import pickle
# import numpy as np
# import pandas as pd
# from format import FormatData


# app = FastAPI()

# model = pickle.load(open("model.pkl", "rb"))

# le_sex = pickle.load(open("le_sex.pkl", "rb"))
# le_region = pickle.load(open("le_region.pkl", "rb"))
# le_smoker = pickle.load(open("le_smoker.pkl", "rb"))



# @app.get("/")
# def insurance():
#     return "Welcome to the Insurance API"

# #age	sex	bmi	children	smoker	region	charges
# @app.post('/predict')
# def prediction(data:FormatData):
#     data = data.dict()
#     age=data['age']
#     bmi=data['bmi']
#     children=data['children']
#     sex = le_sex.transform([data['sex']])[0]
#     region = le_region.transform([data['region']])[0] 
#     smoker = le_smoker.transform([data['smoker']])[0]


#     input_data = [[age, sex, bmi, children, smoker, region]]
#     predictions = model.predict(input_data)
#     prediction = predictions[0]
#     return {
#         "The predicted insurance charge is: ": float(prediction)
            

#     }
   

# @app.get("/predict")
# def get_data(data: FormatData):
#     data
#     return data
 


from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import pickle

from db_config import SessionLocal, engine
from db_format import InsuranceData
import db_format
from format import FormatData

app = FastAPI()

db_format.Base.metadata.create_all(bind = engine)

# Load model
model = pickle.load(open("model.pkl", "rb"))
le_sex = pickle.load(open("le_sex.pkl", "rb"))
le_region = pickle.load(open("le_region.pkl", "rb"))
le_smoker = pickle.load(open("le_smoker.pkl", "rb"))

# Dependency (DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Insurance API with PostgreSQL"}


@app.post("/predict")
def predict(data: FormatData, db: Session = Depends(get_db)):

    # Convert input
    age = data.age
    bmi = data.bmi
    children = data.children

    sex_encoded = le_sex.transform([data.sex])[0]
    region_encoded = le_region.transform([data.region])[0]
    smoker_encoded = le_smoker.transform([data.smoker])[0]

    input_data = [[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]]

    prediction = model.predict(input_data)[0]

    # ✅ Store in PostgreSQL
    db_data = InsuranceData(
        age=age,
        sex=data.sex,
        bmi=bmi,
        children=children,
        smoker=data.smoker,
        region=data.region,
        charges=float(prediction)
    )

    db.add(db_data)
    db.commit()
    db.refresh(db_data)

    return {
        "charges": float(prediction),
        "id": db_data.id
    }