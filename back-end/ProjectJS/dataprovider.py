from getpass import getpass
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

from pymysql import NULL

load_dotenv()


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