from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import HTTPBasic,HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
# Depends是fastapi的依赖注入系统，适用于验证逻辑与路由分离处理
# HTTPException用于返回http错误响应
# status包含http状态码常量，提高代码可读性
# HTTPBasic,HTTPBasicCredentials:fastapi提供的处理http基本认证工具类
# 创建基本认证依赖性实例
app=FastAPI()
security=HTTPBasic()
# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_current_user(credentials:HTTPBasicCredentials=Depends(security)):
    username='Admin'
    password='123456'
    if not(credentials.username==username and credentials.password==password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="认证失败",
            headers={"WWW-Authenticate": "Basic"}
        )
    return credentials.username

@app.get('/login')
def login(username:str=Depends(get_current_user)):
    return {username}