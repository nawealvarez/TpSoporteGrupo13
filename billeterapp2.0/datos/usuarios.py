from connection import client, usuarios

class DatosUsuario(object):
    def alta(self, algo): 
        c = client
        db = c.connect()
        db.usuarios.insert_one(algo)
        # db.close()