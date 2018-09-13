import pymongo

from connection import Connection

class UserData:
    def create_user(self, user):
        db = Connection.openConection()
        db.usuarios.InsertOne(user)

    def find_by_username(self, username):
        db = Connection.openConection()
        return db.usuarios.find_one({"username": username})

    def find_by_prop(self, key, value):
        db = Connection.openConection()
        return db.usuarios.find({key: value})
   