from connection import Connection

class Registro(object):
    c = Connection()
    db = c.connect()

    def altaGasIng(self, gasto_ingreso): 
        self.Aversiahorradb.gastos.insert_one(gasto_ingreso)
        # return gasto_ingreso
        # db.close()
    
    def devRegistros(self, id_usuario):
        # Esta runcion recibe el id del usuario y verifica en que registros de gastos/ingresos se encuentra 
        # y los devuelve
        for reg_a_devolver in self.Aversiahorradb.gastos.find({"id_usuario": id_usuario}):
            return reg_a_devolver
