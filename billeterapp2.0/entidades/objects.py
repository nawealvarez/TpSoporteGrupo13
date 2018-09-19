from flask_login import UserMixin
from enum import Enum


class Usuario(UserMixin, Enum):    
    def __init__(self, username, email,  _id = None):
        super.__init__()
        self._id = _id
        self.username = username
        self.email = email

    def get_id(self):
        return self._id
