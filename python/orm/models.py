import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Enum,
    DECIMAL,
    DateTime,
    Boolean,
    UniqueConstraint,
    Index
)
from sqlalchemy.orm import declarative_base

# 基础类
Base = declarative_base()

"""engine = create_engine(
    "mysql+pymysql://tom:123@192.168.0.120:3306/db1?charset=utf8mb4",
    # "mysql+pymysql://tom@127.0.0.1:3306/db1?charset=utf8mb4", # 无密码时
    # 超过链接池大小外最多创建的链接
    max_overflow=0,
    # 链接池大小
    pool_size=5,
    # 链接池中没有可用链接则最多等待的秒数，超过该秒数后报错
    pool_timeout=10,
    # 多久之后对链接池中的链接进行一次回收
    pool_recycle=1,
    # 查看原生语句（未格式化）
    echo=True
)"""
# 创建引擎
engine = create_engine(
    "mysql+pymysql://root:123456@localhost:3306/a?charset=utf8mb4",
)
# 绑定引擎,创建会话工厂，关联数据库引擎
Session = sessionmaker(bind=engine)
# 创建线程安全的会话对象（scoped_session 确保每个线程有独立会话）
session = scoped_session(Session)


class UserInfo(Base):
    # 数据库表面
    __tablename__ = 'userinfo'
    # 字段
    id=Column(Integer,primary_key=True,autoincrement=True,comment="序号")
    name = Column(String(32), index=True, nullable=False, comment="姓名")
    age = Column(Integer, nullable=False, comment="年龄")

# 创建表
Base.metadata.create_all(engine)