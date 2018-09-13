from connection import Connection

class Manejobd(object):
    def altaGasIng(self, algo) : 
        c = Connection()
        Aversiahorradb = c.connect()
        Aversiahorradb.gastos.insert_one(algo)
        # db.close()