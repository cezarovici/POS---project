from peewee import *
import os

DATABASE_NAME = os.getenv("MYSQL_DATABASE", "my_database")
DATABASE_USER = os.getenv("MYSQL_USER", "my_user")
DATABASE_PASSWORD = os.getenv("MYSQL_PASSWORD", "my_password")
DATABASE_HOST = os.getenv("MYSQL_HOST", "mariadb") 
DATABASE_PORT = int(os.getenv("MYSQL_PORT", 3306))
     
db = MySQLDatabase(
    DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)

class DbModel(Model):
    class Meta:
        database = db
