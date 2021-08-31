from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello From Azure Web App - Version 2.0</h1>"