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
            if m["tipo"] == "gasto":
                count = count - float(format(m["valor"], ".2f"))
            elif m["tipo"] == "ingreso":
                count = count + float(format(m["valor"], ".2f"))
        return count

    @staticmethod
    def get_tipos(userid):
        cur = RegistroData.get_registros(userid)
        cat = {}
        for i in cur:
            a = i['tipo']
            if i['tipo'] in list(cat):
                cat[a] = cat[a] + i['valor']
            else:
                cat[a] = i['valor']
        print(cat)
        return cat

    @staticmethod
    def get_categorias(userid, tipo):
        cur = RegistroData.get_categorias(userid, tipo)
        cat = {}
        for i in cur:
            a = i['categoria']
            if i['categoria'] in list(cat):
                cat[a] = cat[a] + i['valor']
            else:
                cat[a] = i['valor']
        print(cat)
        return cat


   # def sort_by_date(self):
   #     r = RegistroData()
   #     r.sort_registros()
