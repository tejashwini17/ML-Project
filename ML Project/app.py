from flask import Flask,render_template,request
import pickle
from joblib import load
from itertools import chain
app = Flask(__name__)
model =pickle.load(open('Grade.pkl','rb'))
global b1
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/login',methods=["POST"])
def func2():
    x_test = [[str(x) for x in request.form.values()]]
    g = request.form['g']
    if(g=="male"):
        a1=1
    if(g=="female"):
        a1=0
    re = request.form['re']
    if(re=="group A"):
        b1=0
    elif(re=="group B"):
        b1=1
    elif(re=="group C"):
        b1=2
    elif(re=="group D"):
        b1=3
    elif(re=="group E"):
        b1=4
    edu = request.form['edu']
    if(edu=="associate's degree"):
        c1=0
    elif(edu=="bachelor's degree"):
        c1=1
    elif(edu=="high school"): 
        c1=2
    elif(edu=="master's degree"):
         c1=3
    elif(edu=="some college"):
         c1=4
    elif(edu=="some high school"):
         c1=5    
    d= request.form['d']
    if(d=="standard"):
        d=0
    if(d=="free/reduced"):
        d=1
    tpc=request.form['tpc']
    if(tpc=="none"):
        e1=1
    if(tpc=="completed"):
        e1=0
    rs=request.form['rs']
    ms = request.form['ms']
    ws = request.form['ws']
    l = [[a1,b1,c1,d,e1,rs,ms,ws]]
    prediction =  model.predict((l))
 
    if prediction == 0:
        my_prediction='Grade A'
    elif prediction ==1:
        my_prediction='Grade B'
    elif prediction ==2:
        my_prediction='Grade C'
    elif prediction ==3:
        my_prediction='Grade D'
    elif prediction ==4:
        my_prediction='Grade E'
    else:
        my_prediction =  'Fail or Re appear'
        return render_template("result_page_fail.html",prediction = my_prediction)
    return render_template("index.html",y="Predicted Student Performance as {}".format(my_prediction))

if __name__ == '__main__':
    app.run(debug = True)
    