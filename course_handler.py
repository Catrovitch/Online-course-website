from db import db


class UserInputError(Exception):
    pass

def get_all_course_names():

    result = db.session.execute("SELECT name FROM Courses").fetchall()

    return result

def create_course(course_name, course_id, description):

    if not course_name or not course_id or not description:
        raise UserInputError("Fill in all information to create course")

    sql = "INSERT INTO courses (name, course_id, description) values (:name, :course_id, :description)"
    db.session.execute(sql, {"name":course_name, "course_id":course_id, "description":description})
    db.session.commit()

def delete_course(course_name):

    all_courses = [item[0] for item in get_all_courses()]

    if course_name not in all_courses:
        raise UserInputError("No course with such name")
    if not course_name:
        raise UserInputError("No course_name given")

    sql = "DELETE FROM Courses WHERE name =:name"
    db.session.execute(sql, {"name":course_name})
    db.session.commit() 

    return True

def course_exercises(course_name):
    pass


def get_all_courses():

    result = db.session.execute("SELECT name, course_id, description FROM Courses").fetchall()

    return result