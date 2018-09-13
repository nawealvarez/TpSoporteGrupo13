import pymongo
from datos.connection import Conn
from connection import Connection

class UserData:
    def create_user(self, user):
        c = Conn()
        db = c.openConection()
        db.usuarios.insert_one(user)

    def find_by_username(self, username):
        c = Conn()
        db.openConection()
        return db.usuarios.find_one({"username": username})

    @classmethod
    def delete_user_by_username(self, username):
        self.db.usuarios.delete_one({"username": username})
        c = Conn()
        db = c.openConection()
        return db.usuarios.find_one({"username": username})

    def find_by_prop(self, key, value):
        return self.db.usuarios.find({key: value})
   
        c = Conn()
        db = c.openConection()
        return db.usuarios.find({key: value})



