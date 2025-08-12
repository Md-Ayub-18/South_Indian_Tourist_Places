from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database connection
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
    # Get form data safely
    fname = request.form.get("first_name")
    lname = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    gender = request.form.get("gender")
    birth_year = request.form.get("birth_year")
    password = "test"  # In production, you should hash real passwords

    # Validate required fields
    if not all([fname, lname, email, phone, gender, birth_year]):
        return "Missing required fields", 400

    try:
        cursor.execute("""
            INSERT INTO users 
            (first_name, last_name, phone, email, gender, birth_year, password) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, 
            (fname, lname, phone, email, gender, birth_year, password))
        db.commit()
        return "Registration successful!"
    except Exception as e:
        db.rollback()
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)