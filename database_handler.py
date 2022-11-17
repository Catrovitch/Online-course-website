from db import db
from werkzeug.security import check_password_hash, generate_password_hash



class DatabaseHandler():

    def __init__(self, db=db):

        self.db = db

    def get_all_course_names(self):

        result = db.session.execute("SELECT name FROM courses").fetchall()

        return result

    def create_course(self, course_name, course_id, description):

        sql = "INSERT INTO courses (name, course_id, description) values (:name, :course_id, :description)"
        db.session.execute(sql, {"name":course_name, "course_id":course_id, "description":description})
        db.commit()


db_handler = DatabaseHandler(db)


