from flask import Flask, render_template
from data import load_users

app = Flask(__name__)


@app.route("/")
def home():
    users = load_users()
    return render_template("home.html", users=users)


@app.route("/student")
def student():
    return render_template("student.html")


@app.route("/staff")
def staff():
    return render_template("staff.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)
