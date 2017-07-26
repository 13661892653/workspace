#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:2017-07-19
import pickle
import json
import sys,os

__author__ = "Colby"

homeDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(homeDir)


class selectView(object):
    def __init__(self):
        pass
class admin(object):
    def __init__(self,roleName):
        self.roleName=roleName
    def createSchool(self):
        while flag:
            inputSchoolName = input('请输入学校名称：')
            inputAddress = input('请输入学校地址：')
            if inputSchoolName=='Q':
                break
            f = open("../db/school.txt", 'r')
            data=f.readlines()
            isExists=0
            for i in data:
                 i=i.replace("\n", "")
                 if inputSchoolName==i.split(' ')[0]:
                    print('学校名已经存在，(Q退出)请重新输入...')
                    isExists=1
                    self.select()
            if isExists==1:
                pass
            else:
                f2 = open("../db/school.txt", 'a')
                f2.write(inputSchoolName+' '+inputAddress+'\n')
                f2.close()
                print('添加成功')
                self.select()
    def querySchool(self):
        print('学校列表查看成功！')
        self.select()
    def select(self):
        print('''＝＝＝＝＝＝＝＝＝欢迎%s童鞋＝＝＝＝＝＝＝＝＝
                1、创建学校
                2、查看存在的学校
                ''' % self.roleName)
        data=input("选择序号即可，请输入：")
        if data=='1':
            self.createSchool()
        elif data=='2':
            self.querySchool()
        elif data=='Q':
            exit()
        else:
           self.select()
class school(object):
    def __init__(self,name):
        self.name=name
    def createGrade(self):
        pass
    def createTeacher(self):
        pass
    def createCourse(self):
        pass
    def select(self):
        print('''＝＝＝＝＝＝＝＝＝欢迎%s童鞋＝＝＝＝＝＝＝＝＝
                        1、创建班级
                        2、创建讲师
                        2、创建课程
                        ''' % self.roleName)
        data = input("选择序号即可，请输入：")
        if data == '1':
            self.createGrade()
        elif data == '2':
            self.createTeacher()
        elif data == '3':
            self.createCourse()
        elif data == 'Q':
            exit()
        else:
            self.select()
class grade(object):
    def __init__(self,name,schoolName):
        pass

class teachear(object):
    def __init__(self,teacherName,schoolName,gradeName):
        pass
    def selectGrade(self):
        pass
    def selectStudent(self):
        pass

class student(object):
    def __init__(self,studentName,schoolName,gradeName,score):
        pass
    def register(self):
        pass
    def payMent(self):
        pass
    def chooseGrade(self):
        pass

class course(object):
    def __init__(self,courseName,cycle,price,gradeName):
        pass

if __name__=="__main__":
    flag=True
    while flag:
        print('''
        请选择您的角色，输入序号即可：
        =======================
            1、系统管理员
            2、学校
            3、讲师
            4、学生
        =======================
        ''')
        data=input('请输入序号：').strip()
        if data=='1':
            a1=admin('管理员')
            a1.select()
        elif data=='2':
            s1=school('学校')
            s1.select()
        elif data=='3':
            pass
        elif data == '4':
            pass
        elif data=='Q':
            print('用户选择退出程序...')
            flag=False
        else:
            pass