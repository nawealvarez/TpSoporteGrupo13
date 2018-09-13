import pymongo

<<<<<<< HEAD
from connection import Connection

class Usuario(object):
    c = Connection()
    db = c.connect()

    @classmethod
    def create_user(self, user):
        self.db.usuarios.InsertOne(user)
=======
from datos.connection import Conn

class UserData:
    def create_user(self, user):
        c = Conn()
        db = c.openConection()
        db.usuarios.insert_one(user)
>>>>>>> 018f0899937ecc9b7e2479f70ec2a0b58f377f66

    def find_by_username(self, username):
<<<<<<< HEAD
        return self.db.usuarios.find_one({"username": username})

    @classmethod
    def delete_user_by_username(self, username):
        self.db.usuarios.delete_one({"username": username})
=======
        c = Conn()
        db = c.openConection()
        return db.usuarios.find_one({"username": username})
>>>>>>> 018f0899937ecc9b7e2479f70ec2a0b58f377f66

    def find_by_prop(self, key, value):
<<<<<<< HEAD
        return self.db.usuarios.find({key: value})
   
=======
        c = Conn()
        db = c.openConection()
        return db.usuarios.find({key: value})



>>>>>>> 018f0899937ecc9b7e2479f70ec2a0b58f377f66
