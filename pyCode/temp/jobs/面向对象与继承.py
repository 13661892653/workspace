#coding=utf-8
class Class(object):
    num=0
    def _returnNum(self):
        print(Class.num)

class Student(Class):
    def __init__(self,name,age,*args):
        super(Class, self).__init__()
        self.name=name
        self.age = age
        self.args = args
        Class.num = Class.num + 1
    def retName(self):
        print ('大家好我叫%s' %(self.name))

    def retNameAge(self):
        print ('姓名：%s年龄：%s' %(self.name,self.age))

    def Score(self):
        print ('这是我的语文成绩：%s' %(self.args[0][0]))

    def ScoreMax(self):
        print('我最好的成绩是：%s' %(max(self.args[0])))
#实例化
Student1=Student('colby','20',[10,20,30])
Student1.retName()
Student1.retNameAge()
Student1.Score()
Student1.ScoreMax()

#实例化
Student1=Student('colby','20',[10,20,30])
Student1.retName()
Student1.retNameAge()
Student1.Score()
Student1.ScoreMax()
Student1._returnNum()

