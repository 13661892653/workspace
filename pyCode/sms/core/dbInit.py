#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime
engine=create_engine(
    "mysql+pymysql://root:root@localhost/sms",
    encoding='utf-8',echo=True
)
Base=declarative_base()#生成orm基类

class User_Grade(Base):
    __tablename__='user_grade'
    user_id = Column(Integer,primary_key=True)
    grade_id =Column(Integer,primary_key=True)
    insert_time=Column(DateTime)
    update_time=Column(DateTime)

class Class_Record(Base):
    __tablename__ = 'class_record'
    grade_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    insert_time = Column(DateTime)
    update_time = Column(DateTime)

class Course(Base):
    __tablename__ = 'course'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(50))
    insert_time = Column(DateTime)
    update_time = Column(DateTime)

class Course_Record(Base):
    __tablename__ = 'course_record'
    course_id = Column(Integer, primary_key=True)
    section_id = Column(Integer)
    section_name = Column(String(50))
    insert_time = Column(DateTime)
    update_time = Column(DateTime)

class Grade(Base):
    __tablename__ = 'grade'
    grade_id = Column(Integer, primary_key=True)
    course_id = Column(Integer)
    user_id = Column(Integer)
    grade_name= Column(String(50))
    insert_time = Column(DateTime)
    update_time = Column(DateTime)

class Grade_Course(Base):
    __tablename__ = 'grade_course'
    grade_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, primary_key=True)
    insert_time = Column(DateTime)
    update_time = Column(DateTime)

class Role(Base):
    __tablename__ = 'role'
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50))
    type_id = Column(String(50))
    type_name = Column(String(50))
    insert_time = Column(DateTime)
    update_time = Column(DateTime)

class Score(Base):
    __tablename__ = 'score'
    user_id = Column(Integer, primary_key=True)
    grade_id = Column(Integer, primary_key=True)
    class_id = Column(Integer, primary_key=True)
    score = Column(Integer)
    insert_time = Column(DateTime)
    update_time = Column(DateTime)

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    password = Column(String(50))
    user_name = Column(String(50))
    role_id = Column(Integer)
    qq = Column(String(50))
    sex = Column(String(50))
    age = Column(String(50))
    addr = Column(String(50))
    email = Column(String(50))
    insert_time = Column(DateTime)
    update_time = Column(DateTime)
#Base.metadata.create_all(engine)
print('表结构无需初始化化')