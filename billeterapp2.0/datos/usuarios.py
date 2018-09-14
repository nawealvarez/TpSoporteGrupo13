import pymongo

from datos.connection import Connection

class UserData():
    def create_user(self, user):
        c = Connection()
        db = c.connect()
        db.usuarios.InsertOne(user)

    def find_by_username(self, username):
        c = Connection()
        db = c.connect()
        return db.usuarios.find_one({"username": username})

    def delete_user_by_username(self, username):
        c = Connection()
        db = c.connect()
        db.usuarios.delete_one({"username": username})

    def find_by_prop(self, key, value):
        c = Connection()
        db = c.connect()
        return db.usuarios.find({key: value})
   