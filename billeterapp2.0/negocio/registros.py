from datos.registros import RegistroData

class RegistroLogic():

    def insert_one(self, registro):
        r = RegistroData()
        r.create_registro(registro)

    def find_by_categoria(self, categoria):
        r = RegistroData()
        return r.find_by_categoria(categoria)

   # def sort_by_date(self):
   #     r = RegistroData()
   #     r.sort_registros()