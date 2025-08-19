import pymysql

user = int(input('id: '))

# 1. 创建连接

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='123456',
                       database='a', charset='utf8mb4')
try:
    # 2. 获取游标对象
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'delete from `users` where `id`=%s',
            (user, )
        )
        if affected_rows == 1:
            print('删除部门成功!!!')
finally:
    # 5. 关闭连接释放资源
    conn.close()