from pydantic import BaseModel
from typing import Optional

# 注册用户
class User(BaseModel):
    id:None
    username:str
    password:str
    phone:str
    email:str
    time:str
    role:str

# 登陆用户
class Login(BaseModel):
    username:str
    password:str
