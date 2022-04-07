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
        user.address = data["job"]
        user.address = data["workingtime"]
        user.address = data["introduction"]
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
user = Users()
user.name = 'Nguyen Minh A'
user.gmail = 'minha@gmail.com'
user.phone = '0132456789'
user.address = 'hanoi,vietnam'
user.dateofbirth = '2003-24-11'
user.linkedin = 'linkedin321'
user.facebook = 'facebook000'
user.github = 'github0101'
user.job = 'github0101'
user.workingtime= 'github0101'
user.introduction = 'github0101'

experience = [
    {
        'title': 'Master in Computer Engineering',
        'time': '2015-2020',
        'content': 'some details about this field'
    },
    {
        'title': 'Bachelor in Computer Engineering',
        'time': '2011-2014',
        'content': 'some details about this field'
    },
    {
        'title': 'Computer Science',
        'time': '2012-2020',
        'content': 'some details about this field'
    }
]

education = [
    {
        'title': 'Sr. Front End Developer',
        'time': '2020-current',
        'content': 'some details about this field'
    },
    {
        'title': 'Jr. Front end Developer',
        'time': '2011-2014',
        'content': 'some details about this field'
    },
    {
        'title': 'HTML Developer',
        'time': '2012-2020',
        'content': 'some details about this field'
    }
]
services = [
    {
        'title': 'Graphic Design',
        'description': 'some details about this field'
    },
    {
        'title': 'Web Design',
        'description': 'some details about this field'
    }
]
skills = [
    {
        'title': 'python',
        'value': '55'
    },
    {
        'title': 'html',
        'value': '80'
    }
]