from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
import re


class UserInputError(Exception):
    pass

def login(username, password):

    user = get_user_from_users(username)

    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]


def user_name():
    
    id = user_id()

    sql = f"SELECT username FROM users WHERE id = {id}"

    return db.session.execute(sql).fetchone()[0]

def is_admin():
    
    id = user_id()

    sql = f"SELECT admin FROM users WHERE id = {id}"

    if db.session.execute(sql).fetchone()[0]:
        return True
    else:
        return False
    
def register_user(username, password, password_confirmation):

    if not username or not password:
        raise UserInputError("Username and password are required")

    if validate_registration(username, password, password_confirmation):
        register_user_in_db(username, password)
        return True
    
    return False

def register_admin(username, password, password_confirmation):

    if not username or not password:
        raise UserInputError("Username and password are required")

    if validate_registration(username, password, password_confirmation):    
        register_admin_in_db(username, password)
        return True
    
    return False

def register_user_in_db(username, password):
    
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)"
    db.session.execute(sql, {"username":username, "password":password_hash, "admin":False})
    db.session.commit()

    login(username, password)

def register_admin_in_db(username, password):
    
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)"
    db.session.execute(sql, {"username":username, "password":password_hash, "admin":True})
    db.session.commit()

    login(username, password)

def student_records():

    result = db.session.execute("SELECT username FROM Users WHERE ADMIN IS FALSE").fetchall()
    
    studentrecords = [item[0] for item in result]

    return studentrecords

def user_id():
    # Checks if and which user is logged in
    return session.get("user_id",0)

def username_exists(username):

    sql = "SELECT username FROM Users WHERE username =:username"
    
    usernames = db.session.execute(sql, {"username":username}).fetchall()
    username_list = [item[0] for item in usernames]

    if username in username_list:
        return True
        
    return False

def get_user_from_users(username):

    sql = "SELECT id, password, admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    return user

def validate_username(username):

    if username_exists(username):
        raise UserInputError(f"User with username {username} exists already")
        
    if not re.match('^[a-z]+$', username, flags=0):
        raise UserInputError(f"Username needs to contain only letters a-z")
            
    if len(username) < 3:
        raise UserInputError(f"Username is too short")

    return True

def validate_password(password):

    if len(password) < 8:
        raise UserInputError(f"Password is too short")
            
    if not re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password, flags=0):
        raise UserInputError("Password needs to contain numbers")

    return True

def validate_registration(username, password1, password2):

    if password1 != password2:
        raise UserInputError("Passwords must match")

    validate_username(username)

    validate_password(password1)

    return True


if __name__=="__main__":
    
    studentrecords = student_records()