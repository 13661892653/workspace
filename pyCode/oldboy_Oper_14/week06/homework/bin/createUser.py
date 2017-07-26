#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
from school import School
from grade import Grade
from selectView import selectSchool
def CreateSchool():
    print('create CreateSchool')
    schoolName=input('schoolName:')
    s1=School(schoolName)
    s1.schoolSave()
def CreateGrade():
    print('create CreateGrade')
    gradeName=input('gradeName:')
    print('''
            可选择学校：
            %s
            ''' % selectSchool())
    schoolName = input('schoolName:')
    s1 = Grade(gradeName,schoolName)
    s1.gradeSave()
def CreateCourse():
    print('create CreateCourse')
    courseName = input('courseName:')
    cycle = input('cycle:')
    price = input('price:')
    gradename = input('gradename:')
def CreateTeacher():
    print('create CreateTeacher')
    teacherName = input('teacherName:')
    gradeName = input('gradeName:')
    schoolName = input('schoolName:')
def CreateStudent():
    print('create CreateStudent')
    studentName = input('studentName:')
    schoolName = input('schoolName:')
    gradeName = input('gradeName:')
