import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from db import sql_db
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

app=FastAPI()

# JWT配置
SECRET_KEY=''
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30
# 定义数据模型
class User(BaseModel):
    id:None
    username:str
    password:str
    phone:str
    email:str
    time:None
    role:str
class Login(BaseModel):
    username:str
    password:str


@app.get("/")
async def hello():
    return {'message':"hello11!!"}
@app.post("/adduser",summary="注册用户")
async def AddUser():

@app.get('/user',summary='查询用户接口')
async def read_user():
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select * from user;"
            cursor.execute(sql)
            user=cursor.fetchall()
            return user
    except Exception as e:
        print(f"操作错误{e}")

@app.post("/login",summary="登录验证接口")
async def login(login:Login):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select * from user where username=%s and password=%s;"
            cursor.execute(sql,(login.username,login.password))
            # LoginUser=cursor.fetchall()
            return login.username
    except Exception as e:
        print(f"{e}")




# if __name__=="__main__":
#     uvicorn.run(
#         "main:app",
#         host='127.0.0.1',
#         port=8000,
#         reload=True
#     )