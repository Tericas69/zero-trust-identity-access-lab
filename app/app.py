from flask import Flask, render_template
from data import load_users

app = Flask(__name__)

@app.route("/")
def home():
    users = load_users()
    return render_template("home.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
