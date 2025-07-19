from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

'''
key可以使用内置secrets随机生成
import secrets
secret_key = secrets.token_urlsafe(32)
'''
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 模拟用户数据
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
schemes=["bcrypt"]使用‘bcrypt算法’
deprecated="auto" 自动处理过时哈希
"""
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

"""验证明文密码跟哈希密码（参数明文密码和储存的哈希密码）"""
def verify_password(plain_password, hashed_password):
    # 哈希值比对返回bool
    return pwd_context.verify(plain_password, hashed_password)
"""数据库中获取用户"""
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict
"""验证用户是否存在跟密码是否正确"""
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user or not verify_password(password, user["hashed_password"]):
        return False
    return user
"""创建jwt"""
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
# 接收前端返回数据
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/return_ok")
async def protected_route():
    return {"message": "认证成功！"}