from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from os import getenv


def launch_app():
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")

    return app

def database(admin_app):
    admin_app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    db = SQLAlchemy(admin_app)
    return db

def register_admin(username, password, db):

    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)"
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":True})
        db.session.commit()
        
    except:
        print(f"Failed to create admin account with username {username}")
        return False
    
    print(f"Admin {username} created")
    return True

if __name__=="__main__":
    admin_app = launch_app()
    db = database(admin_app)
    register_admin("Sauron", "onering", db)