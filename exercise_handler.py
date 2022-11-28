from db import db
import course_handler


class UserInputError(Exception):
    pass

def course_exercises(course_id):
    
    sql = "SELECT exercise_nr, question, option1, option2, option3 FROM Exercises WHERE course_id =:course_id ORDER BY exercise_nr ASC"
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

    if result == None:
        return 1

    exercise_nr = int(result) +1

    return exercise_nr

def update_exercise(course_id, exercise_nr, question, option1, option2, option3, answer):

    if not exercise_nr:
        raise UserInputError("Exercise number is mandatory")

    id = get_id(course_id, exercise_nr)

    if not question:
        question = get_question(id)
    
    if not option1:
        option1 = get_option1(id)

    if not option2:
        option2 = get_option2(id)        
    
    if not option3:
        option3 = get_option3(id)
    
    if not answer:
        answer = get_answer(id)

    sql = "UPDATE Exercises SET question =:question, option1 =:option1, option2 =:option2, option3 =:option3, answer =:answer WHERE course_id =:course_id AND exercise_nr =:exercise_nr"
    db.session.execute(sql, {"question":question, "option1":option1, "option2":option2, "option3":option3, "answer":answer, "course_id":course_id, "exercise_nr":exercise_nr})
    db.session.commit()

def delete_exercise(course_id, exercise_nr):

    course_id = str(course_id)
    sql = "DELETE FROM Exercises WHERE course_id =:course_id AND exercise_nr =:exercise_nr"
    db.session.execute(sql, {"course_id":course_id, "exercise_nr":exercise_nr})
    db.session.commit()

    update_exercise_numbers(exercise_nr)

def update_exercise_numbers(exercise_nr):

    sql = "UPDATE Exercises SET exercise_nr = exercise_nr -1 WHERE exercise_nr >=:exercise_nr"
    db.session.execute(sql, {"exercise_nr":exercise_nr})
    db.session.commit()

def get_answer(id):

    sql = "SELECT answer FROM Exercises WHERE id=:id"
    answer = db.session.execute(sql, {"id":id}).fetchone()[0]

    return answer

def get_option1(id):

    sql = "SELECT option1 FROM Exercises WHERE id=:id"
    option1 = db.session.execute(sql, {"id":id}).fetchone()[0]

    return option1

def get_option2(id):

    sql = "SELECT option1 FROM Exercises WHERE id=:id"
    option2 = db.session.execute(sql, {"id":id}).fetchone()[0]

    return option2

def get_option3(id):

    sql = "SELECT option1 FROM Exercises WHERE id=:id"
    option3 = db.session.execute(sql, {"id":id}).fetchone()[0]

    return option3

def get_question(id):

    sql = "SELECT question FROM Exercises WHERE id=:id"
    question = db.session.execute(sql, {"id":id}).fetchone()[0]

    return question

def get_id(course_id, exercise_nr):

    sql = "SELECT id FROM Exercises WHERE course_id =:course_id AND exercise_nr =:exercise_nr"
    id = db.session.execute(sql, {"course_id":course_id, "exercise_nr":exercise_nr}).fetchone()[0]

    return id