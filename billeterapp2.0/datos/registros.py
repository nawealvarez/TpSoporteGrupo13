import pymongo
import datetime
from datos.connection import Connection

class RegistroData():
    
    @staticmethod
    def create_registro(registro):
        db = Connection.connect()
        db.registros.insert_one(registro)

    @staticmethod
    def find_by_categoria(categoria):
        db = Connection.connect()
        return db.registros.find_one({"categoria": categoria})

    @staticmethod
    def find_by_prop(key, value):
        db = Connection.connect()
        return db.registros.find({key: value})
    
    @staticmethod
    def get_lasts_registers(userid, top):
        db = Connection.connect()
        return db.registros.find({"userid": userid}, sort=[("fecha", pymongo.DESCENDING)]).limit(top)

    @staticmethod
    def get_montos(userid):
        db = Connection.connect()
        return db.registros.find({"userid": userid}, {"valor": 1})
