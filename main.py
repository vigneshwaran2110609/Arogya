import numpy as np
import pandas as pd
import csv 
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('heart.csv')
heartDisease = heartDisease.replace('?',np.nan)

# print('Sample instances from the dataset are given below')
# print(heartDisease.head())

# print('\n Attributes and datatypes')
# print(heartDisease.dtypes)

model= BayesianNetwork([('Age','HeartDisease'),('Sex','HeartDisease'),('ChestPainType','HeartDisease'),('HeartDisease','MaxHR'),('HeartDisease','RestingECG'),('HeartDisease','Cholesterol'),('HeartDisease','FastingBS'),('RestingBP','HeartDisease')])
# print('\nLearning CPD using Maximum likelihood estimators')
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

# print('\n Inferencing with Bayesian Network:')
HeartDiseasetest_infer = VariableElimination(model)
def chole(val):

    print('\n 1. Probability of HeartDisease given evidence= restecg and cholesterol = 233')
    q1=HeartDiseasetest_infer.query(variables=['HeartDisease'],evidence={'Cholesterol':val})
    print(q1)
    vj=max(q1.values)*100
    vj=round(vj)
    vj=int(vj)
    return vj

def bpp(val):
    print('\n 1. Probability of HeartDisease given evidence= restecg and cholesterol = 233')
    q1=HeartDiseasetest_infer.query(variables=['HeartDisease'],evidence={'RestingBP':val})
    print(q1)
    vj=max(q1.values)*100
    vj=round(vj)
    vj=int(vj)
    return vj

def final(val1,val2,val3):
    val1=int(val1)
    # val2=int(val2)
    val3=int(val3)
    q1=HeartDiseasetest_infer.query(variables=['HeartDisease'],evidence={'RestingECG':val3,'MaxHR':val1})
    print(q1)
    vj=max(q1.values)*100
    vj=round(vj)
    vj=int(vj)
    return vj

def sugarr(val):
    val=int(val)
    if val>120:
        val=1
    else:
        val=0
    q1=HeartDiseasetest_infer.query(variables=['HeartDisease'],evidence={'FastingBS':val})
    print(q1)
    
    vj=max(q1.values)*100
    vj=round(vj)
    vj=int(vj)
    return vj


# print('\n 2. Probability of HeartDisease given evidence male ')
# q2=HeartDiseasetest_infer.query(variables=['heartdisease'],evidence={'restecg':0})
# print(q2)
# print(max(q2.values))

