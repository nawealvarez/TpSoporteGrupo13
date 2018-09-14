from datos.usuarios import UserData

class UserLogic():

    def insert_one(self, user):
        u = UserData()
        u.create_user(user)

    def find_by_username(self, username):
        u = UserData()
        return u.find_by_username(username)

# c = UserLogic()
# m = c.find_by_username("marche")
# print(m)
