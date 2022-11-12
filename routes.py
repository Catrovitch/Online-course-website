from app import app
from flask import render_template, request, redirect
import users

@app.route("/")
def index():
    if users.user_id() == 0:
        return render_template("index.html")
    
    return render_template("index.html", user = users.user_name())

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("/index.html")

@app.route("/courses", methods=["GET", "POST"])
def courses():
    if request.method == "GET":
        return render_template("courses.html")
    if request.method == "POST":
        return render_template("courses.html")
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")

@app.route("/register_admin", methods=["GET", "POST"])
def register_admin():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")
        if users.register_admin(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    allow = False
    if users.is_admin():
        allow = True
    if allow:
        return render_template("admin.html")
    else:
        return render_template("error.html", message="You are no admin")