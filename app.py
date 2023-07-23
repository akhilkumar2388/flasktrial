#create a simple flask condaapplication
from flask import Flask,redirect,url_for,render_template,Request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>hello world</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<score>')
def success(score):
    return score

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    

if __name__=='__main__':
    app.run(debug=True)