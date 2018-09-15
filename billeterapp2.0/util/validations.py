from datos.usuarios import UserData

class UserValidations():
    @classmethod
    def is_email_valid(self, email_field):
        userdata = UserData()
        return any(userdata.find_by_prop("email", email_field))

    @classmethod
    def is_username_valid(self, username_field):
        userdata = UserData()
        return any(userdata.find_by_prop("username", username_field))
