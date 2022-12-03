from app import app
import users
import course_handler
import exercise_handler
import course_registration_handler
import statistics_handler

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
    
    return render_template("index.html", user = users.user_name(),
                         status = users.is_admin())

    
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
    
    if users.is_admin():
        student_records = users.student_records()
        courses_lst = course_handler.get_all_courses()
        return render_template("admin.html", users=student_records,
                                courses=courses_lst, user = users.user_name())
    else:
        return render_template("error.html", message="You are no admin")


@app.route("/admin/createcourse", methods=["POST"])
def create_course():

    if users.is_admin():
        course_name = request.form["course_name"]
        course_code = request.form["course_code"]
        course_description = request.form["course_description"]
        try:
            course_handler.create_course(course_name, course_code, course_description)
        except:
            pass
        return redirect("/admin")
    return redirect("/")


@app.route("/delete_course", methods=["POST"])
def delete_course():

    if users.is_admin():
        course_name = request.form["course_to_delete"]
        try:
            course_handler.delete_course(course_name)
            statistics_handler.delete_course(course_name)
        except:
            pass
        student_records = users.student_records()
        courses_lst = course_handler.get_all_courses()
        return render_template("admin.html", users=student_records,
                                courses=courses_lst, user = users.user_name())
      

@app.route("/courses", methods=["GET"])
def courses_page():
    courses_list = course_handler.get_all_courses()

    if users.user_id() == 0:
        return render_template("courses.html", courses = courses_list)

    return render_template("courses.html", courses = courses_list, user=users.user_name())


@app.route("/course/<int:course_id>", methods=["GET"])
def course_page(course_id):
    course = course_handler.get_course(course_id)
    exercises = exercise_handler.course_exercises(course_id)

    if users.user_id() == 0:
        return render_template("course.html", course=course, exercises=exercises)

    return render_template("course.html", course=course, exercises=exercises, user=users.user_name(), status = users.is_admin())


@app.route("/course/<int:course_id>/create_exercise/", methods=["POST"])
def create_exercise(course_id):

    question = request.form['question']
    option1 = request.form['option1']
    option2 = request.form['option2']
    option3 = request.form['option3']
    answer = request.form['radiobutton']

    exercise_handler.create_exercise(course_id, question, option1, option2, option3, answer)
    statistics_handler.add_exercise(course_id)

    return course_page(course_id)

@app.route("/course/<int:course_id>/edit_exercise/", methods=["POST"])
def update_exercise(course_id):

    exercise_nr = request.form['exercise_nr']
    question = request.form['question']
    option1 = request.form['option1']
    option2 = request.form['option2']
    option3 = request.form['option3']
    answer = request.form['radiobutton']

    exercise_handler.update_exercise(course_id, exercise_nr, question, option1, option2, option3, answer)

    return course_page(course_id)

@app.route("/course/<int:course_id>/delete_exercise/", methods=["POST"])
def delete_exercise(course_id):

    exercise_nr = request.form['exercise_to_delete']
    exercise_handler.delete_exercise(course_id, exercise_nr)
    statistics_handler.delete_exercise(course_id, exercise_nr)

    return course_page(course_id)


@app.route("/register_for/<int:course_id>/<int:user_id>/", methods=["POST"])
def register_for_course(course_id, user_id):
    
    if users.user_id() == 0:
        return courses_page()
    
    if not course_registration_handler.user_already_in_course(course_id, user_id):
        course_registration_handler.register_for_course(course_id, user_id)
        statistics_handler.initialize_user_at_course(user_id, course_id)

    return courses_page()

@app.route("/unregister/<int:course_id>/<int:user_id>/", methods=["POST"])
def unregister_from_course(course_id, user_id):
    
    if users.user_id() == 0:
        return courses_page()
    
    course_registration_handler.unregister_from_course(course_id, user_id)
    statistics_handler.user_unregisters_from_course(course_id, user_id)
    return courses_page()

@app.route("/user/<int:user_id>/", methods=["GET"])
def user(user_id):

    if user_id == users.user_id() or users.is_admin():
        course_progression = statistics_handler.progression(user_id)

        return render_template("user.html", courses=course_progression)

    return redirect("/")

    
@app.route("/course/<int:course_id>/<int:user_id>/check_exercises/", methods=["POST"])
def check_exercises(course_id, user_id):

    if users.user_id() == 0:
        return redirect("/")
    
    exercise_ids = exercise_handler.exercise_ids(course_id)
    submitted_answers = {}

    for number in exercise_ids:
        submitted_answers[number] = request.form[str(number)]

    checked_exercises = exercise_handler.check_correctness(course_id, submitted_answers)
    statistics_handler.submit_exercises(user_id, course_id, checked_exercises)

    return course_page(course_id)