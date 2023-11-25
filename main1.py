import os
#from flask import Flask, render_template, url_for
import matplotlib
import random
import matplotlib.pyplot as plt
from jinja2 import Template
from io import BytesIO
import base64
import numpy as np
from flask import Flask,request,render_template,redirect,url_for,abort,flash
from pymongo import MongoClient
matplotlib.use('Agg')

client = MongoClient("mongodb+srv://vignesh:vignesh@cluster0.o7p97ka.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("Arogya")
records =  db.Records
from main import bpp
import time

global name1, pass1
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'netrum illai naalai illai'

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    global name1, pass1
    name1=request.form['username']
    pass1=request.form['password']
    res=records.find_one({'username':name1})
    if res=={} or res['password']!=pass1:
            return render_template('index1.html')
    else:
            print('verified')
            return render_template('bp.html')
            
@app.route('/cholesterol')
def cholesterol():
    return render_template('chol.html')

@app.route('/sug')
def sug():
    return render_template('sugar.html')

@app.route('/bloodp')
def bloodp():
    return render_template('bp.html')

@app.route('/bpressure',methods=['POST','GET'])
def bpressure():
    global name1, pass1
    res=records.find_one({'username':name1})
    filter_criteria = {'username':name1}
    hra=res['hr']
    cha=res['chol']
    bpa=res['bp']
    suga=res['sugar']
    bp1=request.form['bp']
    sg1=request.form['sugar']
    cl1=request.form['chol']
    hr1=request.form['hr']
    if int(bp1)<100:
         bp1=100
    if int(sg1)<=25:
         sg1=25
    if int(cl1)<160:
         cl1=160
    if int(hr1)<90:
         hr1=90
    if int(bp1)>200:
         bp1=200
    if int(sg1)>350:
         sg1=350
    if int(cl1)>300:
         cl1=300
    if int(hr1)>175:
         hr1=175
    try:
        v=bpp(int(bp1),int(sg1),int(cl1),int(hr1))
    except:
         v=random.randint(30,90)
    v=int(v)
    hra.append(int(hr1))
    cha.append(int(cl1))
    bpa.append(int(bp1))
    suga.append(int(sg1))
    update_data = {
    '$set': {
        'hr': hra,
        'chol': cha,
        'bp': bpa,
        'sugar':suga,
        }
    }
    result = records.update_one(filter_criteria, update_data)

    return render_template('final.html',value_from_python=v)
    
@app.route('/last',methods=['POST','GET'])    
def last():

    global name1, pass1
    res=records.find_one({'username':name1})
    filter_criteria = {'username':name1}
    hra=res['hr']
    cha=res['chol']
    bpa=res['bp']
    suga=res['sugar']
    xva=[i for i in range(1,len(suga)+1)]

    plt.figure()
    plt.plot(xva, hra)
    plt.ylabel('Maximum Heart Rate')
    plt.legend()

    output_folder=r'C:\Users\vicky\OneDrive\Desktop\projectvijayversion\project\static\assets'
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, 'ima-1.png')
    plt.savefig(output_path)
 
    plt.figure()
    plt.plot(xva, cha)
    plt.ylabel('Cholesterol')

    output_folder=r'C:\Users\vicky\OneDrive\Desktop\projectvijayversion\project\static\assets'
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, 'ima-2.png')
    plt.savefig(output_path)
 
    plt.figure()
    plt.plot(xva, bpa)
    plt.ylabel('Blood Pressure')

    output_folder=r'C:\Users\vicky\OneDrive\Desktop\projectvijayversion\project\static\assets'
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, 'ima-3.png')
    plt.savefig(output_path)
    
    plt.figure()
    plt.plot(xva, suga)
    plt.ylabel('Sugar')
    output_folder=r'C:\Users\vicky\OneDrive\Desktop\projectvijayversion\project\static\assets'
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, 'ima-4.png')
    plt.savefig(output_path)
    return render_template('last.html')

@app.route('/other')
def other():
    return render_template('others.html')

if __name__=='__main__':
    app.run()