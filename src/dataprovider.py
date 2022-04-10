from mysql.connector import connect, Error
from pymysql import NULL

from .config import *
from .model import Users
from src import model

connection = connect(**DATABASE_CONFIG) 


def get_id():
    """
    :return: id of new user
    """
    data = str(InteractDatabase.executequery("SELECT max(id) FROM portfolio;"))
    id = ''
    for i in range(len(data)):
        if data[i].isdigit():
            id += data[i]
    return str(int(id) + 1)

def ConvertForTuple_Exp_Edu(database):
    list_result = list()
    dict_temp = dict()
    list_key = ["id", "portfolio_id", "title", "time", "content"]
    for item in database:
        tuple_temp = [(list_key[0],item[0]), (list_key[1],item[1]), (list_key[2],item[2]), (list_key[3],item[3]), (list_key[4],item[4])]
        dict_temp = dict(tuple_temp)
        list_result.append(dict_temp)
    return list_result


def ConvertForTuple_Services(database):
    list_result = list()
    dict_temp = dict()
    list_key = ["id", "portfolio_id", "title", "description"]
    for item in database:
        tuple_temp = [(list_key[0],item[0]), (list_key[1],item[1]), (list_key[2],item[2]), (list_key[3],item[3])]
        dict_temp = dict(tuple_temp)
        list_result.append(dict_temp)
    return list_result

def ConvertForTuple_my_skills(database):
    list_result = list()
    dict_temp = dict()
    list_key = ["id", "portfolio_id", "skill", "value"]
    for item in database:
        tuple_temp = [(list_key[0],item[0]), (list_key[1],item[1]), (list_key[2],item[2]), (list_key[3],item[3])]
        dict_temp = dict(tuple_temp)
        list_result.append(dict_temp)
    return list_result


class InteractDatabase:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(InteractDatabase, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def executequery(query: str, parameter=NULL):
        """
        query select
        :param parameter:
        :return:
        """
        if not connection.is_connected():
            connection.connect()
        try:
            with connection.cursor() as cursor:
                if parameter != NULL:
                    cursor.execute(query, parameter)
                else:
                    cursor.execute(query)

                result = cursor.fetchall()

            return result
        except Error as e:
            print(e)

    @staticmethod
    def executenonquery(query, parameter=NULL):
        """
        query update,delete,insert
        :param parameter:
        :return:
        """
        if not connection.is_connected():
                connection.connect()
        try:
            
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

    @staticmethod
    def addportfolio(data_user):
        """
        add data portfolio to database
        :return: id of this portfolio
        """
        id = get_id()  # id of new user
        parameter = model.Users.getuserlist(id, data_user)  # get data user with datatype: list
        query = "INSERT INTO `portfolio` (`id`, `name`, `nickname`, `gmail`, `phone`, `address`, `dateofbirth`, `linkedin`, `facebook`, `github`, `job`, `workingtime`, `introduction`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        InteractDatabase.executenonquery(query, parameter)
        return id

    @staticmethod
    def save_path_to_database(id, path):
        """
        save avt path of user to database
        :param path:
        :return:
        """
        query = "INSERT INTO `avt_path` (`portfolio_id`, `path`) VALUES (%s, %s) "
        parameter = list()
        parameter.append(id)
        parameter.append(path)
        InteractDatabase.executenonquery(query, parameter)
        if not connection.is_connected():
            connection.close()


    # parameter list_edu [id, title, time, content] ; list_exp [id, title, time, content]
    @staticmethod
    def save_edu(id, list_edu):
        # insert education
        query = "INSERT INTO `education` (`portfolio_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_edu:
            parameter = (id, row['title'], row['time'], row['content'])
            InteractDatabase.executenonquery(query, parameter)

    # parameter list_edu [id, title, time, content] ; list_exp [id, title, time, content]
    @staticmethod
    def save_exp(id, list_exp):
        query = "INSERT INTO `experience` (`portfolio_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_exp:
            parameter = (id, row['title'], row['time'], row['content'])
            InteractDatabase.executenonquery(query, parameter)

    @staticmethod
    def save_services(id, list_services):
        query = "INSERT INTO `services` (`portfolio_id`, `title`, `description`) VALUES (%s, %s, %s)"
        for row in list_services:
            parameter = (id, row['title'], row['description'])
            InteractDatabase.executenonquery(query, parameter)

    @staticmethod
    def save_skills(id, list_skill):
        query = "INSERT INTO `my_skills` (`portfolio_id`, `skill`, `value`) VALUES (%s, %s, %s)"
        for row in list_skill:
            parameter = (id, row['skill'], row['value'])
            InteractDatabase.executenonquery(query, parameter)

  
    @staticmethod
    def get_user_data_from_id(id):
        data = InteractDatabase.executequery(
            """
            SELECT
            #   *
                p.id,
                p.name,
                p.nickname,
                p.gmail,
                p.phone,
                p.address,
                p.dateofbirth,
                p.linkedin,
                p.facebook,
                p.github,
                p.job,
                p.workingtime,
                p.introduction,
                ap.path
            FROM portfolio as p
                LEFT JOIN avt_path ap on p.id = ap.portfolio_id
            WHERE p.id = %s
            """,
            (id,))

        temp = data[0]
        data_user = dict(
            id=temp[0],
            name=temp[1],
            nickname=temp[2],
            gmail=temp[3],
            phone=temp[4],
            address=temp[5],
            dateofbirth=temp[6],
            linkedin=temp[7],
            facebook=temp[8],
            github=temp[9],
            job=temp[10],
            workingtime=temp[11],
            introduction=temp[12],
        )
        path = temp[13]
        education = ConvertForTuple_Exp_Edu( InteractDatabase.executequery("SELECT * FROM `education` WHERE `portfolio_id` = %s", (id,)) )
        services = ConvertForTuple_Services( InteractDatabase.executequery("SELECT * FROM `services` WHERE `portfolio_id` = %s", (id,)) )
        experience = ConvertForTuple_Exp_Edu( InteractDatabase.executequery("SELECT * FROM `experience` WHERE `portfolio_id` = %s", (id,)) )
        skills = ConvertForTuple_my_skills( InteractDatabase.executequery("SELECT * FROM `my_skills` WHERE `portfolio_id` = %s", (id,)) )
        if not connection.is_connected():
            connection.close()
        return {
            'user': data_user,
            'path': path,
            'education': education,
            'services': services,
            'experience': experience,
            'skills': skills
        }

   
    @staticmethod
    def get_all_portfolio():
        data = InteractDatabase.executequery(
            """
            SELECT p.id, p.name, p.introduction FROM portfolio as p LIMIT 12
            """)
        return data
