import numpy as np
import pandas as pd
import csv 
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('dataset.csv')
heartDisease = heartDisease.replace('?',np.nan)


# print('Sample instances from the dataset are given below')
# print(heartDisease.head())

# print('\n Attributes and datatypes')
# print(heartDisease.dtypes)

model= BayesianNetwork([('age','heartdisease'),('gender','heartdisease'),('exang','heartdisease'),('cp','heartdisease'),('heartdisease','restecg'),('heartdisease','chol'),('heartdisease','fbs'),('trestbps','heartdisease')])
# print('\nLearning CPD using Maximum likelihood estimators')
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)
# Check variable names in the model
# print(model.nodes())

# # Check column names in the data
# print(heartDisease.columns)
# print('\n Inferencing with Bayesian Network:')
HeartDiseasetest_infer = VariableElimination(model)
print('\n 1. Probability of HeartDisease given evidence= restecg and cholesterol = 233')
q1=HeartDiseasetest_infer.query(variables=['heartdisease'],evidence={'chol':233})
print(q1)