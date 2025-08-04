from fastapi import APIRouter,HTTPException
from db import sql_db

router=APIRouter()

@router.get("/list")
async def list():
    conn=sql_db()
    try:
        with conn.cursor() as cursor:
            sql="select * from article;"
            cursor.execute(sql)
            list=cursor.fetchall()
            return list
    except Exception as e:
        print(f"错误{e}")
