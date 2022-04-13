from datetime import date


class Users:
    def __init__(self):
        self.name = None
        self.nickname = None
        self.texterea = None
        self.gmail = None
        self.phone = None
        self.address = None
        self.dateofbirth = None
        self.linkedin = ""
        self.facebook = ""
        self.github = ""
        self.job = None
        self.workingtime = None
        self.introduction = None

    # get data user from request.form

    @staticmethod
    def getdatafromrequest(data):
        data_user = Users()
        try:
            data_user.linkedin = data["linkedin"]
            data_user.facebook = data["facebook"]
            data_user.github = data["github"]
        except:
            pass
        
        try:
            data_user.name = data["name"]
            data_user.nickname = data["nickname"]
            data_user.texterea = data["texterea"]
            data_user.gmail = data["gmail"]
            data_user.phone = data["phone"]
            data_user.address = data["address"]
            data_user.dateofbirth = data["dateOfBirth"]

            data_user.job = data["job"]
            data_user.workingtime = data["workingtime"]
            data_user.introduction = data["introduction"]
            if checknvalidValue(data_user , data) == "-1":
             return "-1"
        except:
            return "-1"
        return {
            'user': data_user,
            'education': data['education'],
            'services': data['services'],
            'experience': data['experience'],
            'skills': data['skills']
        }



    @staticmethod
    def getuserlist(data_user):
        data = list()
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

def checknvalidValue(data_user, data):
    print(str(data_user.github))
    if  data_user.name == None or data_user.nickname == None or  data_user.texterea == None or  data_user.gmail == None or data_user.phone == None or data_user.address == None or data_user.dateofbirth == None or  data_user.job == None or data_user.workingtime == None  :
       return "-1"
    
    if  str(data_user.name).replace(" ","") == "" or str(data_user.nickname).replace(" ","") == "" or  str(data_user.texterea).replace(" ","") == "" or  str(data_user.gmail).replace(" ", "") == "" or str(data_user.phone).replace(" ","") == "" or str(data_user.address).replace(" ","") == "" or str(data_user.dateofbirth).replace(" ","") == "" or str(data_user.job).replace(" ","") == "" or str(data_user.workingtime).replace(" ","") == ""  :
        return "-1"

    for item in data['education']:
            if str(item["title"]).replace(" ","") == "" or item["title"] == None:
                return "-1"
            if str(item["time"]).replace(" ","") == "" or item["time"] == None:
                return "-1"
            if str(item["content"]).replace(" ","") == "" or item["content"] == None:
                return "-1"

    for item in data['services']:
            if str(item["title"]).replace(" ","") == "" or item["title"] == None:
                return "-1"
            if str(item["description"]).replace(" ","") == "" or item["description"] == None:
                return "-1"
         
    for item in data['experience']:
            if str(item["title"]).replace(" ","") == "" or item["title"] == None:
                return "-1"
            if str(item["time"]).replace(" ","") == "" or item["time"] == None:
                return "-1"
            if str(item["content"]).replace(" ","") == "" or item["content"] == None:
                return "-1"

    for item in data['skills']:
            if str(item["skill"]).replace(" ","") == "" or item["skill"] == None:
                return "-1"
            if str(item["value"]).replace(" ","") == "" or item["value"] == None:
                return "-1"
            
    return "1"
           