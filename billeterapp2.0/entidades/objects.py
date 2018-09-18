from flask_login import UserMixin



class Usuario(UserMixin):    
    def __init__(self, username, email,  _id = None):
        self._id = _id
        self.username = username
        self.email = email

    def get_id(self):
        return self._id
