import pymongo

from datos.connection import Connection

class UserData():
    @staticmethod
    def create_user(user):
        db = Connection.connect()
        db.usuarios.insert_one(user)

    @staticmethod
    def find_by_username(username):
        db = Connection.connect()
        return db.usuarios.find_one({"username": username})

    @staticmethod
    def delete_user_by_username(username):
        db = Connection.connect()
        db.usuarios.delete_one({"username": username})

    @staticmethod
    def find_by_prop(key, value):
        db = Connection.connect()
        return db.usuarios.find({key: value})
    
    @staticmethod
    def check_password(pwhash, username):
        db = Connection.connect()
        return True if db.usuarios.find_one({"username": username, "password": pwhash}) else False
   