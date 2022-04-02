from inspect import Parameter
from sqlite3 import paramstyle
import string
from time import timezone
from datetime import date

# module
class Users:
    def __init__(self):
        self.name = ""
        self.gmail = ""
        self.phone = ""
        self.nation = ""
        self.slogan = ""
        self.gender = ""
        self.address = ""
        self.language = ""
        self.dateofbirth = date.today()
        self.twitter = ""
        self.linkedin = ""
        self.facebook = ""
        self.github = ""
        

    # get data user from request.form   
    def getdatafromrequest(data):   
        user = Users()
        user.name = data["name"]
        user.gmail = data["gmail"]
        user.phone = data["phone"]
        user.nation = data["nation"]
        user.slogan = data["slogan"]
        user.gender = data["gender"]
        user.address = data["address"]
        user.language = data["language"]
        user.dateofbirth = data["dateofbirth"]
        user.twitter = data["twitter"]
        user.linkedin = data["linkedin"]
        user.facebook = data["facebook"]
        user.github = data["github"]
        return user

