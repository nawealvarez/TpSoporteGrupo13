import pymongo
import datetime
from datos.connection import Connection

class RegistroData():
    
    @staticmethod
    def create_registro(self, registro):
        db = Connection.connect()
        fecha = datetime.datetime.now
        registro["fecha"] = fecha
        db.registros.insert_one(registro)

    @staticmethod
    def find_by_categoria(self, categoria):
        db = Connection.connect()
        return db.registros.find_one({"categoria": categoria})

    @staticmethod
    def find_by_prop(self, key, value):
        db = Connection.connect()
        return db.registros.find({key: value})
    

