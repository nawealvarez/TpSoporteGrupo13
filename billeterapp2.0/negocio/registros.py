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
        l = list(RegistroData.get_lasts_registers(userid, top))
        return l

    @staticmethod
    def get_balance(userid):
        montos = list(RegistroData.get_montos(userid))
        count = 0
        for m in montos:
            count = count + float(format(m["valor"], ".2f"))
        return count
    
    @staticmethod
    def get_all_categories():
        cats = RegistroData.get_all_categories()
        if cats:
            dic = {}
            index = 0   
            for c in cats:
                dic[index] = c
                index+=1
        return dic
        