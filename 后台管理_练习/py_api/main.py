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
class Login(BaseModel):
    username:str
    password:str

@app.get("/hello")
async def hello():
    return {"hello,wold!"}

@app.post("/login")
async def login(user_data:Login):
    conn=db_sql()  #数据库连接
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from users where username=%s",(user_data.username,))
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