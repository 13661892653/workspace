#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
engine=create_engine(
    "mysql+pymysql://root:root@localhost/ob",
    encoding='utf-8',echo=False
)
Base=declarative_base()#生成orm基类
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    password=Column(String(64))
    grade_id=Column(Integer)
    def __repr__(self):
        return '<%s,%s,%s,%s>' %(self.id,self.name,self.password,self.grade_id)
class Grade(Base):
    __tablename__='grade'
    id=Column(Integer,primary_key=True)
    gradename=Column(String(32))
    ds=Column(String(64))

    def __repr__(self):
        return '<%s,%s,%s>' %(self.id,self.gradename,self.ds)
Base.metadata.create_all(engine)
Session_class=sessionmaker(bind=engine)#创建与数据库的会话class
Session=Session_class()#生成session实例，跟cursor一样
#第一种方法
result=Session.query(User,Grade).filter(User.grade_id==Grade.id).all()
print(result)
#第二种方法，有外键才能使用
'''
result=Session.query(User).join(Grade).all()
result=Session.query(User).join(Grade,isouter=True).all()
'''
