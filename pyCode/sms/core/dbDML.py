#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__ = 'colby'
from sqlalchemy.orm import sessionmaker
from core.dbInit import *
from sqlalchemy import create_engine
from conf.setting import MysqlLink
import time
class DML(object):
    def __init__(self):
        self.engine = create_engine(
            #MysqlLink()
        "mysql+pymysql://root:root@localhost/sms", encoding = 'utf-8', echo = False
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
    def CreateGrade(self):
        print('当前功能【创建班级】>>')
        gradeName=input('输入班级名称>>')
        data = self.Session.query(Grade) \
            .filter_by(grade_name=gradeName) \
            .first()
        if data!=None:
            print('班级名称[%s]已经存在，请重新输入...' %gradeName)
            self.CreateGrade()
        else:
            now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            gradeObj=Grade(grade_name=gradeName,insert_time=now,update_time=now)
            self.Session.add(gradeObj)
            try:
                self.Session.commit()
                print('创建成功')
                return 1
            except Exception as e:
                print('数据库异常！')
    def DeleteGrade(self):
        print('当前功能【删除班级】>>')
        gradeName = input('删除班级，输入名称>>')
        data = self.Session.query(Grade) \
            .filter_by(grade_name=gradeName) \
            .first()
        if data!=None:
            print('班级名称[%s]已经不存在，未执行任何操作...' %gradeName)
            self.DeleteGrade()
        else:
            self.Session.delete(data)
            self.Session.commit()
            print('删除成功...')
            return 1
    def QueryGrade(self):
        print('当前功能【班级列表】>>')
        data=10
        data=input('显示多少条数据，不输入默认10条：')
        #query后面可以指定字段的名称
        res = self.Session.query(Grade.grade_id,Grade.grade_name).all()
        for i in res:
            print(i[0],i[1])
        return 1