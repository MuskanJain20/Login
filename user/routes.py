from flask import Flask, render_template, redirect, url_for, request, session, Response
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


@app.route('/squats', methods=["POST", "GET"])
def squats():
    count = 0
    calories = 0
    from squats import squats
    if request.method == "POST":
        n = request.form.get('co')
        count, calories = squats(int(n))
        # print(n)
    return render_template('squats.html', count=count, calories=calories)


# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/pushup', methods=["POST", "GET"])
def pushups():
    count = 0
    calories = 0
    if request.method == "POST":
        from push_up import pushup
        print("started")
        n = request.form.get('co')
        # print(n)
        count, calories = pushup(int(n))

    return render_template('pushup.html', count=count, calories=calories)


@app.route('/pullup', methods=["POST", "GET"])
def pullup():
    count = 0
    calories = 0
    if request.method == "POST":
        from pull_up import pullup
        print("started")
        n = request.form.get('co')
        # print(n)
        count, calories = pullup(int(n))

    return render_template('pullup.html', count=count, calories=calories)


@app.route('/biceps', methods=["POST", "GET"])
def biceps():
    count = 0
    calories = 0
    if request.method == "POST":
        from weight_lifting import biceps
        print("started")
        n = request.form.get('co')
        # print(n)
        count, calories = biceps(int(n))

    return render_template('weight_lifting.html', count=count, calories=calories)


@app.route('/crunches', methods=["POST", "GET"])
def crunches():
    count = 0
    calories = 0
    if request.method == "POST":
        from crunches import crunches
        print("started")
        n = request.form.get('co')
        # print(n)
        count, calories = crunches(int(n))

    return render_template('crunches.html', count=count, calories=calories)


@app.route('/count', methods=["POST", "GET"])
def count():
    return render_template('count.html')


@app.route('/user/login', methods=['POST'])
def login():
  return User().login()
app.run()