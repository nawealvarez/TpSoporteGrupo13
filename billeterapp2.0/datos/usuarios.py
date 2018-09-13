from pymongo import InsertOne

from connection import Connection

class Usuario(object):
    c = Connection()
    db = c.connect()

    @classmethod
    def create_user(self, user):
        self.db.usuarios.InsertOne(user)

    @classmethod
    def find_by_username(self, username):
        return self.db.usuarios.find_one({"username": username})

    @classmethod
    def delete_user_by_username(self, username):
        self.db.usuarios.delete_one({"username": username})

    @classmethod
    def find_by_prop(self, key, value):
        return self.db.usuarios.find({key: value})
   