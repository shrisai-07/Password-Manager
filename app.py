from flask import Flask, render_template, request, redirect, session
from database import create_tables, get_db_connection
from security import encrypt_password
import bcrypt

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    return "Password Manager Running Successfully!"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
            conn.commit()
        except:
            conn.close()
            return "Username already exists!"

        conn.close()
        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        conn.close()

        if user:
            stored_hash = user["password_hash"]

            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode()

            if bcrypt.checkpw(password.encode(), stored_hash):
                session["user_id"] = user["id"]
                return redirect("/dashboard")

        return "Invalid Credentials"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    passwords = conn.execute(
        "SELECT * FROM passwords WHERE user_id = ?",
        (session["user_id"],)
    ).fetchall()
    conn.close()

    return render_template("dashboard.html", passwords=passwords)

@app.route("/add", methods=["GET", "POST"])
def add_password():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        website = request.form["website"]
        email = request.form["email"]
        password = request.form["password"]

        encrypted = encrypt_password(password)

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO passwords (user_id, website, email, encrypted_password) VALUES (?, ?, ?, ?)",
            (session["user_id"], website, email, encrypted)
        )
        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template("add.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
