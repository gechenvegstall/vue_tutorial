import pymysql
from pymysql.cursors import DictCursor

def db_sql():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        db="a",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )