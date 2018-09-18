import pymongo
import datetime
from datos.connection import Connection

class RegistroData():
    def create_registro(self, registro):
        db = Connection.connect()
        fecha = datetime.datetime.now
        registro["fecha"] = fecha
        db.registros.insert_one(registro)

    def find_by_categoria(self, categoria):
        db = Connection.connect()
        return db.registros.find_one({"categoria": categoria})

    def find_by_prop(self, key, value):
        db = Connection.connect()
        return db.registros.find({key: value})
    

