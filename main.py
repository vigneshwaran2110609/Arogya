import numpy as np
import pandas as pd
import random
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pymongo import MongoClient
client = MongoClient("mongodb+srv://vignesh:vignesh@cluster0.o7p97ka.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("Arogya")
records =  db.Records
heartDisease = pd.read_csv(r"C:\Users\vicky\OneDrive\Desktop\projectvijayversion\project\dataset.csv")
heartDisease = heartDisease.replace('?',np.nan)

model= BayesianNetwork([('age','heartdisease'),('gender','heartdisease'),('thalach','heartdisease'),('cp','heartdisease'),('heartdisease','restecg'),('heartdisease','chol'),('heartdisease','fbs'),('trestbps','heartdisease')])

model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

# print('\n Inferencing with Bayesian Network:')
HeartDiseasetest_infer = VariableElimination(model)

def bpp(val,val1,val2,val3):
    
    if val1>120:
        val1=1
    else:
        val1=0
    print('\n 1. Probability of HeartDisease given evidence= restecg and cholesterol = 233')
    q1=HeartDiseasetest_infer.query(variables=['heartdisease'],evidence={'trestbps':val,'fbs':val1,'chol':val2,'thalach':val3})
    l=len(q1.values)
    if max(q1.values)==1:
        return random.randint(70,100)
    vj=sum(q1.values)*100
    vj=vj/l
    vj=round(vj)
    vj=int(vj)
    return vj