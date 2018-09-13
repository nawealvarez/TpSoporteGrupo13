import pymongo

from datos.connection import Conn

class UserData:
    def create_user(self, user):
        c = Conn()
        db = c.openConection()
        db.usuarios.insert_one(user)

    def find_by_username(self, username):
        c = Conn()
        db = c.openConection()
        return db.usuarios.find_one({"username": username})

    def find_by_prop(self, key, value):
        c = Conn()
        db = c.openConection()
        return db.usuarios.find({key: value})



