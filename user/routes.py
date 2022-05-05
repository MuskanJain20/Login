from flask import Flask,render_template
from app import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/index/',methods=["POST","GET"])
def index():
    return render_template("index.html")
@app.route('/food_chart/',methods=["POST","GET"])
def food_chart():
    return render_template("food_chart.html")
@app.route('/chatbot/',methods=["POST","GET"])
def chatbot():
    return render_template("chatbot.html")



@app.route('/user/login', methods=['POST'])
def login():
  return User().login()
app.run()