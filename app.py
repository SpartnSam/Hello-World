from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "password"

@app.route("/hello")
def index():
    flash("What is your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet(): 
    flash("Hey " + str(request.form['name_input']) + ", glad to see you here!")
    return render_template("index.html")