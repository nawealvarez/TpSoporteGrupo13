from flask_login import UserMixin

class Usuario(UserMixin):
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @property
    def _id(self):
        return self._id
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
