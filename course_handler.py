from db import db

def get_all_course_names():

    result = db.session.execute("SELECT name FROM Courses").fetchall()

    return result

def create_course(course_name, course_id, description):

    sql = "INSERT INTO courses (name, course_id, description) values (:name, :course_id, :description)"
    db.session.execute(sql, {"name":course_name, "course_id":course_id, "description":description})
    db.session.commit()

def course_exercises(course_name):
    pass


def get_all_courses():

    result = db.session.execute("SELECT name, course_id, description FROM Courses").fetchall()

    return result