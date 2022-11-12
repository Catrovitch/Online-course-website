from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


def login(username, password):
    sql = "SELECT id, password, admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
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

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)"
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":False})
        db.session.commit()
    except:
        return False
    return login(username, password)

def register_admin(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)"
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":True})
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
