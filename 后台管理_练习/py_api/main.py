from pydantic import BaseModel
from db import db_sql
from fastapi import FastAPI,HTTPException
from  fastapi.middleware.cors import CORSMiddleware
import uvicorn

app=FastAPI()

# 跨域连接
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# basemodel定义数据结构
# 登录信息数据结构
class Login(BaseModel):
    username:str
    password:str

class Post_user(BaseModel):
    username:str
    password:str
    roles:int
# 获取数据库用户表信息
@app.get("/users")
async def user():
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from users;")
            users=cursor.fetchall()
            return users
    finally:
        conn.close()

# 添加用户
@app.post("/post_user")
async def post_user(users:Post_user):
    conn=db_sql()
    try:
        with conn.cursor() as cursor:
            sql="insert into users (username,password,roles) values (%s,%s,%s)"
            cursor.execute(sql,(users.username,users.password,users.roles))
            conn.commit()
    finally:
        conn.close()

@app.post("/login")
async def login(user_data:Login):
    conn=db_sql()  #数据库连接
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from users where username=%s;",(user_data.username,))
            user=cursor.fetchone()
            # print(user)
            # 验证信息
            if user['username']==user_data.username and user["password"]!=user_data.password:
                    raise HTTPException
            else:return user
    finally:
        conn.close()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )