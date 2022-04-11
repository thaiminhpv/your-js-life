from datetime import date


class Users:
    def __init__(self):
        self.name = ""
        self.nickname = ""
        self.texterea = "Em anh Vũ\nCTV JS"
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
        data_user = Users()
        data_user.name = data["name"]
        data_user.nickname = data["nickname"]
        data_user.texterea = data["texterea"]
        data_user.gmail = data["gmail"]
        data_user.phone = data["phone"]
        data_user.address = data["address"]
        try:
            data_user.dateofbirth = data["dateofbirth"]
        except:
            pass
        data_user.linkedin = data["linkedin"]
        data_user.facebook = data["facebook"]
        data_user.github = data["github"]
        data_user.job = data["job"]
        data_user.workingtime = data["workingtime"]
        data_user.introduction = data["introduction"]

        return {
            'user': data_user,
            'education': data['education'],
            'services': data['services'],
            'experience': data['experience'],
            'skills': data['skills']
        }



    @staticmethod
    def getuserlist(id, data_user):
        data = list()
        data.append(id)
        data.append(data_user.name)
        data.append(data_user.nickname)
        data.append(data_user.texterea)
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
