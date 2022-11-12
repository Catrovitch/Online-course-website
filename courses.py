from db import db
import users
from flask import session


def get_all_courses():
    sql = "SELECT * FROM Courses"
    result = db.session.execute().fetchall()
    return result

def register_to_course(user_id):

    
    try:
        sql = "INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)"
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":False})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    # Checks if and which user is logged in
    return session.get("user_id",0)

def is_admin():
    # Checks if user is admin
    id = user_id()

    sql = f"SELECT admin FROM users WHERE id = {id}"

    if db.session.execute(sql).fetchone()[0]:
        return True
    else:
        return False

def user_name():
    
    id = user_id()

    sql = f"SELECT username FROM users WHERE id = {id}"

    return db.session.execute(sql).fetchone()[0]
