from flask import Flask,url_for,request
from flask.templating import render_template



app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calc',methods=['GET','POST'])
def calc():
    if request.method=='POST' and 'number1' in request.form and 'number2' in request.form and 'operator' in request.form:
        number1=request.form['number1']
        number2=request.form['number2']
        operator=request.form['operator']
        print(number1,number2,operator)

    return render_template('calc.html')

@app.route('/func',methods=['GET','POST'])
def func():
    if request.method =="POST" and 'number1' in request.form:
        number1=request.form['number1']
        func=request.form['func']
        if func =="armstrong":
            return "arm"
        elif func =="prime":
            return "prime"
        elif func =="oe":
            return "oe"
        else:
            return "factorial"
        print(number1,func)
    return render_template('func.html')


app.run(debug=True)