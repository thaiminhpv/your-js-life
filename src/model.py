from datetime import date


class Users:
    def __init__(self):
        self.name = ""
        self.nickname = ""
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

    @staticmethod
    def getdatafromrequest(data):
        user = Users()
        #user.name = data["name"]
        user.nickname = data["nickname"]
        user.gmail = data["gmail"]
        user.phone = data["phone"]
        user.address = data["address"]
        try:
            user.dateofbirth = data["dateofbirth"]
        except:
            pass
        user.linkedin = data["linkedin"]
        user.facebook = data["facebook"]
        user.github = data["github"]
        user.job = data["job"]
        user.workingtime = data["workingtime"]
        user.introduction = data["introduction"]
        return user

    # get data user from request.form
    @staticmethod
    def getdatafromdb(data):
        user = Users()
        user.name = data[1]
        user.nickname = data[2]
        user.gmail = data[3]
        user.phone = data[4]
        user.address = data[5]
        user.dateofbirth = data[6]
        user.linkedin = data[7]
        user.facebook = data[8]
        user.github = data[9]
        user.job = data[10]
        user.workingtime = data[11]
        user.introduction = data[12]
        return user

    @staticmethod
    def getuserlist(id, data_user):
        data = list()
        data.append(id)
        data.append(data_user.name)
        data.append(data_user.nickname)
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
