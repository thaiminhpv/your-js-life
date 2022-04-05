from inspect import Parameter
from math import gamma
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

        # get data user from request.form

    def getdatafromdb(data):
        user = Users()
        user.name = data[1]
        user.gmail = data[2]
        user.phone = data[3]
        user.address = data[4]
        user.nation = data[5]
        user.slogan = data[6]
        user.gender = data[7]
        user.language = data[8]
        user.dateofbirth = data[9]
        user.twitter = data[10]
        user.linkedin = data[11]
        user.facebook = data[12]
        user.github = data[13]
        return user.github


user = Users()
user.name = 'Nguyen Minh A',
user.gmail = 'minha@gmail.com',
user.phone = '0132456789',
user.address = 'ha noi, viet nam',
user.nation = 'Viet Nam',
user.slogan = 'nothingggg',
user.gender = 'Nam',
user.language = 'Vietnamese',
user.dateofbirth = '2003-24-11',
user.twitter = 'twitter123',
user.linkedin = 'linkedin321',
user.facebook = 'facebook000',
user.github = 'github0101',




