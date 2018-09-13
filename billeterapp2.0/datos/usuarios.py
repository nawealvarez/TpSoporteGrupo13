from pymongo import InsertOne

from datos.connection import Connection

class Usuario(object):

    @classmethod
    def create_user(self, user):
        c = Connection()
        db = c.connect()
        db.usuarios.InsertOne(user)

    @classmethod
    def find_by_username(self, username):
        c = Connection()
        db = c.connect()
        return db.usuarios.find_one({"username": username})

    @classmethod
    def find_by_prop(self, key, value):
        c = Connection()
        db = c.connect()
        return db.usuarios.find({key: value})
   