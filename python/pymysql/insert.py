import pymysql

username = input('username: ')
password = input('password: ')
roles = input('roles: ')


conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='123456',
                       database='a', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'insert into `users`(username,password,roles) values (%s, %s, %s)',
            (username,password,roles)
        )
        if affected_rows == 1:
            print('新增部门成功!!!')
    # 4. 提交事务
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()