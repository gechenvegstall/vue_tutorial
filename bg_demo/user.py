from fastapi import APIRouter,HTTPException
from db import sql_db
import schemas


router=APIRouter()

@router.get("/users")
async def read_user():
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select id,username,password,phone,emali,time from user;"
            cursor.execute(sql)
            user=cursor.fetchall()
            return user
    except Exception as e:
        print(f"操作错误{e}")
