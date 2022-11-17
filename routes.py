from app import app
import users
import course_handler

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    flash
)


@app.route("/")
def index():
    if users.user_id() == 0:
        return render_template("index.html")
    
    return render_template("index.html", user = users.user_name(), status = users.is_admin())

    
@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():

    username = request.form["username"]
    password = request.form["password"]
    
    if users.login(username, password):
        return redirect("/")
    else:
        return render_template("index.html")

@app.route("/courses", methods=["GET", "POST"])
def course_handlerr():
    if request.method == "GET":
        return render_template("courses.html")
    if request.method == "POST":
        return render_template("courses.html")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def handle_register():

    username = request.form["username"]
    password = request.form["password1"]
    password_confirmation = request.form["password2"]

    try:
        users.register_user(username, password, password_confirmation)
        return redirect("/")        
    
    except Exception as error:
        flash(str(error))
        return redirect("/register")

@app.route("/register_admin", methods=["POST"])
def handle_register_admin():

    username = request.form["username"]
    password = request.form["password"]
    password_confirmation = request.form["password_confirmation"]

    try:
        users.register_admin(username, password, password_confirmation)
        return redirect("/")       
    
    except Exception as error:
        flash(str(error))
        return redirect("/register")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    allow = False
    if users.is_admin():
        allow = True
    if allow:

        courses_lst = course_handler.get_all_courses()
        return render_template("admin.html", courses=courses_lst, user = users.user_name())
    else:
        return render_template("error.html", message="You are no admin")


@app.route("/admin/createcourse", methods=["Post"])
def create_course():

    if users.is_admin():
        course_name = request.form["course_name"]
        course_id = request.form["course_id"]
        course_description = request.form["course_description"]

        course_handler.create_course(course_name, course_id, course_description)
        return redirect("/admin")

    return redirect("/")