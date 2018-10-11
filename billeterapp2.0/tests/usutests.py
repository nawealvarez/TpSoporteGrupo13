import unittest
from negocio.usuarios import UserLogic
from datos.usuarios import UserData
from entidades.objects import Usuario

class TestNegocio(unittest.TestCase):
    
    def test_find_by_username(self):
        # cargo un usuario
        usuario = {"username": "cosmefulanito", "email": "cosmef@gmail.com", "password": '12345', "password2": '12345'}
        user = Usuario(usuario["username"],
                       usuario["email"])
        user.password = usuario["password"]
        UserLogic.insert_one(user)
        
        #busco el usuario cargado por el username
        encontrado = UserLogic.find_by_username(usuario["username"])
        return self.assertTrue(encontrado)


if __name__=='__main__':
    unittest.main()