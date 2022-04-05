from getpass import getpass
from operator import ge
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os
from pymysql import NULL
from .model import Users
from src import model


load_dotenv()

#get id of new user
def get_id():
    data = str(InteractDatabase.executequery("SELECT COUNT(*) FROM `portfolio`"))
    id = ''
    for i in range(len(data)):
        if data[i].isdigit():
            id += data[i]
    return str(int(id)+1)


def AddValueForTuple(database):
    list_result = list()
    dict_temp = dict()
    list_key = ["id", "portfolio_id", "title", "time", "content"]
    for item in database:
        tuple_temp = [(list_key[0],item[0]), (list_key[1],item[1]), (list_key[2],item[2]), (list_key[3],item[3]), (list_key[4],item[4])]
        dict_temp = dict(tuple_temp)
        list_result.append(dict_temp)
    return list_result


def connect_info():
    return {
        "host": "localhost",
        "user": "root",
        "password": os.getenv('DATABASE_PASSWORD'),
        "database": os.getenv('DATABASE_NAME'),
    }


class InteractDatabase:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(InteractDatabase, cls).__new__(cls)
        return cls.instance
  
    # query select
    def executequery(query, parameter=NULL):
        try:
            with connect(
                **connect_info()
            ) as connection:
                with connection.cursor() as cursor:
                    if parameter != NULL:
                        cursor.execute(query, parameter)
                    else:
                        cursor.execute(query)

                    result = cursor.fetchall()

            return result
        except Error as e:
            print(e)
      
    # query update,delete,insert
    def executenonquery(query, parameter=NULL):
        try:
            with connect(
                **connect_info()
            ) as connection:
                with connection.cursor() as cursor:
                    if parameter != NULL:
                        cursor.execute(query, parameter)
                    else:
                        cursor.execute(query)

                    result = cursor.rowcount
                connection.commit()
            return result
        except Error as e:
            print(e)

    # add data portfolio to database and return id of this portfolio

    def addportfolio(data_user):
        id = get_id() # id of new user

        parameter = list()

        parameter.append(id)
        parameter.append(data_user.name)
        parameter.append(data_user.gmail)
        parameter.append(data_user.phone)
        parameter.append(data_user.address)
        parameter.append(data_user.nation)
        parameter.append(data_user.slogan)
        parameter.append(data_user.gender)
        parameter.append(data_user.language)
        parameter.append(data_user.dateofbirth)
        parameter.append(data_user.twitter)
        parameter.append(data_user.linkedin)
        parameter.append(data_user.facebook)
        parameter.append(data_user.github)
        query = "INSERT INTO `portfolio` (`id`, `name`, `gmail`, `phone`, `address` , `nation`, `slogan`, `gender`, `language`, `dateofbirth`, `twitter`, `linkedin`, `facebook`, `github`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
        InteractDatabase.executenonquery(query, parameter)
        return id

    # save avt path of user to database

    def save_path_to_database(id, path):
        query = "INSERT INTO `avt_path` (`portfolio_id`, `path`) VALUES (%s, %s) "
        parameter = list()
        parameter.append(id)
        parameter.append(path)
        InteractDatabase.executenonquery(query, parameter)


    # parameter list_edu [id, title, time, content] ; list_exp [id, title, time, content]
    def save_edu(list_edu):
        # insert education
        query = "INSERT INTO `education` (`portfolio_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_edu:
            InteractDatabase.executequery(query, row)

    def save_exp(list_exp):
        # insert experience
        query = "INSERT INTO `experience` (`portfolio_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_exp:
            InteractDatabase.executequery(query, row)


    # pass parameter id and get portfolio
    def getportfolio(id):
        query = "SELECT * FROM `portfolio` WHERE ID = %s"
        temp = InteractDatabase.executequery(query, (id,))
        result = list()
        for i in range(14):
            if temp[0][i] is None:
                result.append("")
            else:
                result.append(temp[0][i])
        data = model.Users.getdatafromdb(result)
        return data

    #
    def get_exp(id):
        database = InteractDatabase.executequery("SELECT * FROM `experience` WHERE `portfolio_id` = %s", (id,))
        return AddValueForTuple(database)

    def get_edu(id):
        database = InteractDatabase.executequery("SELECT * FROM `education` WHERE `portfolio_id` = %s", (id,))
        return AddValueForTuple(database)


