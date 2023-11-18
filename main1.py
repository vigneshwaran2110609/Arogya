from flask import Flask,request,render_template,redirect,url_for,abort,flash
import mysql.connector
from main import final,bpp,sugarr,chole
import time


conn=mysql.connector.connect(host="localhost", user="root", password="vijay", database ='login')
try:
    if conn.is_connected():
        print("yes")
except:
    print("Errored")

cur=conn.cursor()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'netrum illai naalai illai'

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    name1=request.form['username']
    pass1=request.form['password']
    cur.execute("SELECT USERNAME,PASSWORD FROM ID;")
    res=cur.fetchall()
    username1 = []
    password1 = []
    for i in res:
        username1.append(i[0])
        password1.append(i[1])
    if name1 in username1:
        ind=username1.index(name1)
        if password1[ind]==pass1:
            print('verified')
            return render_template('launch.html')
        else:
            return render_template('index1.html')

@app.route('/cholesterol')
def cholesterol():
    return render_template('chol.html')

@app.route('/chol' ,methods=['POST','GET'])
def chol():
    cholo=request.form['chol_level']
    print(cholo)
    v=chole(int(cholo))
    v=int(v)
    return render_template('final.html',value_from_python=v)

@app.route('/sug')
def sug():
    return render_template('sugar.html')

@app.route('/sugarlevel',methods=['POST','GET'])
def sugarlevel():
    sug=request.form['sugar']
    print(sug)
    v=sugarr(sug)
    v=int(v)
    time.sleep(10)
    return render_template('final.html',value_from_python=v)

@app.route('/bloodp')
def bloodp():
    return render_template('bp.html')

@app.route('/bpressure',methods=['POST','GET'])
def bpressure():
    bp1=request.form['bp']
    print(bp1)
    v=bpp(int(bp1))
    v=int(v)
    time.sleep(10)
    return render_template('final.html',value_from_python=v)

@app.route('/other')
def other():
    return render_template('others.html')

@app.route('/oth',methods=['POST','GET'])
def oth():
    attack=request.form['rate']
    smoke=request.form['smoke']
    ecg=request.form['ecg']
    v=final(attack,smoke,ecg)
    v=int(v)
    print(attack,smoke,ecg)

    return render_template('final.html',value_from_python=v)

app.run()