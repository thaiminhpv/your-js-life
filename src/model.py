from email.policy import default
from inspect import Parameter
from sqlite3 import paramstyle
import string
from time import timezone
from datetime import date

# module
class Users:
    def __init__(self, name="", email="", nation="", language="", address="", dateofbirth = date.today()):
        self.name = name
        self.email = email
        self.nation = nation
        self.language = language
        self.dateofbirth = dateofbirth
        self.address = address

    # get data user from request.form   
    def getdatafromrequest(data):   
        user = Users()
        user.name = data["firstname"]
        user.email = data["email"]
        user.nation = data["nation"]
        user.dateofbirth = data["dateofbirth"]
        user.language = data["selectLanguage"]
        user.address = data["address"]
        return user



