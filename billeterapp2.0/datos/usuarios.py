import pymongo

from datos.connection import Connection

class UserData():
    def create_user(self, user):
        db = Connection.connect()
        db.usuarios.insert_one(user)

    def find_by_username(self, username):
        db = Connection.connect()
        return db.usuarios.find_one({"username": username})

    def delete_user_by_username(self, username):
        db = Connection.connect()
        db.usuarios.delete_one({"username": username})

    def find_by_prop(self, key, value):
        db = Connection.connect()
        return db.usuarios.find({key: value})
    
    def check_password(self, pwhash, username):
        db = Connection.connect()
        u = any(db.usuarios.find_one({"username": username, "password": pwhash}))
        return u
   