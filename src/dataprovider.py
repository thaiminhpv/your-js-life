from mysql.connector import connect, Error
from pymysql import NULL

from .config import *
from .model import Users
from src import model


def get_id():
    """
    :return: id of new user
    """
    data = str(InteractDatabase.executequery("SELECT COUNT(*) FROM `portfolio`"))
    id = ''
    for i in range(len(data)):
        if data[i].isdigit():
            id += data[i]
    return str(int(id) + 1)


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

    @staticmethod
    def executenonquery(query, parameter=NULL):
        """
        query update,delete,insert
        :param parameter:
        :return:
        """
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

    @staticmethod
    def addportfolio(data_user):
        """
        add data portfolio to database
        :return: id of this portfolio
        """
        id = get_id()  # id of new user
        parameter = model.Users.getuserlist(id, data_user)  # get data user with datatype: list
        query = "INSERT INTO `portfolio` (`id`, `name`, `gmail`, `phone`, `address`, `dateofbirth`, `linkedin`, `facebook`, `github`, `job`, `workingtime`, `introduction`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
                ap.path,
                e.title,
                e.time,
                e.content,
                s.title,
                s.description,
                ex.title,
                ex.time,
                ex.content,
                ms.skill,
                ms.value
            FROM portfolio as p
                     LEFT JOIN avt_path ap on p.id = ap.portfolio_id
                     LEFT JOIN education e on p.id = e.portfolio_id
                     LEFT JOIN services s on p.id = s.portfolio_id
                     LEFT JOIN experience ex on p.id = ex.portfolio_id
                     LEFT JOIN my_skills ms on p.id = ms.portfolio_id
            WHERE p.id = %s
            """,
            (id,))

        temp = data[0]
        data_user = dict(
            id=temp[0],
            name=temp[1],
            gmail=temp[2],
            phone=temp[3],
            address=temp[4],
            dateofbirth=temp[5],
            linkedin=temp[6],
            facebook=temp[7],
            github=temp[8],
            job=temp[9],
            workingtime=temp[10],
            introduction=temp[11],
        )
        path = temp[12]
        education = [_[13] for _ in data]  # = data[:, 13].T in numpy
        services = [_[14] for _ in data]
        experience = [_[15] for _ in data]
        skills = [_[16] for _ in data]

        return {
            'user': data_user,
            'path': path,
            'education': education,
            'services': services,
            'experience': experience,
            'skills': skills
        }
