from connection import Connection

class Manejobd(object):
    c = Connection()
    Aversiahorradb = c.connect()
   
    def altaGasIng(self, algo): 
        self.Aversiahorradb.gastos.insert_one(algo)
        # db.close()

    def altaUsuario(self, algo):
        self.Aversiahorradb.usuarios.insert_one(algo)