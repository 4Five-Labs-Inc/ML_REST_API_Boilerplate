import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

class Connection:

    """
        initialize constructor
        creates database connection
    """
    def __init__(self):
        try:
            self.pool = psycopg2.pool.SimpleConnectionPool(1, 20, user = os.getenv('DB_USER'),
                                  password = os.getenv('DB_PASSWORD'),
                                  host = os.getenv('DB_HOST'),
                                  port = os.getenv('DB_PORT'),
                                  database = os.getenv('DB_NAME'))
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to Database", error)
    
    """
        fetch_query executes the fetch query
        :param query: any string
        :return: list
    """
    def fetch_query(self, query):
        try:
            connection = self.pool.getconn()
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("Error while executing query", error)
        finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                self.pool.putconn(connection)

    """
        insert_query executes the input query
        :param query: any string
        :param values: dict
        :return: list
    """
    def insert_query(self, query, values):
        try:
            connection = self.pool.getconn()
            cursor = connection.cursor()
            cursor.execute(query, values)
            return connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("Error while executing query", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    self.pool.putconn(connection)