
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="tourapp",
    password="Tour@1234",
    database="tourism"
)
cursor = db.cursor(dictionary=True)
@app.route("/")
def home():
    return render_template("signup.html")

# @app.route("/signup")
# def home():
#     return "Hello, Flask on Windows!"

if __name__ == "__main__":
    app.run(debug=True)


