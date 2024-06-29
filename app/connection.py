import mysql.connector
from app.config import Config


def get_db():
    try:
        db =mysql.connector.connect( host=Config.MYSQL_DATABASE_HOST, 
                                    user=Config.MYSQL_DATABASE_USER,
                                          password=Config.MYSQL_DATABASE_PASSWORD, 
                                          database=Config.MYSQL_DATABASE_DB)
        return db
    except mysql.connector.Error as err :
        raise  Exception("Error: {}".format(err))
        
