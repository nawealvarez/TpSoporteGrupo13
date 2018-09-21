from flask_login import UserMixin

# Cuando llama al init de super lo rompe
# Que la clase herede de Enum tambien lo rompe

class Usuario(UserMixin):
    def __init__(self, username, email,  _id = None):
        #super.__init__()

        self._id = _id
        self.username = username
        self.email = email

    def get_id(self):
        return self._id
