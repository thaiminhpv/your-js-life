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
        try:
            return {
                'from_name': data['from_name'],
                'from_facebook': data['from_facebook'],
                'from_sex': data['from_sex'],
                'from_gen': data['from_gen'],
                'from_phone': data['from_phone'],
                'from_mail': data['from_mail'],
                'to_name': data['to_name'],
                'to_facebook': data['to_facebook'],
                'to_sex': data['to_sex'],
                'to_phone': data['to_phone'],
                'to_mail': data['to_mail'],
                'to_mess': data['to_mess'],
                'to_request': data['to_request'],
                'gift': data['gift']
            }
        except:
            return "-1"



    @staticmethod
    def getuserlist(data):
        output = list()
        output.append(data['from_name'])
        output.append(data['from_facebook'])
        output.append(data['from_sex'])
        output.append(data['from_gen'])
        output.append(data['from_phone'])
        output.append(data['from_mail'])
        output.append(data['to_name'])
        output.append(data['to_facebook'])
        output.append(data['to_sex'])
        output.append(data['to_phone'])
        output.append(data['to_mail'])
        output.append(data['to_mess'])
        output.append(data['to_request'])
        output.append(data['gift'])
        return output

# def checknvalidValue(data_user, data):
#     print(str(data_user.github))
#     if  data_user.name == None or data_user.nickname == None or  data_user.texterea == None or  data_user.gmail == None or data_user.phone == None or data_user.address == None or data_user.dateofbirth == None or  data_user.job == None or data_user.workingtime == None  :
#        return "-1"
    
#     if  str(data_user.name).replace(" ","") == "" or str(data_user.nickname).replace(" ","") == "" or  str(data_user.texterea).replace(" ","") == "" or  str(data_user.gmail).replace(" ", "") == "" or str(data_user.phone).replace(" ","") == "" or str(data_user.address).replace(" ","") == "" or str(data_user.dateofbirth).replace(" ","") == "" or str(data_user.job).replace(" ","") == "" or str(data_user.workingtime).replace(" ","") == ""  :
#         return "-1"

#     for item in data['education']:
#             if str(item["title"]).replace(" ","") == "" or item["title"] == None:
#                 return "-1"
#             if str(item["time"]).replace(" ","") == "" or item["time"] == None:
#                 return "-1"
#             if str(item["content"]).replace(" ","") == "" or item["content"] == None:
#                 return "-1"

#     for item in data['services']:
#             if str(item["title"]).replace(" ","") == "" or item["title"] == None:
#                 return "-1"
#             if str(item["description"]).replace(" ","") == "" or item["description"] == None:
#                 return "-1"
         
#     for item in data['experience']:
#             if str(item["title"]).replace(" ","") == "" or item["title"] == None:
#                 return "-1"
#             if str(item["time"]).replace(" ","") == "" or item["time"] == None:
#                 return "-1"
#             if str(item["content"]).replace(" ","") == "" or item["content"] == None:
#                 return "-1"

#     for item in data['skills']:
#             if str(item["skill"]).replace(" ","") == "" or item["skill"] == None:
#                 return "-1"
#             if str(item["value"]).replace(" ","") == "" or item["value"] == None:
#                 return "-1"
#    return "1"
           
