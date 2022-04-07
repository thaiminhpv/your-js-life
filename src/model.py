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
        self.address = ""
        self.dateofbirth = date.today()
        self.linkedin = ""
        self.facebook = ""
        self.github = ""
        self.job = ""
        self.workingtime = ""
        self.introduction = ""

    # get data user from request.form

    def getdatafromrequest(data):
        user = Users()
        user.name = data["name"]
        user.gmail = data["gmail"]
        user.phone = data["phone"]
        user.address = data["address"]
        user.dateofbirth = data["dateofbirth"]
        user.linkedin = data["linkedin"]
        user.facebook = data["facebook"]
        user.github = data["github"]
        user.job = data["job"]
        user.workingtime = data["workingtime"]
        user.introduction = data["introduction"]
        return user

    # get data user from request.form
    def getdatafromdb(data):
        user = Users()
        user.name = data[1]
        user.gmail = data[2]
        user.phone = data[3]
        user.address = data[4]
        user.dateofbirth = data[5]
        user.linkedin = data[6]
        user.facebook = data[7]
        user.github = data[8]
        user.address = data[9]
        user.address = data[10]
        user.address = data[11]
        return user

    def getuserlist(data_user):
        data = list()
        data.append(id)
        data.append(data_user.name)
        data.append(data_user.gmail)
        data.append(data_user.phone)
        data.append(data_user.address)
        data.append(data_user.dateofbirth)
        data.append(data_user.linkedin)
        data.append(data_user.facebook)
        data.append(data_user.github)
        data.append(data_user.job)
        data.append(data_user.workingtime)
        data.append(data_user.introduction)
        return data
