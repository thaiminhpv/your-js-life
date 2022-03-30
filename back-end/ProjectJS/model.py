from email.policy import default
import string
from time import timezone
    

class Users:
    def __init__(self, first_name = "", last_name = "", email = "", nation = "", Language = "",address = "", age = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nation = nation
        self.Language = Language
        self.age = age
        self.address = address