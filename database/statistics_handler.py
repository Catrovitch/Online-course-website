from database.db import db

import database.course_handler as course_handler
import database.exercise_handler as exercise_handler
import database.course_registration_handler as course_registration_handler

class UserInputError(Exception):
    pass

def initialize_user_at_course(user_id, course_id):
    
    exercise_ids = exercise_handler.exercise_ids(course_id)

    for exercise_id in exercise_ids:
        sql = "INSERT INTO Statistics (user_id, course_id, exercise_id, completed) values (:user_id, :course_id, :exercise_id, :completed)"
        db.session.execute(sql, {"user_id":user_id, "course_id":course_id, "exercise_id":exercise_id, "completed":False})
    
    db.session.commit()

def add_exercise(course_id):

    user_list = course_registration_handler.user_courses(course_id)
    exercise_id = exercise_handler.max_exercise_id(course_id)

    for user_id in user_list:
        sql = "INSERT INTO Statistics (user_id, course_id, exercise_id, completed) values (:user_id, :course_id, :exercise_id, :completed)"
        db.session.execute(sql, {"user_id":user_id, "course_id":course_id, "exercise_id":exercise_id, "completed":False})

    db.session.commit()

def delete_course(course_name):

    course_id = get_course_id(course_name)
    
    sql = "DELETE FROM Statistics WHERE course_id =:course_id"
    db.session.execute(sql, {"course_id":course_id})
    db.session.commit()

    return True

def get_course_id(course_name):

    sql = "SELECT id from Courses WHERE name =:course_name"
    result = db.session.execute(sql, {"course_name":course_name}).fetchone()[0]

    return result


def delete_exercise(course_id, exercise_id):

    delete_exercise_from_course(course_id, exercise_id)
    update_exercise_numbers_after_deletion(course_id, exercise_id)

def delete_exercise_from_course(course_id, exercise_id):

    sql = "DELETE FROM Statistics WHERE course_id =:course_id AND exercise_id =:exercise_id"
    db.session.execute(sql, {"course_id":course_id, "exercise_id":exercise_id})
    db.session.commit()

def update_exercise_numbers_after_deletion(course_id, exercise_id):

    sql = "UPDATE Statistics SET exercise_id = exercise_id -1 WHERE course_id =:course_id AND exercise_id >=:exercise_id"
    db.session.execute(sql, {"course_id":course_id, "exercise_id":exercise_id})
    db.session.commit()

def complete_exercise(user_id, course_id, exercise_id):


    sql = "UPDATE Statistics SET completed =:completed WHERE user_id =:user_id AND course_id =:course_id AND exercise_id =:exercise_id"  
    db.session.execute(sql, {"completed":True, "user_id":user_id, "course_id":course_id, "exercise_id":exercise_id})
    db.session.commit()

def submit_exercises(user_id, course_id, correct_exercises):

    for exercise_id in correct_exercises:

        complete_exercise(user_id, course_id, exercise_id)

def progression(user_id):

    user_on_courses = courses_by_user(user_id) #SELECT course_id

    course_progressions = []

    for course_id in user_on_courses:
        name = course_handler.course_name(course_id)
        description = course_handler.course_description(course_id)
        user_progression = progression_on_course(course_id, user_id)
        course_progressions.append((course_id, name, description, user_progression))

    return course_progressions


def courses_by_user(user_id):

    sql = "SELECT course_id FROM Course_registration WHERE user_id =:user_id"
    result = db.session.execute(sql, {"user_id":user_id}).fetchall()
    course_lst = [course[0] for course in result]

    return course_lst

def progression_on_course(course_id, user_id):

    exercises_total = number_of_exercises(course_id)
    exercises_done = completed_exercises(course_id, user_id)
    if exercises_total > 0:
        progression_of_user_on_course = exercises_done/exercises_total
    else:
        progression_of_user_on_course = "currently no exercises are available"
        return progression_of_user_on_course
    
    return (f"{int(progression_of_user_on_course)*100} %")

def number_of_exercises(course_id):

    sql = "SELECT COUNT(*) FROM Exercises WHERE course_id =:course_id"
    result = db.session.execute(sql, {"course_id":course_id}).fetchone()[0]

    return result


def completed_exercises(course_id, user_id):

    
    sql = "SELECT COUNT(*) FROM Statistics WHERE course_id =:course_id AND user_id =:user_id AND completed =:completed"
    result = db.session.execute(sql, {"course_id":course_id, "user_id":user_id, "completed":True}).fetchone()[0]
    
    return result


def user_unregisters_from_course(course_id, user_id):

    sql = "DELETE FROM Statistics WHERE user_id =:user_id AND course_id =:course_id"
    db.session.execute(sql, {"user_id":user_id, "course_id":course_id})
    db.session.commit()


