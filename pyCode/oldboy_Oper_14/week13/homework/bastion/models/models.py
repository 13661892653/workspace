#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import ChoiceType

Base=declarative_base()

class Host_info(Base):
    __tablename__='host_info'
    id=Column(Integer,primary_key=True)
    host_ip=Column(String(14),unique=True)
    host_name=Column(String(20),unique=True)
    host_port=Column(String(5),default=22)

    def __str__(self):
        return self.host_ip

class Local_user_info(Base):
    __tablename__='local_user_info'
    id=Column(Integer,primary_key=True)
    user_name=Column(String(64))
    password=Column(String(64))

    def __str__(self):
        return self.user_name

class Log_info(Base):
    __tablename__='log_info'
    #三键值联合唯一
    __table_args__=(UniqueConstraint('host_ip','user_name','remote_user_name',name='_log_info_unique'),)
    id=Column(Integer,primary_key=True)
    host_ip=Column(String(14))
    user_name=Column(String(64))
    remote_user_name = Column(String(64))
    content=Column(String(128))

    def __str__(self):
        return '<%s-%s-%s:%s>'%(self.host_ip,self.user_name
                                      ,self.remote_user_name,self.content)
class Remote_user_info(Base):
    __tablename__='remote_user_info'
    AuthTypes=[
        ('ssh-password','SSH/Password'),
        ('ssh-key','SSH/KEY')
    ]
    id=Column(Integer,primary_key=True)
    user_name = Column(String(64))
    password = Column(String(64))
    auth_type=Column(ChoiceType(AuthTypes))
    ip = Column(String(14))

    def __str__(self):
        return self.user_name

class User_group(Base):
    __tablename__='user_group'
    id=Column(Integer,primary_key=True)
    host_ip=Column(String(14))
    user_name=Column(String(64))
    user_group = Column(String(12))

    def __str__(self):
        return '%s-%s-%s' %(self.host_ip,self.user_name,self.user_group)

if __name__=='__main__':
    engine = create_engine(
        "mysql+pymysql://root:root@localhost/bastion",
        encoding='utf-8', echo=True
    )
    Base.metadata.create_all(engine)  # 创建表结构