from flask import Flask, render_template
from data import load_users
from authorization import role_required, department_required

app = Flask(__name__)


def get_user_by_username(username):
    users = load_users()
    for user in users:
        if user["username"] == username:
            return user
    return None


@app.route("/")
def home():
    users = load_users()
    return render_template("home.html", users=users)


@app.route("/student")
def student():
    current_user = get_user_by_username("student1")
    if not role_required(current_user, ["student"]):
        return render_template("access_denied.html")
    return render_template("student.html", user=current_user)


@app.route("/staff")
def staff():
    current_user = get_user_by_username("staff1")
    if not role_required(current_user, ["staff", "admin"]):
        return render_template("access_denied.html")
    if not department_required(current_user, ["registrar"]):
        return render_template("access_denied.html")
    return render_template("staff.html", user=current_user)


@app.route("/admin")
def admin():
    current_user = get_user_by_username("admin1")
    if not role_required(current_user, ["admin"]):
        return render_template("access_denied.html")
    if not department_required(current_user, ["it-security"]):
        return render_template("access_denied.html")
    return render_template("admin.html", user=current_user)


if __name__ == "__main__":
    app.run(debug=True)
