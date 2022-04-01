from getpass import getpass
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

from pymysql import NULL

load_dotenv()

class InteractDatabse:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(InteractDatabse, cls).__new__(cls)
        return cls.instance
    
    def executequery(query,parameter = NULL):
        try:
            with connect(
                host="localhost",
                user="root",
                password= os.getenv('DATABASE_PASSWORD'),
                database=os.getenv('DATABASE_NAME'),
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

    def executenonquery(query,parameter = NULL):
        try:
            with connect(
                host="localhost",
                user="root",
                password= os.getenv('DATABASE_PASSWORD'),
                database=os.getenv('DATABASE_NAME'),
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
    
    # add data user to database and return id of this user
    def adduser(user):
        parameter = list()
        #get id user
        myTuple = str(InteractDatabse.executequery("SELECT COUNT(*) FROM `users`"))
        id = ''
        for i in range(len(myTuple)):
            if myTuple[i].isdigit():
                id += myTuple[i]
        id = str(int(id)+1)
        {   # parameter append
        parameter.append(id),
        parameter.append(user.name),
        parameter.append(user.gmail),
        parameter.append(user.phone),
        parameter.append(user.address),
        parameter.append(user.nation),
        parameter.append(user.slogan),
        parameter.append(user.gender),
        parameter.append(user.language),
        parameter.append(user.dateofbirth),
        parameter.append(user.twitter),
        parameter.append(user.linkedin),
        parameter.append(user.facebook),
        parameter.append(user.github),
        }        
        
        query = "INSERT INTO `users` (`id`, `name`, `gmail`, `phone`, `address`, `nation`, `slogan`, `gender`, `language`, `dateofbirth`, `twitter`, `linkedin`, `facebook`, `github`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        InteractDatabse.executequery(query, parameter)
        return id

    #save avt path of user to database
    def savepath(id, path):
        query = "INSERT INTO `portfolio_js`.`avt_path` (`user_id`, `path`) VALUES (%s, %s) "
        parameter = list()
        parameter.append(id)
        parameter.append(path)
        InteractDatabse.executequery(query,parameter)

    #parameter list_edu [id, title, time, content] ; list_exp [id, title, time, content]
    def save_eduexp(list_edu, list_exp):
        #insert education
        query = "INSERT INTO `education` (`user_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_edu:
            InteractDatabse.executequery(query,row)
        #insert experience
        query = "INSERT INTO `experience` (`user_id`, `title`, `time`, `content`) VALUES (%s, %s, %s, %s)"
        for row in list_exp:
            InteractDatabse.executequery(query,row)
    
    def test(name):
        parameter = list()
        #get id user
        myTuple = str(InteractDatabse.executequery("SELECT COUNT(*) FROM `users`"))
        id = ''
        for i in range(len(myTuple)):
            if myTuple[i].isdigit():
                id += myTuple[i]
        #parameter.append(id)
        parameter.append(name)
        query = "INSERT INTO `users` (`name`) VALUES ( %s )"
        InteractDatabse.executenonquery(query,parameter)
        return id






