#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from sqlalchemy.orm import sessionmaker
from core.dbInit import *
from sqlalchemy import create_engine
class DML(object):
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:root@localhost/sms",
            encoding='utf-8', echo=False
        )
        self.Session_class = sessionmaker(bind=self.engine)  # 创建与数据库的会话class
        self.Session = self.Session_class()  # 生成session实例，跟cursor一样
    def Add(self):
        #data = self.Session.query(User).filter_by(password='123456').filter_by(name='Guo1').first()
        pass
    def Delete(self):
        pass
    def Update(self):
        pass
    def Query_User(self,user,password):
        '''
        :return: 
        '''
        #登录验证，查询数据库
        data = self.Session.query(User)\
            .filter_by(user_name=user)\
            .filter_by(password=password).first()
        print('data',data)
        return data
