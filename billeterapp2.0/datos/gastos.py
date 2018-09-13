from manejodedatos import Manejobd
import time

class DatosGastos():

    def inGastoIngreso(self):
        gasing = {}
        listo, ready = False, False
        op, opc = "w", "w"
        fecha = "Fecha"
        v_fecha =  time.strftime("%c")
        while not ready:
            tip = input("1 - Ingresar un gasto  2 - Ingresar ingreso" )
            if tip == 1:
                cat = "Categoria"
                cat_nom = input("ingrese una categoria ")
                gasing[cat] = cat_nom

                while not listo:  
                    op = input("desea ingresar otra propiedad? Y/N: ").lower()
                    if op == "y":
                        prop = input("Ingrese el nombre de la propiedad")
                        val = input("Ingrese el valor de la propiedad")
                        gasing[prop] = val
                        op == input("Ingresar otra propiedad? Y/N").lower()
                    elif op == "n":
                        listo = True
            else:
                cat = input("Ingrese una categoria ")
                val = input("ingrese el valor: ")
                gasing[prop] = val   
                while not listo:  
                    op = input("desea ingresar otra propiedad? Y/N: ").lower()
                    if op == "y":
                        prop = input("Ingrese el nombre de la propiedad")
                        val = input("Ingrese el valor de la propiedad")
                        gasing[prop] = val
                        op == input("Ingresar otra propiedad? Y/N").lower()
                    elif op == "n":
                        listo = True

            gasing[fecha] = v_fecha                    
            a = Manejobd()
            a.altaGasIng(gasing)

            while opc!= "y" and opc != "n": 
                opc = input("ingresar otro gasto o ingreso Y/N").lower
                if opc == "n":
                    ready = False 