from manejodedatos import Manejobd

class DatosUsuario(object):
    c = Manejobd()
    usu = {}
    id = "_id"
    id_valor =  c.Aversiahorradb.usuarios.find().count()+1
    usu[id] = id_valor
    usuario = "Usuario"
    val_usu = input("Ingrese un nombre de Usuario: ")
    usu[usuario]=val_usu
    passw = "Password"
    val_pass = input("Ingrese una Contraseña: ")
    usu[passw]=val_pass
    nombre = "Nombre"
    val_nom = input("Ingrese su Nombre: ")
    usu[nombre]=val_nom
    apellido = "Apellido"
    val_apel = input("Ingrese su Apellido: ")
    usu[apellido]=val_apel
    c.altaUsuario(usu)

   