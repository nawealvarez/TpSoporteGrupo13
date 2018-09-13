from connection import Connection

class Manejobd(object):
    c = Connection()
    Aversiahorradb = c.connect()

    def altaUsuario(self, usuario):
        self.Aversiahorradb.usuarios.insert_one(usuario)
        # return usuario

    def buscarUsuario(self, usuario):
        for usu_a_devolver in self.Aversiahorradb.usuarios.find({"Usuario": usuario}):
            return usu_a_devolver

    def darBajaUsu(self, usuario):
        for usu_abajar in self.Aversiahorradb.usuarios.delete_one({"Usuario": usuario}):
            return ("Usuario Eliminado")

    def altaGasIng(self, gasto_ingreso): 
        self.Aversiahorradb.gastos.insert_one(gasto_ingreso)
        # return gasto_ingreso
        # db.close()
    
    def devRegistros(self, id_usuario):
        # Esta runcion recibe el id del usuario y verifica en que registros de gastos/ingresos se encuentra 
        # y los devuelve
        for reg_a_devolver in self.Aversiahorradb.gastos.find({"id_usuario": id_usuario}):
            return reg_a_devolver
