from datos.usuarios import UserData
from werkzeug.security import check_password_hash, generate_password_hash

class UserLogic():

    def insert_one(self, user):
        user["password"] = generate_password_hash(user["password"])
        u = UserData()
        u.create_user(user)

    def find_by_username(self, username):
        u = UserData()
        return u.find_by_username(username)

    def check_password(self, password, username):
        u = UserData()
        pwhash = generate_password_hash(password)        
        return u.check_password(password, pwhash)

