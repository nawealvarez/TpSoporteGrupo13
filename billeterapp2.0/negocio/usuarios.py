from datos.usuarios import UserData

class UserLogic():

    def insert_one(self, user):
        userdata = UserData()
        userdata.create_user(user)

    def find_by_username(self, username):
        userdata = UserData()
        return userdata.find_by_username(username)