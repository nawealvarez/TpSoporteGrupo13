from datos.usuarios import UserData
from werkzeug.security import check_password_hash, generate_password_hash

from entidades.objects import Usuario

class UserLogic():

    @staticmethod
    def insert_one(user):
        user.password = generate_password_hash(user.password)
        UserData.create_user(user)

    @staticmethod
    def find_by_username(username):
        user = UserData.find_by_username(username)
        return Usuario(user["_id"], user["username"], user["email"], user["password"])
        
    @staticmethod
    def check_password(password, username):
        pwhash = generate_password_hash(password)        
        return UserData.check_password(password, pwhash)

