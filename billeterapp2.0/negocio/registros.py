from datos.registros import RegistroData

class RegistroLogic():

    @staticmethod
    def insert_one(registro):
        RegistroData.create_registro(registro)

    @staticmethod
    def find_by_categoria(categoria):
        return RegistroData.find_by_categoria(categoria)

    @staticmethod
    def get_lasts_registers(userid, top):
        col = list(RegistroData.get_lasts_registers(userid, top))
        return col
    


   # def sort_by_date(self):
   #     r = RegistroData()
   #     r.sort_registros()