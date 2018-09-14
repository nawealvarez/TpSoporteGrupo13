import time

class DatosGastos():
    gasing = {}
    # c = Manejobd()
    listo = False
    op = "w"
    id = "_id"
    id_valor = 0 #  c.Aversiahorradb.gastos.find().count()+1
    gasing[id] = id_valor
    fecha = "Fecha"
    v_fecha =  time.strftime("%c")
    gasing[fecha] = v_fecha 
    tipo = "Tipo"
    tip = input("1 - Ingresar un gasto  2 - Ingresar ingreso: " )
    if tip == '1':
        val_tipo = "Gasto"
        gasing[tipo] = val_tipo
    elif tip == '2':
        val_tipo = "Ingreso"
        gasing[tipo] = val_tipo
            
    cat = "Categoria"
    cat_nom = input("ingrese una categoria: ")
    gasing[cat] = cat_nom
    valor = "Valor"
    nom_val = int(input("ingrese la cantidad: "))
    gasing[valor] = nom_val
    while not listo:  
        op = input("desea ingresar otra propiedad? Y/N: ").lower()
        if op == "y":
            prop = input("Ingrese el nombre de la propiedad: ")
            val = input("Ingrese el valor de la propiedad: ")
            gasing[prop] = val
        elif op == "n":
            listo = True
    
   # c.altaGasIng(gasing)
