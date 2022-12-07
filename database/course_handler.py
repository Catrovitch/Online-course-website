from database.db import db

class UserInputError(Exception):
    pass

def get_all_course_names():

    result = db.session.execute("SELECT name FROM Courses").fetchall()

    return result

def create_course(course_name, course_code, description):

    if not course_name or not course_code or not description:
        raise UserInputError("Fill in all information to create course")

    sql = "INSERT INTO courses (name, course_code, description) values (:name, :course_code, :description)"
    db.session.execute(sql, {"name":course_name, "course_code":course_code, "description":description})
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

def course_name(course_id):

    sql = "SELECT name FROM Courses WHERE id =:course_id"
    result = db.session.execute(sql, {"course_id":course_id}).fetchone()
    name = result[0]

    return name

def course_description(course_id):

    sql = "SELECT description FROM Courses WHERE id =:course_id"
    result = db.session.execute(sql, {"course_id":course_id}).fetchone()
    description = result[0]

    return description

def get_course(course_id):

    sql = "SELECT id, name, description FROM Courses WHERE id =:course_id"
    course = db.session.execute(sql, {"course_id":course_id}).fetchone()    

    return course

def get_all_courses():

    result = db.session.execute("SELECT id, name, course_code, description FROM Courses").fetchall()

    return result

def get_users_courses(user_courses):

    sql = f"SELECT * FROM Courses WHERE id = ANY(ARRAY{user_courses})"
    courses = db.session.execute(sql).fetchall()

    return courses