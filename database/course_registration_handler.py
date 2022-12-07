from database.db import db

class UserInputError(Exception):
    pass


def register_for_course(course_id, user_id):

    sql = "INSERT INTO Course_registration (course_id, user_id) values (:course_id, :user_id)"
    db.session.execute(sql, {"course_id":course_id, "user_id":user_id})
    db.session.commit()

def unregister_from_course(course_id, user_id):

    sql = "DELETE FROM Course_registration WHERE course_id =:course_id AND user_id =:user_id"
    db.session.execute(sql, {"course_id":course_id, "user_id":user_id})
    db.session.commit()

def user_already_in_course(course_id, user_id):

    sql = "SELECT * FROM Course_registration WHERE course_id =:course_id AND user_id =:user_id"
    result = db.session.execute(sql, {"course_id":course_id, "user_id":user_id}).fetchall()

    if len(result) == 0:
        return False
    
    return True

def user_courses(user_id):

    sql = "SELECT course_id FROM Course_registration WHERE user_id =:user_id"
    result = db.session.execute(sql, {"user_id":user_id}).fetchall()

    course_list = [course[0] for course in result]

    return course_list

def get_users_on_course(course_id):

    sql = "SELECT user_id FROM Course_registration WHERE course_id =:course_id"
    result = db.session.execute(sql, {"course_id":course_id}).fetchall()

    if len(result) == 0:
        return False
    
    users_lst = [user[0] for user in result]

    return users_lst


