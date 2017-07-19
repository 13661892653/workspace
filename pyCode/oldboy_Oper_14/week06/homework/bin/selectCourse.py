#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:2017-07-19
import pickle
import json
import sys,os
__author__ = "Colby"
homeDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class admin(object):
    def __init__(self,schoolName):
        self.schoolName=schoolName
    def createSchool(self):
        lst=[]
        lst.append(self.schoolName)
        f = open("school.txt", 'r+')
        f.write(json.dumps(lst))
class school(object):
    def __init__(self,name):
        self.name=name
    def createSchool(self):
        pass
    def createCourse(self,name):
        pass
class grade(object):
    pass

class teachear(object):
    pass

class student(object):
    pass

class course(object):
    pass

#a1=admin('北京').createSchool()