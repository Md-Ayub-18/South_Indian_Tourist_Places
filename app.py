from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="user"
)
cursor = db.cursor(dictionary=True)

@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def doSignUp():
    fname = request.form["first_name"]
    
    lname = request.form["last_name"]
    email = request.form["email"]
    phone = request.form["phone"]
    gender = request.form["gender"]
    birth_year = request.form["birth_year"]
    # password = "text"

    cursor.execute("INSERT INTO user (first_name, last_name, phone, email, gender, birth_year,password) VALUES (%s, %s, %s, %s, %s, %s)",
                   (fname, lname, phone, email, gender, birth_year))
    db.commit()

    return "Hello, Flask on Windows!"

if __name__ == "__main__":
    app.run(debug=True)
