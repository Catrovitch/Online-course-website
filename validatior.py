import users
import re

class UserInputError(Exception):
    pass

class Validator():

    def __init__(self):

        pass

    def __validate_username(self, username):

        if users.search_for_user_by_username(username):
            raise UserInputError(f"User with username {username} exists already")
        
        if not re.match('^[a-z]+$', username, flags=0):
            raise UserInputError(f"Username needs to contain only letters a-z")
            
        if len(username) < 3:
            raise UserInputError(f"Username is too short")

    def __validate_password(self, password):

        if len(password) < 8:
            raise UserInputError(f"Password is too short")
            
        if not re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password, flags=0):
            raise UserInputError("Password needs to contain numbers")

        return True


    def validate_registration(self, username, password1, password2):

        if password1 != password2:
            raise UserInputError("Passwords must match")

        self.__validate_username(username)

        self.__validate_password(password1)

        return True


validator = Validator()