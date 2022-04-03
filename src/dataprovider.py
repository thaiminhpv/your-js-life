from getpass import getpass
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os
from pymysql import NULL
from .model import Users
from src import model


load_dotenv()

DATABASE_CONFIG = dict(
    host="localhost",
    user="root",
    password=os.getenv('DATABASE_PASSWORD'),
    database=os.getenv('DATABASE_NAME'),
)


class InteractDatabse:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(InteractDatabse, cls).__new__(cls)
        return cls.instance

    def executequery(query, parameter=NULL):
        try:
            with connect(**DATABASE_CONFIG) as connection:
                with connection.cursor() as cursor:
                    if parameter != NULL:
                        cursor.execute(query, parameter)
                    else:
                        cursor.execute(query)

                    result = cursor.fetchall()

            return result
        except Error as e:
            print(e)

    def executenonquery(query, parameter=NULL):
        try:
            with connect(**DATABASE_CONFIG) as connection:
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
        parameter = list()
        # get id user
        myTuple = str(InteractDatabse.executequery(
            "SELECT COUNT(*) FROM `portfolio`"))
        id = ''
        for i in range(len(myTuple)):
            if myTuple[i].isdigit():
                id += myTuple[i]
        id = str(int(id)+1)
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
        #query = "INSERT INTO `portfolio` ( `name`, `gmail`, `phone`, `address`, `nation`, `slogan`, `gender`, `language`, `dateofbirth`, `twitter`, `linkedin`, `facebook`, `github`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
        InteractDatabse.executenonquery(query, parameter)
        return id

    # save avt path of user to database

    def savepath(id, path):
        query = "INSERT INTO `avt_path` (`user_id`, `path`) VALUES (%s, %s) "
        parameter = list()
        parameter.append(id)
        parameter.append(path)
        InteractDatabse.executequery(query, parameter)

    # parameter list_edu [id, title, time, content] ; list_exp [id, title, time, content]

    def save_eduexp(list_edu, list_exp):
        # insert education
        query = "INSERT INTO `education` (`portfolio_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_edu:
            InteractDatabse.executequery(query, row)
        # insert experience
        query = "INSERT INTO `experience` (`portfolio_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_exp:
            InteractDatabse.executequery(query, row)

    # pass parameter id and get portfolio

    def getportfolio(id):
        query = "SELECT * FROM `portfolio` WHERE ID = %s" 
        temp = InteractDatabse.executequery(query, (id,))
        result = list()
        for i in range(14):
            if temp[0][i] is None:
                result.append("")
            else:
                result.append(temp[0][i])
        data = model.Users.getdatafromdb(result)
        return data
