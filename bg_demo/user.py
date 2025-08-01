from fastapi import APIRouter,HTTPException,Depends,status
from jwt import ExpiredSignatureError,PyJWTError
import jwt
from fastapi.security import OAuth2PasswordBearer
from db import sql_db
import schemas


router=APIRouter()

secret_key = 'pmiqgtNFFVagSB7DZPPoir7Hb7g25qH1eSiou5fqP5s'
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def verify_token_expiration(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token 无效或已过期",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_key, algorithms=ALGORITHM)
        return True  # token 有效
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token 已过期",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except PyJWTError:
        raise credentials_exception

@router.get("/users")
async def read_user(is_valid:bool=Depends(verify_token_expiration)):
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select id,username,password,phone,emali,time from user;"
            cursor.execute(sql)
            user=cursor.fetchall()
            return user
    except Exception as e:
        print(f"操作错误{e}")
