import logging
from datetime import datetime
from os import times

from pydantic import BaseModel
from db import db_sql
from fastapi import FastAPI,HTTPException
from  fastapi.middleware.cors import CORSMiddleware
import bcrypt
import uvicorn

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log",encoding='utf-8'),
        logging.StreamHandler()
    ]
)
app=FastAPI()

# 跨域连接
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# basemodel定义数据结构
# 通用数据结构
class UserBase(BaseModel):
    username:str
    password:str
    roles:int
# 登录
class Login(BaseModel):
    username:str
    password:str

class Post_user(UserBase):
    pass

class delete_user(BaseModel):
    id:int

class put_user(UserBase):
    id:int

# 获取数据库用户表信息
@app.get("/users")
async def user():
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from users;")
            users=cursor.fetchall()
            logging.info("成功查询用户，并且返回")
            return users
    except Exception as e:
        logging.error(f"查询用户失败：{e}")
    finally:
        conn.close()
        logging.info('关闭数据库')

# 添加用户
@app.post("/post_user")
async def post_user(users:Post_user):
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            sql="insert into users (username,password,roles) values (%s,%s,%s)"
            cursor.execute(sql,(users.username,users.password,users.roles))
            conn.commit()
            logging.info(f"成功添加用户{users.username}")
    except Exception as e:
        logging.error(f"添加失败{e}")
        raise
    finally:
        conn.close()
        logging.info("关闭数据库")

#删除用户
@app.delete("/delete_user")
async def del_user(id:delete_user):
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            sql="delete from users where id=%s"
            cursor.execute(sql,(id.id,))
            conn.commit()
            logging.info(f"删除用户{id.id}")
    except Exception as e:
        logging.error(f"删除用户{e}失败")
    finally:
        conn.close()
        logging.info("关闭数据库")

# 修改用户
@app.put("/put_user")
async def post_user(put_u:put_user):
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            sql="update users set username=%s,password=%s,roles=%s where id=%s"
            cursor.execute(sql,(put_u.username,put_u.password,put_u.roles,put_u.id))
            conn.commit()
            logging.info(f"修改用户{put_u.username}成功")
    except Exception as e:
        logging.error(f"修改用户{put_u.username}失败")
    finally:
        conn.close()
        logging.info("关闭数据库")

# 验证登录
@app.post("/login")
async def login(user_data:Login):
    conn=db_sql()  #数据库连接
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from users where username=%s;",(user_data.username,))
            user=cursor.fetchone()
            # print(user)
                # 验证信息
            if user is None:
                raise HTTPException(status_code=404,detail="用户不存在")
                # if user['username']==user_data.username and user["password"]!=user_data.password:
            if user['password']!=user_data.password:
                raise HTTPException(status_code=401,detail="密码不正确")
            logging.info(f"登录用户{user_data.username}成功")
            return user
    except Exception as e:
        logging.error(f"登录用户{user_data.username}失败")
    finally:
        conn.close()
        logging.info("关闭数据库")
# 订单数据数据结构
class table(BaseModel):
    goods:str
    address:str
    state:str
# 删除用户数据结构
class del_table(BaseModel):
    goods:str
# 更新用户数据结构
class put_table(BaseModel):
    state:str
    gooda:str
# 查询订单表
@app.get("/tables")
async def get_table():
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from ordertable;")
            tables=cursor.fetchall()
            return tables
            logging.info("查询成功")
    except Exception as e:
        logging.error("查询订单表失败")
    finally:
        conn.close()
        logging.info("关闭查询订单表")
# 添加订单
@app.post("/post_tables")
async def post_table(tables:table):
    times=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            sql="insert into ordertable values (%s,%s,%s,%s) "
            cursor.execute(sql,(times,tables.goods,tables.address,tables.state))
            conn.commit()
            logging.info('添加订单成功')
    except Exception as e:
        logging.error(f'添加失败{e}')
    finally:
        conn.close()
        logging.info("关闭数据库")

# 删除订单
@app.delete("/delete_table")
async def del_table(del_tables:del_table):
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            sql="delete from ordertable where goods=%s"
            cursor.execute(sql,(del_tables.goods))
            conn.commit()
            logging.info(f"删除用户{del_tables.goods}")
    except Exception as e:
        logging.error(f'删除失败{e}')
    finally:
        conn.close()
        logging.info('关闭数据库')

# 更新订单
@app.post("/put_table")
async def put_table(put_table:put_table):
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            sql="update ordertable set state=%s where goods=%s"
            cursor.execute(sql,(put_table.state,put_table.state))
            conn.commit()
            logging.info(f"更新用户{put_table.gooda}")
    except Exception as e:
        logging.error(f"更新失败{e}")
    finally:
        conn.close()
        logging.info("关闭数据库")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=True,
        reload_dirs=["."],
        reload_delay=1
    )