from flask import Flask,url_for
from flask.templating import render_template


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


app.run(debug=True)