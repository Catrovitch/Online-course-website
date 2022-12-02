from db import db


class UserInputError(Exception):
    pass


def register_for_course(course_id, user_id):

    if not user_already_in_course(course_id, user_id):
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