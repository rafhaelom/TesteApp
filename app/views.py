from app import app
from datetime import datetime

@app.route('/')
def home():
   return "hello world!"

@app.route('/hora')
def hora():
   return f"{datetime.now()}"

@app.route('/soma')
def soma():
   num1 = request.form['num1']
   num2 = request.form['num2']
   soma = int(num1 + num2)
   return f"{soma}"

