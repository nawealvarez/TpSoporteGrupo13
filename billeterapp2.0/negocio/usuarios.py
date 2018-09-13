from datos.usuarios import Usuario as UserData

class User():

    @classmethod
    def insert_one(self, user):
        UserData.create_user(user)

    @classmethod
    def find_by_username(self, username):
        return UserData.find_by_username(username)
