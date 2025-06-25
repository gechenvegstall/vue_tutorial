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
# def db_sql():
#     conn=mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='123456',
#         database='a'
#     )
#     return conn
# def execute_que(query,params=None):
#     conn=db_sql()
#     try:
#         with conn.cursor(dictionary=True) as cursor:
#             cursor.execute(query,params)
#             if query.strip().lower().startswith("select"):
#                 result=cursor.fetchone()
#             else:
#                 conn.commit()
#                 result=cursor.rowcount
#             return result
#     except Exception as e:
#         return e
#     finally:
#         conn.close()