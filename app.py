from assets.fact import fact
from assets.oddoreven import oe
from assets.armstrong import armstrong
from assets.primeornot import PrimeChecker
from flask import Flask,url_for,request
from flask.templating import render_template
from assets import calcul



app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calc',methods=['GET','POST'])
def calc():
    if request.method=='POST' and 'number1' in request.form and 'number2' in request.form and 'operator' in request.form:
        number1=int(request.form['number1'])
        number2=int(request.form['number2'])
        operator=request.form['operator']
        result=calcul(number1,number2,operator)
        return render_template('calc.html',result=result)

    return render_template('calc.html')

@app.route('/func',methods=['GET','POST'])
def func():
    if request.method =="POST" and 'number1' in request.form:
        try:
            number1=int(request.form['number1'])
            func=request.form['func']
            if func =="armstrong":
                result=armstrong(number1)
                if result:
                    msg="{} is an Armstrong number".format(number1)
                else:
                    msg="{} is not an Armstrong number".format(number1)
                return render_template('func.html',msg=msg)
            elif func =="prime":
                result=PrimeChecker(number1)
                if result:
                    msg="{} is a Prime number".format(number1)
                else:
                    msg="{} is not a Prime number".format(number1)
                return render_template('func.html',msg=msg)
            elif func =="oe":
                result=oe(number1)
                if result=="Even":
                    msg="{} is an Even number".format(number1)
                else:
                    msg="{} is an Odd number".format(number1)
                return render_template('func.html',msg=msg)
            else:
                result=fact(number1)
                msg="The factorial of {} is {}".format(number1,result)
                return render_template('func.html',msg=msg)
        except:
            return render_template('func.html',msg="Enter a Valid Number!")
    return render_template('func.html')

if __name__=="__main__":
    app.run(debug=True)