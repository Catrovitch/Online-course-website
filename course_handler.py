from db import db


class UserInputError(Exception):
    pass

def get_all_course_names():

    result = db.session.execute("SELECT name FROM Courses").fetchall()

    return result

def create_course(course_name, course_code, description):

    if not course_name or not course_code or not description:
        raise UserInputError("Fill in all information to create course")

    sql = "INSERT INTO courses (name, course_id, description) values (:name, :course_id, :description)"
    db.session.execute(sql, {"name":course_name, "course_id":course_code, "description":description})
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

def course_exercises(course_id):
    
    sql = "SELECT exercise_nr, question, option1, option2, option3 FROM Exercises WHERE course_id =:course_id"
    exercises = db.session.execute(sql, {"course_id":course_id}).fetchall()
    
    return exercises

def create_exercise(course_id, question, option1, option2, option3, answer):
   
    if not course_id or not question or not option1 or not option2 or not option3 or not answer:
        raise UserInputError("Fill in all information to create exercise")

    exercise_nr = exercise_number(course_id)
    sql = "INSERT INTO Exercises (course_id, exercise_nr, question, option1, option2, option3, answer) values (:course_id, :exercise_nr, :question, :option1, :option2, :option3, :answer)"
    db.session.execute(sql, {"course_id":course_id, "exercise_nr":exercise_nr, "question":question, "option1":option1, "option2":option2, "option3":option3, "answer":answer})
    db.session.commit()

def exercise_number(course_id):

    sql = "SELECT MAX(exercise_nr) FROM Exercises WHERE course_id = :course_id"
    result = db.session.execute(sql, {"course_id":course_id}).fetchone()[0]
    exercise_nr = int(result) +1

    return exercise_nr

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