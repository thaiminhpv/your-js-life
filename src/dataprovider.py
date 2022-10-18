from symbol import parameters
from mysql.connector import connect, Error
from pymysql import NULL

from .config import *
from .model import Users
from src import model


# def get_id():
#     """
#     :return: id of new user, which is max(id) + 1, if there is no user in database, return 1
#     """
#     data = str(InteractDatabase.executequery("SELECT IFNULL(MAX(id),0) FROM portfolio"))
#     id = ''
#     for i in range(len(data)):
#         if data[i].isdigit():
#             id += data[i]
#     return str(int(id) + 1)


class InteractDatabase:
    connection = None

    def __enter__(self):
        InteractDatabase.connection = connect(**DATABASE_CONFIG)
        return InteractDatabase.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        InteractDatabase.connection.close()

    @staticmethod
    def executequery(query: str, parameter=NULL):
        """
        query select
        :param parameter:
        :return:
        """
        try:
            with InteractDatabase.connection.cursor() as cursor:
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
        connection = connect(**DATABASE_CONFIG) 
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
            connection.close()
            return result
        except Error as e:
            print(e)

    # @staticmethod
    # def executenonquery(query, parameter=NULL):
    #     """
    #     query update,delete,insert
    #     :param parameter:
    #     :return:
    #     """
    #     try:

    #         with InteractDatabase.connection.cursor() as cursor:
    #             if parameter != NULL:
    #                 cursor.execute(query, parameter)
    #             else:
    #                 cursor.execute(query)

    #             result = cursor.lastrowid
    #         InteractDatabase.connection.commit()
    #         return result
    #     except Error as e:
    #         print(e)

    @staticmethod
    def save_data(data):
        parameter = Users.getuserlist(data)
        query = "INSERT INTO `anonymous_shipper`.`user` ( `from_name`, `from_facebook`,`from_sex`, `from_gen`, `from_phone`, `from_mail`, `to_name`, `to_facebook`, `to_sex`, `to_phone`, `to_mail`, `to_mess`, `to_request`, `gift`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        InteractDatabase.executenonquery(query, parameter)
        return "success"

    # @staticmethod
    # def addportfolio(data_user):
    #     """
    #     add data portfolio to database
    #     :return: id of this portfolio
    #     """
    #     #id = get_id()  # id of new user
    #     parameter = model.Users.getuserlist(data_user)  # get data user with datatype: list
    #     query = "INSERT INTO `portfolio` ( `name`, `nickname`,`texterea`, `gmail`, `phone`, `address`, `dateofbirth`, `linkedin`, `facebook`, `github`, `job`, `workingtime`, `introduction`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     id =InteractDatabase.executenonquery(query, parameter)
    #     return id

    # @staticmethod
    # def save_path_to_database(id, path):
    #     """
    #     save avt path of user to database
    #     :param path:
    #     :return:
    #     """
    #     query = "INSERT INTO `avt_path` (`portfolio_id`, `path`) VALUES (%s, %s) "
    #     parameter = list()
    #     parameter.append(id)
    #     parameter.append(path)
    #     with InteractDatabase():
    #         InteractDatabase.executenonquery(query, parameter)


    
